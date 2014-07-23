import scrapy
from middlecoin.items import MiddlecoinItem

class MiddlecoinSpider(scrapy.Spider):
    name = "middlecoin"
    allowed_domains = ["middlecoin"]
    start_urls = [
        "http://www.middlecoin.com/allusers.html"
    ]

    def parse(self, response):
        #line=response.xpath('//tr/td[1]/text()').extract()
        #print data
        for line in response.xpath('//tr'):
            item = MiddlecoinItem()
            item['Username'] = line.xpath('td[1]/text()').extract()
            if item['Username']== [] or item['Username']==["Total"]:
                continue
            item['Accepted'] = line.xpath('td[2]/text()').extract()
            item['Rejected'] = line.xpath('td[3]/text()').extract()
            item['ImmatureUnexchangedBalance'] = line.xpath('td[4]/text()').extract()
            item['UnexchangedBalance'] = line.xpath('td[5]/text()').extract()
            item['Balance'] = line.xpath('td[6]/text()').extract()
            item['PaidOut'] = line.xpath('td[7]/a/text()').extract()
            yield item
            #print item['Username'] , "  !!  " , item['Accepted'],"  !!  ",item['Rejected'] , "\n"


#Username    Accepted MH/s (Last Hour)   Rejected MH/s (Last Hour)   Immature Unexchanged Balance (estimated BTC)    Unexchanged Balance (estimated BTC)     Balance (BTC)   Paid Out (BTC)