# -*- coding: utf-8 -*-
import scrapy


class UsersSpider(scrapy.spiders.SitemapSpider):
    name = 'users'
    allowed_domains = ['linternaute.com']
    sitemap_urls = ['http://copainsdavant.linternaute.com/sitemap/']

    sitemap_rules = [
        ('.*copainsdavant.linternaute.com.p.*', 'parse_item'),
    ]
    sitemap_follow = ['.*copainsdavant_user/7$']
    #start_urls = ['http://copainsdavant.linternaute.com/p/pierre-bourzeix-3465028']
    #start_urls = ['http://copainsdavant.linternaute.com/sitemap/copainsdavant_photo/86']

    def parse_item(self, response):
        sel=scrapy.Selector(response)
        town=sel.xpath('//h4[text()="Vit à :"]/../p//text()').getall()
        if len(town)>1:
        	town=town[1]
        else:
        	town=None
        yield{
        	'name':sel.xpath('//h4[text()="Prénom Nom :"]/../a//text()').get(),
        	'town':town,
        	'birthday':sel.xpath('//h4[text()="Né le :"]/../p/abbr/@title').get(),
        	'job':sel.xpath('//h4[text()="Profession :"]/../p/text()').get(),
        	'maritalstatus':sel.xpath('//h4[text()="Situation familiale :"]/../p/text()').get(),
        	'children':sel.xpath('//h4[text()="Enfants :"]/../p/text()').get()
        }
