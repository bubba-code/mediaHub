from collections import defaultdict
from xml.etree.ElementTree import Element, tostring
import re, os

# this creates a an xml file from a list of movies

path = r"F:\KODI\Movies"


def dict_to_xml(tag, d):
    elem = Element('movie')
    tit = Element('title')
    tit.text = str(tag)
    elem.append(tit)

    dat = Element('date')
    dat.text = str(d[0])
    elem.append(dat)
    return elem


movs = defaultdict(list)

for d in os.listdir(path):
    movs[d.split('(')[0][:-1]].append(str(d.split('(')[1][:4]))

filename = path+'MediaData.xml'
text_file = open(filename, "w")

text_file.write('<movies>')
for m in movs:
    text_file.write(str(tostring(dict_to_xml(m,movs.get(m))))[2:-1])
text_file.write('</movies>')
text_file.close()

