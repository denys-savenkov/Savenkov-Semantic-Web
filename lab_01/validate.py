from lxml import etree


xmlschema_doc = etree.parse('djinni.xsd')
xmlschema = etree.XMLSchema(xmlschema_doc)

# parse xml
try:
    doc = etree.parse('djinni.xml')
    print('XML well formed, syntax ok.')

# check for file IO error
except IOError:
    print('Invalid File')

# check for XML syntax errors
except etree.XMLSyntaxError as err:
    print('XML Syntax Error, see error_syntax.log')
    with open('error_syntax.log', 'w') as error_log_file:
        error_log_file.write(str(err.error_log))
    quit()

except:
    print('Unknown error, exiting.')
    quit()
