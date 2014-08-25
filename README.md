# AuctionPro

I built this project to significantly speed up the process of locating gun auctions and processing auction items to determine the going rate for each item on several major gun sites. Before building this, I would manually search through local gun auctions, list each firearm and search for that firearm on multiple sites to gather selling prices and going rates for each firearm. This application turns a 6-8 hour task into a near-instantaneous operation. The project has two major components.

## Frontend application

The frontend to this application is built on Flask and SQLAlchemy. It's a simple interface to gather auction data and review summary reports after a report is generated. 

## Backend crawler

A scrapy application is set up to do the heavy lifting of crawling major gun sites for prices.
