======
dirbot
======

This is a Scrapy project to scrape websites from public web directories.

This project is only meant for educational purposes.

Items
=====

The items scraped by this project are websites, and the item is defined in the
class::

    dirbot.items.Website

See the source code for more details.

Spiders
=======

This project contains one spider called ``dmoz`` that you can see by running::

    scrapy list

Spider: dmoz
------------

The ``dmoz`` spider scrapes the Open Directory Project (dmoz.org), and it's
based on the dmoz spider described in the `Scrapy tutorial`_

This spider doesn't crawl the entire dmoz.org site but only a few pages by
default (defined in the ``start_pages`` attribute). These pages are:

* http://www.dmoz.org/Computers/Programming/Languages/Python/Books/
* http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/

So, if you run the spider regularly (with ``scrapy crawl dmoz``) it will scrape
only those two pages.

.. _Scrapy tutorial: http://doc.scrapy.org/intro/tutorial.html 

Pipelines
=========

Filtering by words
------------------

A pipeline to filter out websites containing certain forbidden words in their
description. This pipeline is defined in the class::

    dirbot.pipelines.FilterWordsPipeline

Requiring certain item fields
-----------------------------

A pipeline to discard items that lack of certain fields. This pipeline is
defined in the class::

    dirbot.pipelines.RequiredFieldsPipeline


Storing items in a MySQL database
---------------------------------

A pipeline to store (insert or update) scraped items in a MySQL database. This
pipeline is defined in the class::

    dirbot.pipelines.MySQLStorePipeline

The database schema is defined in ``db/mysql.sql`` and the settings file
contains the default ``MYSQL_*`` settings values. The scraped items will be
stored in the ``website`` database table.

.. note::

    It is *required* to have set up the database schema *before* running the spider.
