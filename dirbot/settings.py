# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Link'

ITEM_PIPELINES = [
    'dirbot.pipelines.RequiredFieldsPipeline',
    'dirbot.pipelines.FilterWordsPipeline',
    'dirbot.pipelines.MySQLStorePipeline',
]

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'sample'
MYSQL_USER = 'root'
MYSQL_PASSWD = ''