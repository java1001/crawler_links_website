from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from dirbot.items import LinkLoader
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
import os.path
from urlparse import urlparse
from robotparser import RobotFileParser
from urlparse import urljoin
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

terminal_extensions = set([ \
  #
  # text file extensions
  #
  'doc', 'docx', 'log', 'msg', 'pages', 'rtf', 'tt', 'wpd', 'wps' , \
  #
  # data file extensions
  #
  'accdb', 'blg', 'dat', 'db', 'efx', 'mdb', 'pdb', 'pps', 'ppt', \
  'pptx', 'sdb', 'sdf', 'sql', 'vcf', 'wks', 'xls', 'xlsx', \
  #
  # image  file extensions
  #
  'bmp', 'gif', 'jpg', 'png', 'psd', 'psp', 'thm', 'tif', 'tiff' ,\
  'ai', 'drw', 'eps', 'ps', 'svg', \
  '3dm', 'dwg', 'dxf', 'pln', \
  'indd', 'pct', 'pdf', 'qxd', 'qxp', 'rels',  \
  #
  # audio file extensions
  #
  'aac', 'aif', 'iff', 'm3u', 'mid', 'mp3', 'mpa', 'ra', 'wav', 'wma' , \
  #
  # video file extensions
  #
  '3g2', '3gp', 'asf', 'asx', 'avi', 'flv', 'mov', 'mp4', 'mpg', \
  'rm', 'swf', 'vob', 'wmv', \
  #
  # executable file extensions
  #
  'sys', 'dmp', 'app', 'bat', 'cgi', 'exe', 'pif', 'vb', 'ws', \
  #
  # compressed file extensions
  #
  'deb', 'gz', 'pkg', 'rar', 'sit', 'sitx', 'tar', 'gz', 'zip', 'zipx' , \
  #
  # programming file extensions
  #
  'c', 'cc', 'cpp', 'h', 'hpp', 'java', 'pl', 'f', 'for' , \
  #
  # misc file extensions
  #
  'dbx', 'msi', 'part', 'torrent', 'yps', 'dmg', 'iso', 'vcd' , \
  #
  #
  ])

def file_extension(filename) :
    (base, ext) = os.path.splitext(filename)
    if (ext == '.' or ext == ''):
      return ''
    else :
      return ext[1:]

def has_http_in_path(url):
  c = urlparse(url)
  if (c[2].find('http') >= 0) or (c[3].find('http') >= 0):
    return True
  else:
    return False

Permissions = {}

def domain_name(url):
    return urlparse(url)[1]

#  True, if url is allowed by robots.txt permission.  False, otherwise
#
def can_read(url):
  domain = domain_name(url)
  if domain not in Permissions :
         rp = RobotFileParser()
         rp.set_url(urljoin('http://' + domain, 'robots.txt'))
         try :
            rp.read()
         except:
            return False

         Permissions[domain] = rp

  res = False
  try:
    res  = Permissions[domain].can_fetch("*", url)
  except:
    return False

  return res
DOMAIN = 'ebay.com'
URL = 'http://%s' % DOMAIN

class DmozSpider(BaseSpider):
	name = "ebay"
	allowed_domains = ["ebay.com"]
	start_urls = ["http://www.ebay.com"]

	def parse(self, response):
		self.log('Hi, this is an item page! %s' % response.url)
		link = response.url
		#if can_read(link):


		hxs = HtmlXPathSelector(response)
		for url in hxs.select('//a/@href').extract():
			if not url.startswith('http://'):
			    url= URL + url
			if URL in url:
				if ( (file_extension(link).lower() not in terminal_extensions) and
				  (not has_http_in_path(link)) ) :
					il = LinkLoader(response=response)
					il.add_value('link', link)
					yield il.load_item()
			yield Request(url, callback=self.parse)

class DmozSpider(BaseSpider):
	name = "amazon"
	allowed_domains = ["amazon.com"]
	start_urls = ["http://www.amazon.com"]

	def parse(self, response):
		self.log('Hi, this is an item page! %s' % response.url)
		link = response.url
		#if can_read(link):

		hxs = HtmlXPathSelector(response)
		for url in hxs.select('//a/@href').extract():
			if not url.startswith('http://'):
			    url= URL + url
			if URL in url:
				if ( (file_extension(link).lower() not in terminal_extensions) and
				  (not has_http_in_path(link)) ) :
					il = LinkLoader(response=response)
					il.add_value('link', link)
					yield il.load_item()
			yield Request(url, callback=self.parse)

class DmozSpider(BaseSpider):
	name = "rakuten"
	allowed_domains = ["rakuten.com"]
	start_urls = ["http://www.rakuten.com"]

	def parse(self, response):
		self.log('Hi, this is an item page! %s' % response.url)
		link = response.url
		#if can_read(link):

		hxs = HtmlXPathSelector(response)
		for url in hxs.select('//a/@href').extract():
			if not url.startswith('http://'):
			    url= URL + url
			if URL in url:
				if ( (file_extension(link).lower() not in terminal_extensions) and
				  (not has_http_in_path(link)) ) :
					il = LinkLoader(response=response)
					il.add_value('link', link)
					yield il.load_item()
			yield Request(url, callback=self.parse)