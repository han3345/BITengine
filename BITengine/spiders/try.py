from scrapy.selector import Selector
import scrapy
import re
class TrySpider(scrapy.Spider):
    name = "Try"
html = '''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="apple-mobile-web-app-status-bar-style" content="black" />
<meta name="format-detection" content="telephone=no" />
<title>本周会议_北京理工大学党委办公室/行政办公室</title>
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/subCon.css">
<link rel="shortcut icon" href="../images/favicon.ico" >
<!--[if lt IE 9]>
<script src="../js/html5.js" type="text/javascript"></script>
<![endif]-->
</head>
<!--header开始-->

<header class="header">
  <div class="wrapTop">
    <div class="top">
      <div class="logo"> <a id="logo1" class="logo1" href="http://www.bit.edu.cn/"><img src="../images/logo01.png" alt=""></a> <a id="logo2" class="logo2" href="http://dzb.bit.edu.cn/index.htm"><img src="../images/logo03.png" alt=""></a> </div>
      <div class="top_right">
        <div class="cur_nav"> 
        <ul id="nav1">
		              
                <li><a href="../xxld/xrld/index.htm">学校领导</a>
				                   <div class="subNav">
                        <dl>
                              <dd><a href="../xxld/xrld/index.htm">现任领导</a></dd>
       <dd><a href="../xxld/lrld/index.htm">历任领导</a></dd>
                            </dl>
                   </div>
                </li>
							                 
                <li><a href="../jgsz/dzbjj/index.htm">机构设置</a>
				                   <div class="subNav">
                        <dl>
                              <dd><a href="../jgsz/dzbjj/index.htm">工作职责</a></dd>
       <dd><a href="../jgsz/xyld/index.htm">部门领导</a></dd>
       <dd><a href="../jgsz/gzry/index.htm">工作人员</a></dd>
                            </dl>
                   </div>
                </li>
							                 
                <li><a href="../bszn/bslc/index.htm">办事指南</a>
				                   <div class="subNav">
                        <dl>
                              <dd><a href="../bszn/bslc/index.htm">办事流程</a></dd>
       <dd><a href="../bszn/xz/index.htm">下载</a></dd>
                            </dl>
                   </div>
                </li>
							                   <li><a href="../bftz/index.htm">校内通知</a></li>
               			                   <li><a href="../xxgw/index.htm">规范性文件</a></li>
               			                   <li><a href="index.htm">本周会议</a></li>
               			                   
            </ul>
      </div>
      <div class="gp-topRight1">
         <!-- 当前位置展开 -->
         <div class="gp-search gp-search2 no-overlay" id="gp-search2">
           <div class="gp-ser" >
             <form name="dataForm" action="/cms/search/searchResults.jsp" target="_blank" method="post" accept-charset="utf-8" onSubmit="document.charset='utf-8';">
               <input name="siteID" value="$curChannel.site.ID" type ="hidden">
               <input class="notxt" value="search" name="query" type="text" id="keywords" onFocus="if(value==defaultValue){value='';}" onBlur="if(!value){value=defaultValue;}"
               onclick="if(this.value==''){this.value='';this.form.keywords.style.color='#fff'}">
               <button class="notxt1 iconfont icon-search" name="Submit" type="submit" value="" ></button>
             </form>
           </div>
         </div>
         <!-- 结束 -->
         <span class="gp-overlay"></span>
         <a class="gp-serBtn2 gp-ib iconfont" id="gp-serBtn2" href="javascript:void(0)"></a>
       </div> 
      </div>
      <div class="topLinks">
        <div class="ser">
          <form class="search" name="dataForm" action="http://dzb.bit.edu.cn/cms/web/search/index.jsp" target="_blank" method="post" accept-charset="utf-8" onSubmit="document.charset=&#39;utf-8&#39;;">
            <input name="siteID" value="e1cf5fe993424ec18f4245f3245f1eca" type="hidden">
            <input class="notxt" value="搜索党政办网站" name="query" type="text" id="keywords" onFocus="if(value==defaultValue){value=&#39;&#39;;}" onBlur="if(!value){value=defaultValue;}" onClick="if(this.value==&#39;搜索党政办网站&#39;){this.value=&#39;&#39;;this.form.keywords.style.color=&#39;#fff&#39;}">
            <input class="notxt1 btn" name="Submit" type="submit" value="">
          </form>
        </div>
        <div class="top_nav"> <a href="http://www.bit.edu.cn/" class="fs16"  target="_blank">学校主页</a> </div>
      </div>
    </div>
    <div style="clear:both"></div>
  </div>
</header><!--header结束 -->
<!--content结束-->
<div class="content">
	<div class="row">
		<!-- 移动端二级导航开始 -->
		
<div class="phone_subNav">
			<div class="phone-icon01">
				<div class="mobile-inner-header-icon mobile-inner-header-icon-out">
					MENU
				</div>
			</div>
			<aside class="sub_navm">
				<div class="mobile-inner-navTop">
					<div class="mobileToplink">
						<a href="http://www.bit.edu.cn">学校主页</a>'''

selector = Selector(text=html)

# 使用XPath选择器
name_text = selector.css("meta").xpath("@name").getall()
content_text = selector.css("meta").xpath("@content").getall()
title = selector.xpath("//title/text()").get() 


with open('output.txt', 'w', encoding='utf-8') as file:
    #file.writelines(title+'\n')
    #file.writelines(name+'  ' for name in name_text)
    #file.writelines(content+'  ' for content in content_text)
    file.write(title+'\n')
    file.writelines(content+'\n' for content in content_text)