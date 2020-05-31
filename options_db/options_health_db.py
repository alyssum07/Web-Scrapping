from pymongo import MongoClient
import csv
import pandas as pd

class check_value:
    def __init__(self,post):
        val=((float(post["Ask Price"])-float(post["Bid Price"]))/float(post["Bid Price"]))*100
        if(val<5 and val>0):
            self.price=True
        else:
            self.price=False
        if(int(post['OI'])>15000):
            self.oi=True
        else:
            self.oi=False
        if(self.oi and self.price):
            self.both= True
        else:
            self.both= False

def check_condition(post):
    c=check_value(post)
    return c.price,c.oi,c.both

def status(post):
    try:
        client = MongoClient()
        db = client['options_health']
        collec = f"options_collec"
        db.create_collection(collec)
        # print(f"Created New Collection '{collec}'")
        db[collec].insert(post)
        
    except:
        db[collec].insert(post)

class csv_data():
    id={}
    reader=csv.reader(open(r'OptionIds.txt'))
    for row in reader:
        v,k=row
        id[k]=v
    
cd=csv_data()
options_id=cd.id
# print(options_id)

def option_db(final_expdate):

    data=pd.read_csv("nse_bank_nifty_data.csv")
    data2=pd.read_csv("nse_data.csv")
    # data=data.replace('-',"0")
    # print(data.dtypes)
    for i,j,k,l,m,n in zip(data['OI'],data['Volume'],data["BidPrice"],data['AskPrice'],data['Strike Price'],data['LTP']):
        if(i!='-' and j!='-' and k!='-' and l!='-' and n!='-'):
            strike_price="BANKNIFTY"+final_expdate+str(int(m))+"CE"
            if(strike_price in options_id.keys()):
                symbolId=options_id[strike_price]
            else:
                symbolId=""

            post={'exchangeInstrumentID':symbolId,"OI":i,"Volume":j*20,"Bid Price":k,"Ask Price":l,"Strike Price":strike_price} 
            pr,o,validity=check_condition(post)
            if(validity):
                final_post={'exchangeInstrumentID':symbolId,"Strike Price":strike_price,"LTP":n,"Validity":validity}
                status(final_post)
            else:
                if(pr==False):
                    final_post={'exchangeInstrumentID':symbolId,"Strike Price":strike_price,"LTP":n,"Validity":validity,"Reason":"bid ask difference is too high"}
                elif(o==False):
                    final_post={'exchangeInstrumentID':symbolId,"Strike Price":strike_price,"LTP":n,"Validity":validity,"Reason":"Insufficient OI"}
                status(final_post)
            
    for i,j,k,l,m,n in zip(data['OI.1'],data['Volume.1'],data["BidPrice.1"],data['AskPrice.1'],data['Strike Price'],data['LTP.1']):
        if(i!='-' and j!='-' and k!='-' and l!='-' and n!='-'):
            strike_price="BANKNIFTY"+final_expdate+str(int(m))+"PE"
            if(strike_price in options_id.keys()):
                symbolId=options_id[strike_price]
            else:
                symbolId=""
            post={'exchangeInstrumentID':symbolId,"OI":i,"Volume":j*20,"Bid Price":k,"Ask Price":l,"Strike Price":strike_price} 
            pr,o,validity=check_condition(post)
            if(validity):
                final_post={'exchangeInstrumentID':symbolId,"Strike Price":strike_price,"LTP":n,"Validity":validity}
                status(final_post)
            else:
                if(pr==False):
                    final_post={'exchangeInstrumentID':symbolId,"Strike Price":strike_price,"LTP":n,"Validity":validity,"Reason":"bid ask difference is too high"}
                elif(o==False):
                    final_post={'exchangeInstrumentID':symbolId,"Strike Price":strike_price,"LTP":n,"Validity":validity,"Reason":"Insufficient OI"}
                status(final_post)

    for i,j,k,l,m,n in zip(data2['OI'],data2['Volume'],data2["BidPrice"],data2['AskPrice'],data2['Strike Price'],data2['LTP']):
        if(i!='-' and j!='-' and k!='-' and l!='-' and n!='-'):
            strike_price="NIFTY"+final_expdate+str(int(m))+"CE"
            if(strike_price in options_id.keys()):
                symbolId=options_id[strike_price]
            else:
                symbolId=""

            post={'exchangeInstrumentID':symbolId,"OI":i,"Volume":j*75,"Bid Price":k,"Ask Price":l,"Strike Price":strike_price} 
            pr,o,validity=check_condition(post)
            if(validity):
                final_post={'exchangeInstrumentID':symbolId,"Strike Price":strike_price,"LTP":n,"Validity":validity}
                status(final_post)
            else:
                if(pr==False):
                    final_post={'exchangeInstrumentID':symbolId,"Strike Price":strike_price,"LTP":n,"Validity":validity,"Reason":"bid ask difference is too high"}
                elif(o==False):
                    final_post={'exchangeInstrumentID':symbolId,"Strike Price":strike_price,"LTP":n,"Validity":validity,"Reason":"Insufficient OI"}
                status(final_post)

    for i,j,k,l,m,n in zip(data2['OI.1'],data2['Volume.1'],data2["BidPrice.1"],data2['AskPrice.1'],data2['Strike Price'],data2['LTP.1']):
        if(i!='-' and j!='-' and k!='-' and l!='-' and n!='-'):
            strike_price="NIFTY"+final_expdate+str(int(m))+"PE"
            if(strike_price in options_id.keys()):
                symbolId=options_id[strike_price]
            else:
                symbolId=""
            post={'exchangeInstrumentID':symbolId,"OI":i,"Volume":j*75,"Bid Price":k,"Ask Price":l,"Strike Price":strike_price} 
            pr,o,validity=check_condition(post)
            if(validity):
                final_post={'exchangeInstrumentID':symbolId,"Strike Price":strike_price,"LTP":n,"Validity":validity}
                status(final_post)
            else:
                if(pr==False):
                    final_post={'exchangeInstrumentID':symbolId,"Strike Price":strike_price,"LTP":n,"Validity":validity,"Reason":"bid ask difference is too high"}
                elif(o==False):
                    final_post={'exchangeInstrumentID':symbolId,"Strike Price":strike_price,"LTP":n,"Validity":validity,"Reason":"Insufficient OI"}
                status(final_post)

# option_db('23APR20')
