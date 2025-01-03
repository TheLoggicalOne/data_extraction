# Data Extraction
## Project Description
### Ultimate Goal: Tools and Pipelines for Extracting Raw Data from different Internet sources  
 and Transforming and Storing Data in our desired form
- we focus mainly on price related data from Persian sources 
- We need to get, extract, clean, translate and transform data and we also might need to store data at many   
different stages of this process
- we can(hopefully) divide this process into three main parts:

more specifically, this project should make followings possible:
#### 1. Getting and storing raw data from target data sources
#### 2. Keep track of each data source, Store its Data and regurarly update it
#### 3. Extracting useful data from raw data, Translating and Transforming raw data

we should creat a system to add and manage target data sources and their information,  
 and for each data source we should have a corresponding database
 (or database table)







## Plan and Roadmap

### 1. we start by Focusing on Specific Data Sources: Telegram Channels and Groups
Do the job for specific sources, with awareness of ultimate goal of generalization and unification of the processes

#### 1.a Data Pipeline for Telegram Daily Update of Car Prices From  `@khodroo_rooz` Channel
- this kind of daily price list is also found in other channels
Any Pipline Should have two main step:
- First Step,getting the raw text/html, Getting Body Of Text Containing Single Day Car Prices, for all days!
- Second Step, extracting data from raw data, From Body Of Text Containing Single Day Car Prices To Our Desired  
 form of Data

Note that no matter how we design our data pipelines, we need to finally extract our data from single messages,  
which here usually is body of text containing single day car prices. So we need a data pipeline from daily car   
prices text to our desired form of data. Also note that instead of text, we could have raw html file   
representing that text. 


##### First Step: Getting Body Of Text Containing Single Day Car Prices

###### Data Pipeline based on whole text content of `@khodroo_rooz`  channel
###### Data Pipeline based on html content of `@khodroo_rooz`  channel in Web Telegram  
###### Data Pipeline based on getting messages and updates from `@khodroo_rooz`  channel through Telegram API


##### Second Step: From Single Body Of Text Containing Single Day Car Prices To Our Desired Data
###### Extracting and Transforming Telegram Daily Car Price Data From a Body of text 
- [scrape_Telegram_car_prices](scrape_Telegram_car_prices.py)

###### Extracting and Transforming Telegram Daily Car Price Data From raw html representation of Body of text

### Stage 2. generalization and unification and abstraction of Data journey from data source to our desired form
#### Abstraction ideas
- ##### concept of data source
  - name
  - type
  - url
  - where to store its raw data: Raw_Data/name
  - where to store data

#### Managing data Sources and their related data and directory paths
We are going to work with different data sources and for each source we want to determine:
  - name
  - type
  - url
  - where to store its raw data, processed data and final data:
    - `Data/Raw_Data/name`
    - `Data/Processed_Data/nam`e
    - `Data/Final_Data/name`
  - some parameter and configurations specific to data source
  - maybe some specific function and codes related to data source
We would like to have these managed in a nice and extendable way.
  - we have created `data_path_manager.py` module to manage general data structure in project. it also
    determines the path of project root in file system
  - we have created `data_source.py` module and DataSource class to keep and manage information about
    specific data sources