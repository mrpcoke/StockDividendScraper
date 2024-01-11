from bs4 import BeautifulSoup
import requests
import time
import smtplib
import datetime
import os
import pandas as pd

#This Python program is designed to retrieve the dividend 
#amount (per 100 shares) for next dividend forecast date
#for each listed company using the "Beautiful Soup" module
#Written by Paul E. Coke (c)2023

#Initialise array to hold our Dividend Max URLs
div_url = []
div_url.append("https://www.dividendmax.com/united-kingdom/london-stock-exchange/oil-and-gas-producers/bp-plc/dividends")
div_url.append("https://www.dividendmax.com/united-kingdom/london-stock-exchange/food-and-drug-retailers/sainsbury-j-plc/dividends")
div_url.append("https://www.dividendmax.com/united-kingdom/london-stock-exchange/life-insurance/legal-and-general-group-plc/dividends")
div_url.append("https://www.dividendmax.com/united-kingdom/london-stock-exchange/nonlife-insurance/direct-line-insurance-group-plc/dividends")
div_url.append("https://www.dividendmax.com/united-kingdom/london-stock-exchange/life-insurance/aviva-plc/dividends")
div_url.append("https://www.dividendmax.com/united-kingdom/london-stock-exchange/oil-and-gas-producers/diversified-energy-company-plc/dividends")
div_url.append("https://www.dividendmax.com/united-kingdom/london-stock-exchange/banks/lloyds-banking-group-plc/dividends")
div_url.append("https://www.dividendmax.com/united-kingdom/london-stock-exchange/home-construction/persimmon-plc/dividends")
div_url.append("https://www.dividendmax.com/united-kingdom/london-stock-exchange/home-construction/taylor-wimpey/dividends")
div_url.append("https://www.dividendmax.com/united-kingdom/london-stock-exchange/mobile-telecommunications/vodafone-group-plc/dividends")
div_url.append("https://www.dividendmax.com/united-kingdom/london-stock-exchange/financial-services/mandg-plc/dividends")


def displayDividend(url_arr):
    
    #Specify url headers pertaining to user-agent
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

    #Initialise our arrays that will 
    #hold the data to inserted into the DataFrame
    company_name_collection = []
    prev_payment_collection = []
    next_payment_collection = []
    
    #Iterate through each URL in our array
    for url in url_arr: 
        
        #Split each URL on the forward slash character
        # and convert to an array
        split_url = url.split("/")
        
        #Extract specific company name segment from URL
        company_name = split_url[6] 

        #Grab the page content of each URL and 
        #parse using Beautiful Soup
        page = requests.get(url, headers=headers)    
        soup = BeautifulSoup(page.content, 'html.parser')
        prev_payment = soup.find('div',attrs={'class':'prev your-payment mdc-typography--headline5'}).get_text()
        next_payment = soup.find('div',attrs={'class':'next your-payment mdc-typography--headline5'}).get_text()
        
        #Append values to relevant arrays
        company_name_collection.append(company_name)
        prev_payment_collection.append(prev_payment)
        next_payment_collection.append(next_payment)
        
#Prepare our data to be inserted 
#into our DataFrame object
    data = {
        "Company Name" : list(company_name_collection),
        "Previous Payment" : list(prev_payment_collection),
        "Next Payment" : list(next_payment_collection)        
    }
        
    #Assign dataframe data to variable
    df = pd.DataFrame(data)
    
    #Display data frame and remove default numeric index
    print(df.to_string(index=False,justify='left'))
        #print("Company: {} ----- Previous Payment: {}   -   Next Payment: {}".format(company_name, prev_payment, next_payment))
        
 
 
    
displayDividend(div_url)
    
    