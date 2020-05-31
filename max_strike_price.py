from nse_scrap import webscrap
import pandas as pd
import time

# webscrap()
# df= pd.read_excel(r'nse_data.csv')
def max_strike():
    webscrap()
    neg={}
    pos={}
    neg1={}
    pos1={}
    data=pd.read_csv("nse_data.csv")
    data=data.replace('-',"0")

    # print(data)
    # convert_dict={'OI':int,"Chng in OI":int,"Volume":int}
    # data=data.astype(convert_dict)

    data[['OI','Chng in OI','Volume','OI.1','Chng in OI.1','Volume.1']]=data[['OI','Chng in OI',
    'Volume','OI.1','Chng in OI.1','Volume.1']].apply(pd.to_numeric)

    # print(data.dtypes)
    for i,j in zip(data["Chng in OI"],data["Strike Price"]):
        if(i<0):
            neg.update({i:j})
        else:
            neg.update({"0":j})
        if(i>0):
            pos.update({i:j})
        else:
            pos.update({"0":j})
    # print(pos, "\n",neg)
    for i,j in zip(data["Chng in OI.1"],data["Strike Price"]):
        if(i<0):
            neg1.update({i:j})
        else:
            neg1.update({"0":j})
        if(i>0):
            pos1.update({i:j})
        else:
            pos1.update({"0":j})
    # print(neg)
    chngoi1=pd.DataFrame({"Neg chng in OI":list(neg.keys()),"Strike Price":list(neg.values())})
    chngoi2=pd.DataFrame({"Pos chng in OI":list(pos.keys()),"Strike Price":list(pos.values())})
    chngoi3=pd.DataFrame({"Neg chng in OI":list(neg1.keys()),"Strike Price":list(neg1.values())})
    chngoi4=pd.DataFrame({"Pos chng in OI":list(pos1.keys()),"Strike Price":list(pos1.values())})
    chngoi1.to_csv("chngoi1.csv",index=False)
    chngoi2.to_csv("chngoi2.csv",index=False)
    chngoi3.to_csv("chngoi3.csv",index=False)
    chngoi4.to_csv("chngoi4.csv",index=False)
    datachng1=pd.read_csv("chngoi1.csv")
    datachng2=pd.read_csv("chngoi2.csv")
    datachng3=pd.read_csv("chngoi3.csv")
    datachng4=pd.read_csv("chngoi4.csv")
    # print(datachng)
    

    #=============Calls================
    max_oi=data.nlargest(5,['OI'])
    max_negchngoi=datachng1.nlargest(5,['Neg chng in OI'])
    max_poschngoi=datachng2.nlargest(5,['Pos chng in OI'])
    max_vol=data.nlargest(5,['Volume'])
    # df0=pd.DataFrame({" ":[" "]})
    df=pd.DataFrame(max_oi[['OI','Strike Price']])
    df1=pd.DataFrame(max_negchngoi[['Neg chng in OI','Strike Price']])
    df2=pd.DataFrame(max_poschngoi[['Pos chng in OI','Strike Price']])
    df3=pd.DataFrame(max_vol[['Volume','Strike Price']])
    
    # call_max=pd.concat([df,df0,df1,df0,df2],axis=1,sort=False)
    df.to_csv("Call_Max_OI.csv",index=False)
    df1.to_csv("Call_Max_negchnginOI.csv",index=False)
    df2.to_csv("Call_Max_poschnginOI.csv",index=False)
    df3.to_csv("Call_Max_volume.csv",index=False)
    
    #=============Puts=====================
    max_oi1=data.nlargest(5,['OI.1'])
    # print(max_oi1)
    # max_chngoi1=data.nlargest(5,['Chng in OI.1'])
    max_negchngoi1=datachng3.nlargest(5,['Neg chng in OI'])
    max_poschngoi1=datachng4.nlargest(5,['Pos chng in OI'])
    max_vol1=data.nlargest(5,['Volume.1'])
    # f0=pd.DataFrame({" ":[" "]})
    f=pd.DataFrame(max_oi1[['OI.1','Strike Price']])
    # f1=pd.DataFrame(max_chngoi1[['Chng in OI.1','Strike Price']])
    f1=pd.DataFrame(max_negchngoi1[['Neg chng in OI','Strike Price']])
    f2=pd.DataFrame(max_poschngoi1[['Pos chng in OI','Strike Price']])
    f3=pd.DataFrame(max_vol1[['Volume.1','Strike Price']])
    # put_max=pd.concat([f,f0,f1,f0,f2],axis=1)
    f.to_csv("Put_Max_OI.csv",index=False)
    f1.to_csv("Put_Max_negchnginOI.csv",index=False)
    f2.to_csv("Put_Max_poschnginOI.csv",index=False)
    f3.to_csv("Put_Max_Vol.csv",index=False)

    #=============Final data===========
    # row=pd.DataFrame({'Call:':[' ']})
    # row1=pd.DataFrame({'Puts:':[' ']})
    # final_df=pd.concat([row,call_max,f0,row1,put_max],axis=1)
    # final_df.to_csv("Max_strike_values.csv",index=False)

    # for i in data["OI"]:
    #     j=i.replace(",","")
    #     if(j!="-"):
    #         # print(j)
    #         ar.append(int(j))      
    # ar.sort()
    # print(ar)
    # print(data["Strike Price"])
while True:
    max_strike()
    time.sleep(60)
