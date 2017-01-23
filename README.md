#My TechBoard

A Techboard that scrapy the news that I interested.

## Scrapy operation

* scrapy createproject TechBoard
* scrapy crawl hackernews

##Mongodb

* start mongod
    * mongod --config /usr/local/etc/mongod.conf
* test mongodb
    * mongo
    * db.test.insert({'name':'test'}) WriteResult({ "nInserted" : 1 })
    * db.test.find()