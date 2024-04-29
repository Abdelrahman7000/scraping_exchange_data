import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

def extract_data():
  # connect to url
  url='https://www.tradingview.com/markets/world-stocks/worlds-largest-companies/'
  res=requests.get(url)
  soup=BeautifulSoup(res.text)
  # getting the column names from the table
  col_names=soup.find('tr',{'class':'row-RdUXZpkv'}).find_all('th',{'class':'cell-seAzPAHn'})
  col_names=[i.text for i in col_names]

  # getting the rows of the table
  rows=soup.find_all('tr',{'class':'row-RdUXZpkv listRow'})

  # loop over each row of the table
  names=[row.td.span.sup.text for row in rows]
  country=[row.find_all('td')[1].img['title'] for row in rows]
  exchange=[row.find_all('td')[2].span.text for row in rows]
  market_cap=[row.find_all('td')[3].text for row in rows]
  price=[row.find_all('td')[4].text for row in rows]
  price_change=[row.find_all('td')[5].text for row in rows]
  volume=[row.find_all('td')[6].text for row in rows]
  rel_volume=[row.find_all('td')[7].text for row in rows]
  price_to_earnings=[row.find_all('td')[8].text for row in rows]
  eps_dilttm=[row.find_all('td')[9].text for row in rows]
  eps_dil_growth=[row.find_all('td')[10].text for row in rows]
  div_yield_ttm=[row.find_all('td')[11].text for row in rows]
  sector=[row.find_all('td')[12].text for row in rows]
  rating=[row.find_all('td')[13].text for row in rows]

  # create dictionary from column names and table rows
  dic={
    col_names[0]:names,
    col_names[1]:country,
    col_names[2]:exchange,
    col_names[3]:market_cap,
    col_names[4]:price,
    col_names[5]:price_change,
    col_names[6]:volume,
    col_names[7]:rel_volume,
    col_names[8]:price_to_earnings,
    col_names[9]:eps_dilttm,
    col_names[10]:eps_dil_growth,
    col_names[11]:div_yield_ttm,
    col_names[12]:sector,
    col_names[13]:rating
  }
  # transforming the dictionary into dataframe
  df=pd.DataFrame(dic)
  return df

if __name__ == "__main__":
  final_table=extract_data()
  final_table.head(3)