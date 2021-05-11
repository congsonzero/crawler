import scrapy

# from Question1.items import Question1Item


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['https://rmz.cr/release/chicago-pd-s08e07-webrip-x264-ion10']

    def parse(self, response):
        url_list=""
        for page in response.xpath("//pre[@class='links']/text()").extract():
            listpage=page.split("\r\n")

            for page_url in (listpage):
                
                yield {
                    "url": url_list
                }
        # item = Question1Item()
        # item["urls"] =  url_list
        # return item

