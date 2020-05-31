from pymongo import MongoClient

def getLTP(exchange_id):
    connection = MongoClient('localhost', 27017)
    options_db = connection['options_health']
    options_collec = f"options_collec"

    match=options_db[options_collec].find_one({"exchangeInstrumentID": exchange_id})
    if(match):
        if(match["Validity"]):
            return match["LTP"]
        else:
            return match["Reason"]
    else:
        return "No OI Present"
ltp=input("Enter LTP value ")
getLTP(ltp)