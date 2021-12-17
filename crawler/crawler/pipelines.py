# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from typing import overload
from itemadapter import ItemAdapter
from searchEngine.models import Crawl_tb


class CrawlerPipeline:
    def process_item(self, item, spider):
        try:
            question = Crawl_tb.objects.get(discraption=item["discraption"])
            print ("Question already exist")
            return item
        except Crawl_tb.DoesNotExist:
            pass

        crawl_tb = Crawl_tb()
        crawl_tb.discraption = item["discraption"]
        crawl_tb.title = item["title"]
        crawl_tb.url = item["url"]
        crawl_tb.save()
        
        return item
