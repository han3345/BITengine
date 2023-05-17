import scrapy
import os
from urllib.parse import urlparse

class BITSpider(scrapy.Spider):
    name = "bit"
    # with open ('other_utility/bitrenLinks.txt') as f:
    #     start_urls=f.readlines()
    start_urls = [
        'https://www.bit.edu.cn/',
    ]


    subdir='htmlSource'
    if not os.path.exists(subdir):
        os.mkdir(subdir)

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u,callback=self.parse,errback=self.errorback,dont_filter=True)

    def errorback(self,failure):
        # self.dead_links.add(failure.request.url)
        yield{
            # 'error response': failure.value.response,
            'url': failure.request.url
        }
        with open('error_url.txt', 'a') as h:
                h.write(failure.request.url)
                # h.write(failure.value.response)
        
    def parse(self, response):        
        filename = response.url.replace("/",'_')[7:]
        if filename[0]=='_':
            filename=filename[1:]
        if filename[-1]=='_':
            filename=filename[:-1]+'.html'
        # filepath=os.path.join(self.subdir,filename)
        # with open(filepath, 'wb') as f:
        #     f.write(response.body)

        yield {     # return some results
            'url': response.url,
            'filename': filename,
            # 'title': response.css('title::text')
        }

        suburls = response.css('a::attr(href)').getall()  # find all sub urls
        for suburl in suburls:
        # if url end with docx, doc, xls, zip, or pdf, then do something else.
        # if is video or image, don't download.
            if suburl.split('.')[-1] in {'pdf','doc','docx','ppt','pptx','xls','xlsx','zip'}:
                with open('file_url.txt','a') as g:
                    g.write(suburl)
                continue
            
            if 'javascript' in suburl:
                continue

            if 'http' not in suburl:# it's a relative url
                yield response.follow(suburl, callback=self.parse,errback=self.errorback)
                continue

            if 'bit'  in suburl: # do not crawl non-bit domains
                yield response.follow(suburl, callback=self.parse,errback=self.errorback)  
                continue

            if 'mailto' in suburl: # do not crawl non-bit domains
                continue

            # if 'mp.weixin.qq.com' in suburl:
            #     yield response.follow(suburl, callback=self.parse,errback=self.errorback)
            #     continue