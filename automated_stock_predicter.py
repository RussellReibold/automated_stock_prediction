#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install selenium


# In[1]:


import selenium
import pandas as pd
import os
import smtplib, ssl
import numpy as np
import shutil

from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sklearn.ensemble import RandomForestClassifier
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from smtplib import SMTP
from my_functions_automated_prediction import get_name_sectors, get_datetime_format, find_bullishPB, remove_missing_values, creating_relation_features, relevant_features, create_main_df, feature_engineering
import pickle
import time


shutil.rmtree("/Users/admin/Desktop/spearmint-vector-student-code/Final_Project/daily_stock_data")
os.mkdir("/Users/admin/Desktop/spearmint-vector-student-code/Final_Project/daily_stock_data")


stock_dictionary = {
              "BG"   : ["Bunge Limited", "Agrar"],

              "ALSN" : ["Allison Transmission", "Automobile"],
              "AN"   : ["Autonation", "Automobile"],
              "BMW"  : ["BMW", "Automobile"],
              "DAI"  : ["Daimler", "Automobile"],
              "GE"   : ["General Electric", "Automobile"],
              "TSLA" : ["Tesla", "Automobile"],

              "DB"   : ["Deutsche Bank", "Banking"],
              "CBK"  : ["Commerzbank", "Banking"],

              "ABBV" : ["Abbvie Inc.", "Biotech"],
              "ACAD" : ["Acadia Pharmaceuticals Inc.", "Biotech"],
              "AMGN" : ["Amgen Inc.", "Biotech"],
              "BIIB" : ["Biogen Inc.", "Biotech"],


              "APHA"  : ["Aphria Inc.", "Cannabis"],
              "AGEEF": ["Halo Labs Inc.", "Cannabis"],
              "CGC"  : ["Canopy Growth", "Cannabis"],
              "CRON" : ["Cronos Group", "Cannabis"],
              "TLRY" : ["Tilray Inc.", "Cannabis"],
              "ACB"  : ["Aurora Cannabis", "Cannabis"],

              "CLDR" : ["Cloudera Inc.", "Cloud"],
              "CRM"  : ["Salesforce", "Cloud"],
              "DOCU" : ["DocuSign", "Cloud"],
              "NOW"  : ["Service Now", "Cloud"],

              "APX"  : ["Appen Limited", "Datenverarbeitung"],
              "D6H"  : ["Datagroup", "Datenverarbeitung"],

              "D"    : ["Dominion Energy", "Energy"],
              "386"  : ["Sinopec", "Energy"],
              "NEE"  : ["NextEra Energy", "Energy"],
              "R6C"  : ["Royal Dutch Shell", "Energy"],

              "DIS"  : ["Walt Disney", "Entertainment"],

              "AAPL" : ["Apple Inc.", "FANG"],
              "AMZN" : ["Amazon Com Inc.", "FANG"],
              "FB"   : ["Facebook Inc.", "FANG"],
              "GOOGL": ["Alphabet Inc.", "FANG"],
              "NFLX" : ["Netflix Inc.", "FANG"],

              "PYPL" : ["PayPal Inc.", "Fintech"],
              "XAUMF": ["Goldmoney Inc.", "Fintech"],
              "SQ"   : ["Square Inc.", "Fintech"],

              "BC"   : ["Brunswick Corp.", "Tourism"],
              "RCL"  : ["Royal Caribbean Group", "Tourism"],

              "EA"   : ["Electronic Arts Inc.", "Gaming"],
              "GME"  : ["Gamestop", "Gaming"],
              "TCEHY" : ["Tencent Holding LTD", "Gaming"],

              "CDW"  : ["CDW Corp.", "Trade"],

              "AGNC" : ["AGNC Investment Corp.", "Real Estate"],
              "CBRE" : ["CBR Group Inc.", "Real Estate"],
              "MHK"  : ["Mohawk Industries", "Real Estate"],
              "EPR"  : ["EPR Properties", "Real Estate"],
              "PLD"  : ["Prologis Inc.", "Real Estate"],

              "CFX"  : ["Colfax Corporation", "Industry"],
              "DOV"  : ["Dover Corp.", "Industry"],
              "MT"   : ["Arcelormittal SA.", "Industry"],
              "CLF"  : ["Cleveland Cliffs Inc.", "Industry"],
              "SLCA" : ["Silicia Holdings Inc.", "Industry"],
              "BAK"  : ["Braskem", "Industry"],
              "TKA"  : ["Thyssenkrupp AG", "Industry"],
              "SLB"  : ["Schlumberger Limited", "Industry"],
              "MMM"  : ["3M Company", "Industry"],

              "9984" : ["Softbank Group", "Investors"],
              "BRK.B": ["Berkshire Hathaway Inc.", "Investors"],

              "LMT"  : ["Lockheed Martin Corp.", "Nuclear Fusion"],

              "BATS" : ["British American Tobacco", "Consumer Products"],
              "JNJ"  : ["Johnson & Johnson", "Consumer Products"],
              "NESN" : ["Nestlé", "Consumer Products"],
              "PG"   : ["Procter & Gamble", "Consumer Products"],

              "BTCUSD": ["Bitcoin", "Crypto"],
              "ETHUSD": ["Ethereum", "Crypto"],
              "IOTUSD": ["Iota", "Crypto"],
              "LINKUSDT": ["Chainlink", "Crypto"],

              "BYND" : ["Beyond Meat", "Consumer Brands"],
              "LVMH" : ["Louis Vuitton", "Consumer Brands"],
              "TXN"  : ["Texas Instruments", "Consumer Brands"],
              "1810": ["Xiaomi Corp.", "Consumer Brands"],
              "ADS"  : ["Adidas AG", "Consumer Brands"],
              "CMG"  : ["Chipotle Mexican Grill", "Consumer Brands"],

              "ISRG" : ["Intuitive Surgical Inc.", "Medi-Tech"],

              "ACIA" : ["Acacia Communications Inc.", "Network"],
              "BR"   : ["Broadridge Financial Solutions", "Network"],
              "COMM" : ["Commscope Holdings", "Network"],
              "M0Y"  : ["Mynaric AG", "Network"],

              "BBY"  : ["Best Buy", "E-Commerce"],
              "BABA" : ["Alibaba Group", "E-Commerce"],
              "OCDO" : ["Ocado Group PLC", "E-Commerce"],
              "SHOP" : ["Shopify Inc.", "E-Commerce"],
              "FVRR" : ["Fiverr LTD", "E-Commerce"],

              "ABC"  : ["Amerisourcebergen Corp.", "Pharma"],
              "ABT"  : ["Abbott Laboratories", "Pharma"],
              "BAS"  : ["BASF", "Pharma"],
              "BAYN" : ["Bayer AG", "Pharma"],
              "CVS"  : ["CVS Healthcare", "Pharma"],
              "DVA"  : ["Davita Inc.", "Pharma"],
              "MCK"  : ["Mckesson Corp.", "Pharma"],
              "NOVO_B": ["Novo Nordisk", "Pharma"],
              "OHI"  : ["Omega Healthcare", "Pharma"],

              "SPCE" : ["Virgin Galactic Holdings", "Space"],
              "UFO"  : ["Procure ETF", "Space"],

              "AA"   : ["Alcoa Corporation", "Raw Materials"],
              "MPC"  : ["Marathon Petroleum", "Raw Materials"],
              "XAUUSD": ["Gold", "Raw Materials"],
              "EMPR" : ["Empire Petroleum", "Raw Materials"],
              "USOIL": ["WTI Crude Oil", "Raw Materials"],
              "LAC"  : ["Lithium Americas Corp.", "Raw Materials"],
              "PALL" : ["Aberdeen Palladium", "Raw Materials"],
              "NNIC" : ["Norilsk Nickel", "Raw Materials"],
              "GOLD" : ["Barrick Gold", "Raw Materials"],
              "KL"   : ["Kirkland Lake Gold", "Raw Materials"],

              "AMAT" : ["Applied Materials Inc.", "Tech/ Chips"],
              "AMD"  : ["Advanced Micro Devices", "Tech/ Chips"],
              "AVGO" : ["Broadcom Inc.", "Tech/ Chips"],
              "BIDU" : ["Baidu Inc.", "Tech/ Chips"],
              "CDNS" : ["Cadence Design Systems", "Tech/ Chips"],
              "IFX"  : ["Infineon Tech AG", "Tech/ Chips"],
              "INTC" : ["Intel Corp.", "Tech/ Chips"],
              "NVDA" : ["Nvidia Corp.", "Tech/ Chips"],
              "ORCL" : ["Oracle Corp.", "Tech/ Chips"],
              "QCOM" : ["Qualcomm Inc.", "Tech/ Chips"],
              "SNAP" : ["Snap Inc.", "Tech/ Chips"],
              "WB"   : ["Weibo Corp.", "Tech/ Chips"],
              "WDC"  : ["Western Digital Corp.", "Tech/ Chips"],
              "MSFT" : ["Microsoft Corp.", "Tech/ Chips"],
              "ASML" : ["ASML Holding", "Tech/ Chips"],
              "TSM"  : ["Taiwan Semiconductor", "Tech/ Chips"],

              "2318" : ["Ping An", "Insurance"],
              "ACGL" : ["Arch Capital Group", "Insurance"],
              "AON"  : ["Aon PLC", "Insurance"],


              "BLDP" : ["Ballard Power", "Hydrogen"],
              
              "LIN"  : ["Linde PLC", "Hydrogen"]}



