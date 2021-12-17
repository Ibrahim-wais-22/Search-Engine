# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from searchEngine.models import Crawl_tb

class TutorialPipeline:
    def process_item(self, item, spider):
        try:
            question = Crawl_tb.objects.get(identifier=item["discraption"])
            print ("Question already exist")
            return item
        except Crawl_tb.DoesNotExist:
            pass

        crawl_tb = Crawl_tb()
        crawl_tb.identifier = item["discraption"][0]
        crawl_tb.title = item["title"][0]
        crawl_tb.url = item["url"][0]
        crawl_tb.save()
        return item
