import xml.etree.ElementTree as ET

import langdetect

def _root_to_rdf():
    root = ET.Element('rdf:RDF')
    # root.tag = 'rdf:RDF'
    root.set("xmlns:rdf","http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    root.set("xmlns:dc","http://purl.org/dc/elements/1.1/")
    return root

def _subelements_to_rdf(new_root, root):
    for candidate in root.iter("candidate"):

        subelement = ET.SubElement(new_root, 'rdf:Description')
        subelement.set('rdf:about', candidate.find('url').text)

        ET.SubElement(subelement, 'dc:title').text = candidate.find('position').text

        ET.SubElement(subelement, 'dc:description').text = 'Djinni.co - IT Resume'

        ET.SubElement(subelement, 'dc:source').text = candidate.find('url').text

        ET.SubElement(subelement, 'dc:identifier').text = candidate.find('url').text.split('/')[-2]

        ET.SubElement(subelement, 'dc:publisher').text = 'Djinni.co'

        ET.SubElement(subelement, 'dc:format').text = 'text/html'

        ET.SubElement(subelement, 'dc:type').text = 'Human Resources'
        ET.SubElement(subelement, 'dc:subject').text = 'IT Resume'

        if candidate.find('experience').text is not None:
            language_detection_text = candidate.find('experience').text
        elif candidate.find('expectations').text is not None:
            language_detection_text = candidate.find('expectations').text
        elif candidate.find('highlights').text is not None:
            language_detection_text = candidate.find('highlights').text
        else:
            language_detection_text = candidate.find('skills').text
        ET.SubElement(subelement, 'dc:language').text = langdetect.detect(language_detection_text)


def transform(root):
    new_root = _root_to_rdf()
    _subelements_to_rdf(new_root, root)

    return new_root


tree = ET.parse('djinni.xml')
root = tree.getroot()

new_root = transform(root)


ET.ElementTree(new_root).write('rdf_djinni.rdf', encoding="UTF-8", xml_declaration=True, method='xml')
ET.ElementTree(new_root).write('rdf_djinni.xml', encoding="UTF-8", xml_declaration=True, method='xml')
