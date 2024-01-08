# Data Extraction
## Project Description
### Ultimate Goal: Tools and Pipelines to Extracting Data from different Internet sources and Transforming and Storing it in our desired form
- we focus mainly on price related data from Persian sources 
- We need to read, extract, clean, translate and transform data and we also might need to store data at many different stages of this process
- we can(hopefully) divide this process into three main parts:
### Main Parts

#### Getting and reading raw data from sources
#### Storing Data at different Stages
#### Extracting useful data from raw data, Translating and Transforming raw data

## Plan and Roadmap
### Stage One: Do the job for specific sources, with awareness of ultimate goal of generalization and unification of the process
#### Data Pipeline for Telegram Daily Update of Car Prices From  `@khodroo_rooz` Channel
Note that no matter how we design our data the pipelines, we need to finally extract our data from single messages, which here usually is daily car prices. So we need a data pipeline from daily car prices to our desired form of data
##### Extracting and Transforming Data From Telegram Daily Car Prices message/text 

#####  Data Pipeline based on whole text content of `@khodroo_rooz`  channel
##### Data Pipeline based on html content of `@khodroo_rooz`  channel in Web Telegram  
##### Data Pipeline based on getting messages and updates from `@khodroo_rooz`  channel through Telegram API
