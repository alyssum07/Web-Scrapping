# from selenium import webdriver
from nse_scrap import webscrap
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from options_health_db import option_db
import time
import csv

def webscrap1():
    # webscrap()
    connection = MongoClient('localhost', 27017)
    options_collec = f"options_collec"
    try:
        options_db = connection['options_health']
        options_db[options_collec].drop()
        # print('status Collec Deleted')
    except:
        print('error')

    reader=csv.reader(open(r'nse_exp_date.txt'))
    for row in reader:
        try:
            date=row[0]
            print("BANKNIFTY ",date)
            # symbol="BANKNIFTY"
            # url="https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol="+symbol+"&date="+date
            url='https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-9999&symbol=BANKNIFTY&symbol=BANKNIFTY&instrument=OPTIDX&date='+date
            # print(url)
            headers={"User-Agent": "Mozilla/5.0"}
            page=requests.get(url,headers=headers)
            # print(page.text)
            soup=BeautifulSoup(page.content,'lxml')
            # print(soup)
        except Exception as e:
            print("connection error ",e)
        
        try:
            nse_table = soup.find("table",attrs={'id':'octable'})
            # nse_heading =nse_table.tbody.find_all("tr")
            #print(nse_table)

            calls_headers=[]
            puts_headers=[]
            for th,j in zip(nse_table.find_all("th"),range(26)):
                if(j<=14):
                    calls_headers.append(th.text.replace('\n',' ').strip())
                else:
                    puts_headers.append(th.text.replace('\n',' ').strip())
            del calls_headers[0:4]
            del puts_headers[-1]
            calls_data=[]
            puts_data=[]
            tbody =nse_table.find_all("tr")
            trs=tbody[2:]
            # print(trs)
            # print(len(trs))
            for tr in trs[:-1]:
                c_row={}
                p_row={}

                tds=tr.find_all("td")
            # print(tds)

                for td,th in zip(tds[1:12],calls_headers):
                    c_row[th] = re.sub(",|\n","",td.text).strip()
                calls_data.append(c_row)
                
                for td,th in zip(tds[12:25],puts_headers):
                    p_row[th] = re.sub(",|\n","",td.text).strip() 
                puts_data.append(p_row)
            
        except Exception as e:
            print("error",e)

        try:
            first_df = pd.DataFrame(calls_data)
            sec_df = pd.DataFrame(puts_data)
            final_df=pd.concat([first_df,sec_df],axis=1)

            # banknifty_option_db(final_expdate,final_df)

            final_df.to_csv("nse_bank_nifty_data.csv",index=False)

            # first_df.to_csv("nse_data1.csv")
            # sec_df.to_csv("nse_data2.csv")
            print("successful")
            # option_db(option)
        except:
            print('excel error')

        # print(text)
        try:
            select=soup.find("select",attrs={'id':'date'})
            date=select.select_one('option[selected]')['value']
            exp_date=date

            if((exp_date[0] and exp_date[1]).isdigit() ):
                new_expdate=exp_date
            else:
                new_expdate="0"+exp_date
            final_expdate=new_expdate[:5]+new_expdate[7:]
            # print(final_expdate)

            webscrap(date)
            option_db(final_expdate)
        except Exception as e:
            print("server error",e)

while True:
    webscrap1()
    time.sleep(300)

