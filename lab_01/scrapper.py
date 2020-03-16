import re

import scrapy

from scrapper_items import DjinniItem


class DjinniSpider(scrapy.Spider):
    name = 'djinni'
    start_urls = ['https://djinni.co/set_lang?code=en&next=/developers/']

    max_candidates = 10000

    def start_requests(self):
        self.current_candidates = 0
        yield scrapy.Request(self.start_urls[0], self.parse_main_page)

    def parse_main_page(self, response):
        ten_candidates = ['https://djinni.co/' + x for x in
                          response.css('div.searchresults a.profile::attr(href)').extract()]
        for candidate_url in ten_candidates:
            if self.current_candidates > self.max_candidates:
                return
            self.current_candidates += 1
            yield scrapy.Request(candidate_url, self.parse_candidate)

        # next page
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse_main_page)

    def parse_candidate(self, response):
        candidate = DjinniItem(url=response.url)

        candidate['position'] = response.css('h1::text').extract_first().strip()
        candidate['locations'] = [location.strip() for location in
                                  response.css('div.main-profile-details::text').extract_first().split(',')[:-1]]
        candidate['salary'] = response.css(
            'span.profile-details-salary::text').extract_first().strip()

        rx = re.compile(
            r'[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )'
            r'(?: [Ee] [+-]? \d+ ) ?',
            re.VERBOSE)
        years_of_experience = rx.findall(
            response.css('p.before-hint::text').extract_first().strip())
        years_of_experience = 0 if len(years_of_experience) == 0 else float(years_of_experience[0])
        candidate['years_of_experience'] = years_of_experience

        candidate['english_level'] = response.css('p.before-hint::text').extract_first().split('English')[1].strip()

        html_tags = re.compile(r'<.*?>')
        main_body = {x.strip(): html_tags.sub('', y.strip()) for x, y in
                     zip(response.css('h4 *::text').extract(),
                         response.css('p.profile').extract())}

        candidate['experience'] = main_body['Experience'] if 'Experience' in main_body.keys() else ''
        candidate['skills'] = main_body['Skills'] if 'Skills' in main_body.keys() else ''
        candidate['highlights'] = main_body['Highlights'] if 'Highlights' in main_body.keys() else ''
        candidate['expectations'] = main_body['Looking for'] if 'Looking for' in main_body.keys() else ''

        yield candidate



if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess

    with open('djinni.xml', 'w') as f:
        pass

    process = CrawlerProcess(settings={
        'FEED_EXPORTERS': {
            'xml': 'exporter.DjinniXmlItemExporter',
        },
        'FEED_FORMAT': 'xml',
        'FEED_URI': 'djinni.xml'
    })
    process.crawl(DjinniSpider)
    process.start()  # the script will block here until the crawling is finished
