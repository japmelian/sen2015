import scrapy

from senspider.items import Instance

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["ec2instances.info"]
    start_urls = ["http://www.ec2instances.info"]

    def parse(self, response):
        for sel in response.xpath('//tr'):
            item = Instance()
            item['name'] = sel.xpath('td[@class="apiname"]/text()').extract()
            item['memory'] = sel.xpath('td[@class="memory"]/span/text()').extract()
            item['cores'] = sel.xpath('td[@class="cores"]/span/text()').extract()
            item['cost'] = sel.xpath('td[@class="cost cost-linux"]/text()').extract()
            item['provider'] = "amazon"
            yield item

class GoogleSpider(scrapy.Spider):
    name = "gcloud"
    allowed_domains = ["cloud.google.com"]
    start_urls = ["http://cloud.google.com/pricing/#eu"]

    def parse(self, response):
        for sel in response.xpath('//article/div[@class="pricing-table-content"][1]/table/tbody/tr'):
            item = Instance()
            item['name'] = sel.xpath('td[1]/text()').extract()
            item['memory'] = sel.xpath('td[3]/text()').extract()
            item['cores'] = sel.xpath('td[2]/text()').extract()
            item['cost'] = sel.xpath('td[5]/text()').extract()
            item['provider'] = "gcloud"
            yield item