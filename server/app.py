import falcon
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from pyxlsb import open_workbook as open_xlsb

%matplotlib inline

from pyxlsb import open_workbook as open_xlsb

df1 = []

with open_xlsb('Shogun Report Nov 2018.xlsb') as wb:
    with wb.get_sheet(1) as sheet:
        for row in sheet.rows():
            df1.append([item.v for item in row])

df1 = pd.DataFrame(df1[1:], columns=df1[0])
df1=df1.drop(['SEQUENCE','Sr. No.','NET_SALES_QTY','NET_SALES_Cases.Units','UPC','NET_SALES_VALUE','SCHEME_DISCOUNT','OTHER_DISCOUNT','TAX_PERCENTAGE','Net Value Calculation','MRP','TUR','PARTY_CODE','BASEPACK CODE','SKU7_CODE','PRODUCT_NAME',],axis=1)



df2 = []

with open_xlsb('GPS Location Data.xlsb') as wb:
    with wb.get_sheet(1) as sheet:
        for row in sheet.rows():
            df2.append([item.v for item in row])

df2 = pd.DataFrame(df2[1:], columns=df2[0])

d=pd.merge(df1, df2, on=['PARTY_HLL_CODE'])

d1 = pd.DataFrame(columns=['PARTY_HLL_CODE','W_KG'], data=d[['PARTY_HLL_CODE','NET_SALES_WEIGHT_IN_KGS']].values)

d1["W_KG"] = pd.to_numeric(d1["W_KG"])

d1=d1.groupby(['PARTY_HLL_CODE'])['W_KG'].sum()


df=pd.merge(d,d1 , on=['PARTY_HLL_CODE'])
df=df.drop(['SERVICING PLG', 'PARTY_NAME','Verified','NET_SALES_WEIGHT_IN_KGS'],axis=1)
e=df.PARTY_HLL_CODE.unique()
df=df.drop_duplicates(['PARTY_HLL_CODE'], keep='first')
df=df.drop([    'Delivery Date',           'VEHICLE',         'BEAT_NAME',
                 'BILL_NUMBER',         'BILL_DATE',None,
              'Current Latitude',
       'Current Longitude'],axis=1)

data=list(df['W_KG'].head(3))

import copy
def comb(target,data):
    for i in range(len(data)):
        new_target = copy.copy(target)
        new_data = copy.copy(data)
        new_target.append(data[i])
        new_data = data[i+1:]
        final_target.append(new_target)
        comb(new_target,new_data)
    return final_target
    

new_target=[]
target = []
target1 = []

final_target = []
l=[]

data_i=[]
for i in range(len(data)):
    data_i.append(i)
print(data_i)

def check():
    if()
    pp=comb(target,data)
#     kl=pp[2**len(data)-1:]
    f()
    test_d = pd.DataFrame(pp)
    test_d= test_d.fillna(0)
    test_d['w_sum']=test_d.sum(axis=1,skipna=True)
    test_d.drop(test_d[test_d["w_sum"]<500].index,inplace=True) 
    test_d.drop(test_d[test_d["w_sum"]>700].index,inplace=True)
    yz = list(test_d['w_sum'])
    temp = max(yz)
    ill=test_d.index[test_d['w_sum'] == temp].tolist()
    p=0
    test_d= test_d.drop([test_i.index[ill]])
#     indexc(ill)
#     print(ill)
#     print("DONE")
    return ill

def indexc(ill):
    p=1
    while p==1:   
        ipp=comb(target,data_i)
        lp=ipp[:2**len(data)-1]
        test_i=pd.DataFrame(lp)
        test_i=test_i.fillna(-1)
        test_i['w_sum']=pd.DataFrame(ds)
        test_i.drop(test_i[test_i["w_sum"]<500].index,inplace=True) 
        test_i.drop(test_i[test_i["w_sum"]>700].index,inplace=True)
        yz = list(test_i['w_sum'])
        temp1 = max(yz)
        ill=test_i.index[test_i['w_sum'] == temp1].tolist()
        test_i.drop(test_i[test_i["w_sum"]<500].index,inplace=True) 
# Delete row at index position 0 & 1
        print(lp[ill])
        test_i= test_i.drop([test_i.index[ill]])
        if(test_i.empty==True):
            p=0
        check(p,ill)
            
            
    
def check():
    data_frame = pd.read_csv("raw_final.csv")
    print(data_frame)


check()

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            test_i
        }

        resp.media = quote


api = falcon.API()
api.add_route('/', QuoteResource())