#Scraping the stockdata from the chartingplatform www.tradingview.com

username = ""
password = ""




options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '/Users/admin/Desktop/spearmint-vector-student-code/Final_Project/daily_stock_data'}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=options)


driver.get("https://www.tradingview.com/")

driver.implicitly_wait(10)

signin = driver.find_element_by_class_name("tv-header__link.tv-header__link--signin.js-header__signin")
signin.click()

driver.implicitly_wait(5)

email = driver.find_element_by_class_name("tv-signin-dialog__social.tv-signin-dialog__toggle-email.js-show-email")
email.click()

driver.implicitly_wait(4)

user = driver.find_element_by_name("username")
user.send_keys(username)

driver.implicitly_wait(2)

password = driver.find_element_by_name("password")
password.send_keys(password)

driver.implicitly_wait(3)

signin2 = driver.find_element_by_class_name("tv-button.tv-button--size_large.tv-button--primary.tv-button--loader")
signin2.click()

time.sleep(5)

element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tv-mainmenu__item.tv-mainmenu__item--chart")))

element.click()

time.sleep(10)


for key in stock_dictionary:

    search = driver.find_element_by_class_name("button-2ioYhFEY.button-o2NxAp-P.apply-common-tooltip.isInteractive-20uLObIc")
    search.click()

    driver.implicitly_wait(3)

    search2 = driver.find_element_by_class_name("search-2XsDfq16.upperCase-UYMmoP0p.input-2pz7DtzH")
    search2.clear()
    search2.send_keys(key)
    search2.send_keys(Keys.RETURN)

    driver.implicitly_wait(5)

    menu = driver.find_element_by_class_name("button-9U4gleap.button-2ioYhFEY.apply-common-tooltip.isInteractive-20uLObIc")
    menu.click()

    driver.implicitly_wait(3)

    export = driver.find_element_by_class_name("apply-common-tooltip.common-tooltip-vertical.item-2xPVYue0.item-1dXqixrD")
    export.click()

    driver.implicitly_wait(3)

    chart = driver.find_element_by_xpath("(//*[@class='selected-2IjEMdXr'])[1]")
    chart.click()

    driver.implicitly_wait(2)

    daily = driver.find_element_by_xpath("(//*[@class='label-3Xqxy756'])[2]")
    daily.click()

    driver.implicitly_wait(2)

    t_format = driver.find_element_by_xpath("(//*[@class='selected-2IjEMdXr'])[2]")
    t_format.click()

    driver.implicitly_wait(3)

    iso = driver.find_element_by_xpath("(//*[@class='labelRow-3Q0rdE8-'])[1]")
    iso.click()

    driver.implicitly_wait(3)

    download = driver.find_element_by_name("submit")
    download.click()


