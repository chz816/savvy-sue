# FSAN 850 Project: Savvy Sue
This repo is for FSAN 850/CPEG 646 Project at the University of Delaware, from Group #4: Jared(@jaredws), Daniella(@Danidapena) and Rachel(@chz816). Our project, Savvy Sue, is a search system to help savvy but patient customers to find the best deal.



## Local Setup

Clone the repo, go to the repo folder:

```bash
$ cd savvy-sue
```



Then setup the virtual environment, and install the required packages:

```bash
$ python3.7 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```



## User Interface - Give it a try!

We design a user interface for our search system. Once the user logs into the system, they can select the store, product, and the expected purchased date to see our prediction.

Our UI is developed based on ```tkinter```. There are three inputs needed for our model:

- **Store**: this refers to the 22 available stores including different types of retailers. User can select the store in the left checklist.
- **Item**: this refers to the product category. User can select the product category in the right checklist.
- **Date**: it refers to the expected purchased date. User can select the date in the combo box in the bottom.

```bash
$ python gui.py
```



## Data Collection

We collect our data from Dealmoon.com. As one of the biggest online shopping guide websites, it stores the expired deals. We build our crawler to collect the all available promotional information from our data source, and the detailer crawler is put in ```data-collection```.

To run the crawler:

```bash
$ python data-collection/dealmoon-crawler/crawler.py
```


The collected data ```dealmoon-data.xlsx``` is put in the ```data``` folder.



## Data Cleaning

We clean the data for modeling purpose. We classify the promotional information into several product categories. To make this, we pre-define a dictionary with categories and related keywords. Then we match the promotional information with the keywords to find the related categories. The detailed code is put in ```data-cleaning```.

To run the cleaning:

```bash
$ python data-cleaning/DataCleaning.py
```



## Data Distribution Plots

After running the Data Collection and Data Cleaning, the plots included in the report can be generated by running the following bash command:

``````bash
$ R CMD BATCH distribution_plots.R
``````



## Modeling

We build the logistic regression to predict the likelihood of future promotion. The coefficients from logistic regression is implement in the GUI, and the output is the probability for possible promotion.
