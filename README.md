# Data Extraction
## Project Description
### Ultimate Goal: Tools and Pipelines for Extracting Data from different Internet sources and Transforming and Storing Data in our desired form
- we focus mainly on price related data from Persian sources 
- We need to read, extract, clean, translate and transform data and we also might need to store data at many different stages of this process
- we can(hopefully) divide this process into three main parts:
### Main Parts

#### Getting and reading raw data from sources
#### Storing Data at different Stages
#### Extracting useful data from raw data, Translating and Transforming raw data

## Plan and Roadmap
### Stage One: Do the job for specific sources, with awareness of ultimate goal of generalization and unification of the processes
#### Data Pipeline for Telegram Daily Update of Car Prices From  `@khodroo_rooz` Channel
Any Pipline Should have two main step:
- First Step, Getting Body Of Text Containing Single Day Car Prices, for all days!
- Second Step, From Body Of Text Containing Single Day Car Prices To Our Desired form of Data

Note that no matter how we design our data the pipelines, we need to finally extract our data from single messages,
which here usually is body of text containing single day car prices. So we need a data pipeline from daily car prices 
text to our desired form of data. Also note that instead of text, we could have raw html file representing that text. 


##### First Step: Getting Body Of Text Containing Single Day Car Prices

######  Data Pipeline based on whole text content of `@khodroo_rooz`  channel
###### Data Pipeline based on html content of `@khodroo_rooz`  channel in Web Telegram  
###### Data Pipeline based on getting messages and updates from `@khodroo_rooz`  channel through Telegram API


##### Second Step: From Single Body Of Text Containing Single Day Car Prices To Our Desired Data
###### Extracting and Transforming Telegram Daily Car Price Data From a Body of text 
- [scrape_Telegram_car_prices](scrape_Telegram_car_prices.py)

###### Extracting and Transforming Telegram Daily Car Price Data From raw html representation of Body of text