driver.quit()



#Upload the mlm to predict the probability of potential win-trades



direc = "/Users/admin/Desktop/spearmint-vector-student-code/Final_Project/daily_stock_data/"



df_predict = create_main_df(direc, stock_dictionary)

df_predict = remove_missing_values(df_predict)



df_engi = feature_engineering(df_predict)


with open ('rf_grid_10x_pickle', 'rb') as f:
    rf_model = pickle.load(f)


prediction = rf_model.predict_proba(df_engi)
prediction = prediction[:, 1]

df_predict["Probab"] = prediction

high_chances = df_predict[df_predict["Probab"] >= 0.52]

dataframe = print(high_chances[["time", "name", "sector", "Probab"]])


#Setting Up Gmail SMT to send the results to an e-mail address


port = 465
password = ''
sender_email = ''
receiver_email = ''

message = MIMEMultipart("alternative")
message["Subject"] ="Stock Prediction"
message["From"] = sender_email
message["To"] = receiver_email

#Create HTML Version of my message
text = """\
<html>
  <head></head>
  <body>
    {0}
  </body>
</html>
""".format(high_chances.to_html())

#Turn this into html MIMEText objects
part1 = MIMEText(text, 'html')
#Add HTML parts to MIMEMultipart message
message.attach(part1)

#Create secure connection with sever and send email
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())





