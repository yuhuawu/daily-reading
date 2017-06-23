# -*- coding: utf-8 -*-
import scrapy


class StratecherySpider(scrapy.Spider):
    name = 'stratechery'
    allowed_domains = ['stratechery.com']
    start_urls = ['http://stratechery.com/']

    def parse(self, response):
        recents = response.xpath('//div[@id="secondary"]/aside[@id="rpjc_widget_cat_recent_posts-2"]/ul/li/a')
        for _li in recents:
            #print _li
            title = _li.xpath('text()').extract()[0].encode('utf-8')
            url = _li.xpath('@href').extract()[0].encode('utf-8')
            print title + ' url: ' + url
        #yeild []
