import scrapy

from tutorial.items import TutorialItem


class StackoverflowSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        # 'https://www.geeksforgeeks.org/connect-django-project-to-mongodb-using-django/'
        'http://quotes.toscrape.com/page/5/'
    ]
    def parse(self, response):
        all_div = response.css('div.quote')
        items = TutorialItem()
        for n in all_div:
            text_all = n.css('span.text::text').extract()
            link_all = n.css('a::attr(href)').extract()
            p = n.css('.tag::text').extract()

            items['title'] = text_all
            items['url'] = link_all
            items['discraption'] = p
            yield items



    # allowed_domains = ["stackoverflow.com"]
    # start_urls = ['http://stackoverflow.com/questions/41905464/use-djangos-models-in-a-scrapy-project-in-the-pipeline']

    # def parse(self, response):
    #     item = TutorialItem()
    #     item["title"] = response.xpath('//div[@id="question-header"]/h1/a/text()').extract()[0]
    #     item["identifier"] = response.url.split("/")[4]
    #     item["url"] = response.url
    #     return item
