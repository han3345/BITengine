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

    

    def start_requests(self):
        subdir='htmlSource'
        os.rmdir(subdir)
        os.mkdir(subdir)
        with open('file_url.txt','w') as g:
                    g.write('')
        with open('error_url.txt', 'w') as h:
                h.write('')

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
        # assume given valid url. not file or picture or something.

        # extract visiable text in html, then save to a file.

            # filename = response.url.replace("/",'_')[7:]
            # if filename[0]=='_':
            #     filename=filename[1:]
            # if filename[-1]=='_':
            #     filename=filename[:-1]+'.html'
            # filepath=os.path.join(self.subdir,filename)
            #
      

        yield {     # return some results
            'url': response.url,
            # 'filename': filename,
            # 'title': response.css('title::text')
        }

        #find suburls to follow

        suburls = response.css('a::attr(href)').getall()  # find all sub urls
        for suburl in suburls:
            if suburl.split('.')[-1] in {'pdf','doc','docx','ppt','pptx','xls','xlsx','zip','rar','jpg','jpeg','gif','png','svg','mp4','mov','avi','flv','mkv','mp3','wma','exe','msi','pkg','iso','dmg'}:
                with open('file_url.txt','a') as g:
                    g.write(suburl+'\n')
                continue
            
            if 'javascript' in suburl:# ignore javascript:void(0) urls.
                continue

            if 'mailto' in suburl: #do not crawl mailto urls.
                continue
            # only follow .htm, .html and .php links.
            if '.htm' in suburl:
                yield response.follow(suburl, callback=self.parse,errback=self.errorback)
            
            if '.php' in suburl:
                yield response.follow(suburl, callback=self.parse,errback=self.errorback)
            
# i created a new branch.