# Data-Engineering-Nano-Degree-Capstone-Project
Project Summary
For this project I pick 2 different main datasets to make analysis which datasets are I94 US Immigration and US city demopgraphic data. I prefer to use python pandas and Apache Spark for data wrangling and data cleansing operations and serving final product of data tables are parquet files analysis data for data science and analysis teams.

<h1>Scope the Project and Gather Data</h1>
Scope
In this project we are creating analysis data for answering set of questions that help our company to increase profit and productivity to further.<br></br>

- Here our questions that we need to get really detailed answers for our analysis ;
- What is the reason of coming usa studying , touristic or business ?
- What is the population of state that they arrive ?
- Which countries people are coming from to Usa ?
- What are the age average of the students, tourists or business people ?
- What are the top 3 states that tourists visit ?

<h3>Describe and Gather Data</h3>
We are going to use 2 different data sources and addition "I94_SAS_Labels_Descriptions.SAS" for this project.

I94 Immigration Data:
Data contains of really cool details about international visitor arrival statistics by world regions. We can answer plenty of questions to make analysis after we complete our work. This data comes from the US National Tourism and Trade Office and this is going to be our core data and we are planning to create our fact table from this immigration dataset then at the end we will going to place our dimension tables around it. You can reach dataset from https://www.trade.gov/national-travel-and-tourism-office

- U.S. City Demographic Data:
  This data comes from OpenSoft. You can reach dataset from https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/

- I94_SAS_Labels_Descriptions.SAS:
  This file is like dictionary file and I will use this file as my some of dim table data source

