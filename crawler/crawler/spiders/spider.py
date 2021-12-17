import scrapy

from crawler.items import CrawlerItem

#response.css("#main-container > div:nth-of-type(5) > div > div > div:nth-of-type(4) > a > div > span::text").get()
#alaswdi#        response.css('.mui-col-md-6 > h1::text').get()
#alaswdi#       response.css('.entry-content > p::text').get()
#alaswdi#       response.css('.related-post-wrap > div > a::attr(href)').get()
# response.css(".hsoubArticle .ipsType_richText > ul:nth-of-type(9) > li > a::attr(href)").get() حسوب
class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = [
        "tutorialspoint.com"
    ]
    start_urls = [
        "https://www.tutorialspoint.com/css/index.htm"
    ]


    def parse(self, response):
        
        # all_div = response.css('mui-col-md-6')
        items = CrawlerItem()
        # for n in all_div:
        title = response.css('.mui-col-md-6 > h1::text').get()
        discraption = response.css('.mui-col-md-6 > p::text').get()
        link = response.css('.nxt-btn > a::attr(href)').get()

        items["title"] = title
        items["discraption"] = discraption
        items["url"] = link
        yield items

        next_page =response.css('.nxt-btn > a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)