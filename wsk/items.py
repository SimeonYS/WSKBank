# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 RuxitSynthetic/1.0 v8532902802 t38550 ath9b965f92 altpub cvcv=2'
import scrapy


class WskItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
