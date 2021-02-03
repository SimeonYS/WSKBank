import scrapy
from ..items import WskItem

class WskspiderSpider(scrapy.Spider):
    name = 'wskspider'
    allowed_domains = []
    start_urls = ['https://www.wsk-bank.at/news/']

    def parse(self, response):
        articles = response.xpath('//h2')
        for article in articles:
            article_url = article.xpath('.//a/@href').get()
            yield scrapy.Request(article_url, callback = self.parse_article)

        next_page = response.xpath('//a[@class="next page-numbers"]/@href').get()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_article(self,response):

        title = response.xpath('//div/h1/text()').get()
        date = response.xpath('//div[@class="post-meta"]/text()').get().replace("|","").strip()
        content = ''.join(response.xpath('//div[@class="post-content"]//text()').getall()).replace('\n','').strip()

        item = WskItem()

        item['title'] = title
        item['date'] = date
        item['content'] = content
        yield item




