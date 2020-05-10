import lxml.etree as ET

dom = ET.parse('new_djinni.xml')
xslt = ET.parse('candidates_list.xsl')
transform = ET.XSLT(xslt)
newdom = transform(dom)
print(ET.tostring(newdom, pretty_print=True))
print(newdom)

with open("candidates.html", 'w', encoding='utf-8') as outfile:
    outfile.write(str(newdom))
