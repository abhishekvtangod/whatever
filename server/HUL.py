# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%%
from IPython import get_ipython


#%%
import pandas as pd
import numpy as np
import math
from pyxlsb import open_workbook as open_xlsb

get_ipython().run_line_magic('matplotlib', 'inline')


#%%
import pandas as pd
from pyxlsb import open_workbook as open_xlsb

df = []

with open_xlsb('Shogun Report Nov 2018.xlsb') as wb:
    with wb.get_sheet(1) as sheet:
        for row in sheet.rows():
            df.append([item.v for item in row])

df = pd.DataFrame(df[1:], columns=df[0])


#%%
df=df.drop(['SEQUENCE','Sr. No.','NET_SALES_QTY','NET_SALES_Cases.Units','UPC','NET_SALES_VALUE','SCHEME_DISCOUNT','OTHER_DISCOUNT','TAX_PERCENTAGE','Net Value Calculation','MRP','TUR','PARTY_CODE','BASEPACK CODE','SKU7_CODE','PRODUCT_NAME',],axis=1)
df.head()


#%%
import pandas as pd
from pyxlsb import open_workbook as open_xlsb

df1 = []

with open_xlsb('GPS Location Data.xlsb') as wb:
    with wb.get_sheet(1) as sheet:
        for row in sheet.rows():
            df1.append([item.v for item in row])

df1 = pd.DataFrame(df1[1:], columns=df1[0])


#%%
df1


#%%
fin=pd.merge(df, df1, on=['PARTY_HLL_CODE'])


#%%
fin


