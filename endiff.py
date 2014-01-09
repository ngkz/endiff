#!/usr/bin/python3
import xml.dom.minidom
import tempfile
import subprocess
import sys

def prettify_enex(path):
    enex = xml.dom.minidom.parse(path) # or xml.dom.minidom.parseString(xml_string)
    for content_node in enex.getElementsByTagName("content"):
        note = xml.dom.minidom.parseString(content_node.firstChild.data)
        content_node.firstChild.data = note.toprettyxml()
    tmp = tempfile.NamedTemporaryFile()
    tmp.write(enex.toprettyxml().encode("utf-8"));
    return tmp

if len(sys.argv) != 3:
    sys.stderr.write("Usage: {0} FILE1 FILE2\n".format(sys.argv[0]))
    sys.exit(0)

with prettify_enex(sys.argv[1]) as f1, prettify_enex(sys.argv[2]) as f2:
    subprocess.call(["vimdiff", f1.name, f2.name])
