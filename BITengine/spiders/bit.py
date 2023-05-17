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

    allowed_domains=[
        'bit.edu.cn',
    ]

    subdir='htmlSource'
    if not os.path.exists(subdir):
        os.mkdir(subdir)

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u,callback=self.parse,errback=self.errorback)

    def errorback(self,failure):
        # self.dead_links.add(failure.request.url)
        yield{
            # 'error response': failure.value.response,
            'error url': failure.request.url
        }
        with open('error_url.txt', 'a') as h:
                h.write(failure.request.url+'\n')
                # h.write(failure.value.response)
        
    def parse(self, response):
        # if url end with docx, doc, xls, zip, or pdf, then do something else.
        # if is video or image, don't download.
        if response.url.split('.')[-1] in {'pdf','doc','docx','ppt','pptx','xls','xlsx','zip'}:
            pass
        else:
            filename = response.url.replace("/",'_')[7:]
            if filename[0]=='_':
                filename=filename[1:]
            if filename[-1]=='_':
                filename=filename[:-1]+'.html'
            filepath=os.path.join(self.subdir,filename)
            #
            name_text = response.css("meta").xpath("@name").getall()
            content_text = response.css("meta").xpath("@content").getall()
            html_text = response.css("a").xpath("@href").getall()
            title = response.xpath("//title/text()").get() 
            #sel = scrapy.Selector(text=response.body)
            #title_text = sel.xpath('//title/text()').get()
            with open(filepath, 'wb') as f:
                f.writelines(title+'\n')
                f.writelines(name+'\n'  for name in name_text)
                f.writelines(content+'\n' for content in content_text)
                f.writelines(html+'\n' for html in html_text)


        yield {     # return some results
            'url': response.url,
            # 'filename': filename,
            # 'title': response.css('title::text')
        }

        suburls = response.css('a::attr(href)').getall()  # find all sub urls
        for suburl in suburls:
        # if url end with docx, doc, xls, zip, or pdf, then do something else.
        # if is video or image, don't download.
        # why not only download htm, html and php?
            if suburl.split('.')[-1] in {'pdf','doc','docx','ppt','pptx','xls','xlsx','zip','rar','jpg','jpeg','gif','png','svg','mp4','mov','avi','flv','mkv','mp3','wma','exe','msi','pkg','iso','dmg'}:
                with open('file_url.txt','a') as g:
                    g.write(suburl+'\n')
                continue
            
            if 'javascript' in suburl:# ignore javascript:void(0) urls.
                continue

            if 'mailto' in suburl: #do not crawl mailto urls.
                continue

            yield response.follow(suburl, callback=self.parse,errback=self.errorback)