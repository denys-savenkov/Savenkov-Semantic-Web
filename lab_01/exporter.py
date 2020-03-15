from scrapy.exporters import XmlItemExporter


class DjinniXmlItemExporter(XmlItemExporter):

    def __init__(self, file, **kwargs):
        super(DjinniXmlItemExporter, self).__init__(file,
                                                    root_element="candidates",
                                                    item_element="candidate",
                                                    **kwargs)

