#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing pandas module  
import pandas as pd 
import numpy as np
# reading csv file from url  
data =pd.read_excel (r'C:\Python37\Scripts\dealmoon-data.xlsx')

# Find free shipping and exclusions
data["Free Shipping"] = data["information"].str.contains(pat = 'Free shipping', regex = True) 
data["Exclusions Apply"] = data["information"].str.contains(pat = 'Exclusions Apply', regex = True) 

  
# new data frame with split value columns  by imformation looking for minimun
new = data["information"].str.split(r"Free shipping on | Exclusions", n = 2, expand = True) 
  
# making separate last name column from new data frame 
data["Conditions Free Shipping"]= new[1] 

# new data frame with split value columns 
new = data["Conditions Free Shipping"].str.split(r".", n = 2, expand = True) 
  
# making separate last name column from new data frame 
data["Conditions Free Shipping"]= new[0] 


# new data frame with split value columns 
new = data["Conditions Free Shipping"].str.split( n = 4, expand = True) 
  
# making separate last name column from new data frame 
data["Minimum Free Shipping"]= new[2] 
data.drop(columns =["Conditions Free Shipping"], inplace = True) 
new = data["Minimum Free Shipping"].str.split(r",|\(|expires|orders|\+|code|Fisher-Price|free|shipping|over|with|of|not|Deal|coupon|via|or|Mesh|get", n = 1, expand = True) 
  
# making separate last name column from new data frame 
data["Minimum Free Shipping"]= new[0] 

new=data["Minimum Free Shipping"].replace("2", "$2 items")
data["Minimum Free Shipping"]= new

new = data["Minimum Free Shipping"].str.split('，',n = 1, expand = True) 

# making separate last name column from new data frame 
data["Minimum Free Shipping"]= new[0] 

new = data["Minimum Free Shipping"].str.split("$",n = 1, expand = True) 
data["Minimum Free Shipping"]= new[1] 

data["Minimum Free Shipping"].fillna(value=pd.np.nan, inplace=True)
data["Minimum Free Shipping"].fillna("0", inplace = True)
data.loc[data['Free Shipping'] ==False, ['Minimum Free Shipping']] = 'N/A'


# In[3]:


# new data frame with split value columns 

new = data["information"].str.split(r"code", n = 1, expand = True) 

# making separate last name column from new data frame 
data["code"]= new[1] 
data.dropna(inplace = False) 
new = data["code"].str.split(r"\n \n \"", n = 1, expand = True) 
  
# making separate first name column from new data frame 
data["code1"]= new[0] 
new = data["code1"].str.split(r"\"\n \n" , n = 1, expand = True) 
  
# making separate first name column from new data frame 
data["code"]= new[1] 
data.drop(columns =["code1"], inplace = True)  


# In[4]:


data["retailer"]=data["retailer"].str.lower()
data["Clothing"] = data["retailer"].str.contains(pat = r'calvin-klein|adid|hm|lowes|express|gap|hollister|j crew|levis|nike|uniqlo|zara', regex = True) 
data["Superstore"] = data["retailer"].str.contains(pat = r"Target|walmart", regex = True) 
data["Wholesale"] = data["retailer"].str.contains(pat = r"costco|sams club", regex = True) 
data["Department Store"] = data["retailer"].str.contains(pat = r"bloomingdales|macys|neiman marcus|nordstrom", regex = True) 
data["Beauty"] = data["retailer"].str.contains(pat = r"sephora", regex = True) 
data["Electronic"] = data["retailer"].str.contains(pat = r"bestbuy", regex = True) 

data = pd.melt(data, id_vars=list(data.columns)[:7], value_vars=list(data.columns)[7:],
             var_name='Retailer Style', value_name='Dummy')
data=data[data.Dummy==True]

data.drop(columns=["Dummy"], inplace = True)


# In[5]:


data["information"]=data["information"].str.lower()
data["Bottoms"] = data["information"].str.contains(pat = r'jeans|pants|joggers|leggings|short|skirt|sweatpants', regex = True) 
data["Tops"] = data["information"].str.contains(pat = r'polos|shirts|t-shirts|sweaters|blouses|tanks|hoodies|sweatshirts|tees|bodysuits|tops', regex = True) 
data["Shoes"] = data["information"].str.contains(pat = r'sneakers|sandals|shoes|high heels|boots|heels|flats|slippers|loafer|flip flops', regex = True) 
data["Outerwear"] = data["information"].str.contains(pat = r'jackets|coat|outerwear', regex = True) 
data["Underwear"] = data["information"].str.contains(pat = r'bras|uderwear|panties|panty|socks|boxer', regex = True) 
data["Dresses"] = data["information"].str.contains(pat = r'dress', regex = True) 
data["Acessories"] = data["information"].str.contains(pat = r'bracelet|acessor|bags|hat|belt|watch|handbag|wallet|scar|sunglass|jewelry|neck|earing|ring', regex = True) 
data["Acessories"].value_counts()
data["TV"] = data["information"].str.contains(pat = r'tv', regex = True) 
data["Computers"] = data["information"].str.contains(pat = r'computer|laptop|monitor|deskto|ram|cpu|usb|tablet', regex = True) 
data["Headphones and Speakers"] = data["information"].str.contains(pat = r'headphones|earbuds|earpods|speaker', regex = True) 
data["Makeup"] = data["information"].str.contains(pat = r'sephora|makeup|palette', regex = True) 
data["Eyes Makeup"] = data["information"].str.contains(pat = r'eye|eye|mascara|Masca', regex = True) 
data["Skin Makeup"] = data["information"].str.contains(pat = r'blushs|bronzer|foundation|Foundation|Blus|Bronz|Primer|primer', regex = True) 
data["Lips"] = data["information"].str.contains(pat = r'Lips|lip|Balm|balm', regex = True) 
data["Skin Care"] = data["information"].str.contains(pat = r'moisturizer|Moisturizer|Skin Care|skin care|toner|Skin', regex = True) 
data["Sitewide"] = data["information"].str.contains(pat = r'sitewide|entire site|entire store|purchase', regex = True) 


# In[6]:


data = pd.melt(data, id_vars=list(data.columns)[:8], value_vars=list(data.columns)[8:24],
             var_name='Product', value_name='Dummy')
data=data[data.Dummy==True]
data.drop(columns=["Dummy"], inplace = True)


# In[7]:


data["Week"]=data['day'].dt.week
data["year"]=data['day'].dt.year
data["promotion"]=True


# In[8]:


output=[]          
for x in data["retailer"] :
     if x not in output:
        output.append(x)

P=[]
for x in data["Product"] :
     if x not in P:
        P.append(x)

for x in output:
    data1=data[data.retailer==x]
    start=data1['day'].min()
    end=data1['day'].max()
    df = pd.DataFrame({"Date": pd.date_range(start, end)})
    df["Week"] = df.Date.dt.weekofyear.astype(int)
    df["year"] = df.Date.dt.year.astype(int)
    df["Control"]=df["Week"]+df["year"]*100
    J=[]
    for z in data1["Retailer Style"]:
            J=z
    for y in P:
        data2=data1[data.Product==y]
        result = pd.merge(left=df, right=data2, how='left', left_on=['year','Week'], right_on=['year','Week'])
        result.drop_duplicates('Control',keep='first',inplace=True)
        result.drop(columns =["Control","Date"], inplace = True)
        result["Product"]=y
        result["retailer"]=x
        result["Retailer Style"]=J
        result.to_excel( x+y+'.xlsx' )


# In[9]:


for x in output:
    dh =pd.read_excel(x+P[0]+'.xlsx')
    for y in P[2:16]:
        data =pd.read_excel(x+y+'.xlsx')
        dh=dh.append(data, ignore_index=True)
    dh["code"].fillna(" ", inplace = True) 
    dh["Free Shipping"].fillna(0, inplace = True) 
    dh["Minimum Free Shipping"].fillna(0, inplace = True) 
    dh["promotion"].fillna(0, inplace = True) 
    dh.drop(columns =["Unnamed: 0"], inplace = True)
    dh.to_excel( x+'_Data.xlsx' )


# In[10]:


import numpy as np
data =pd.read_excel(output[0]+'_Data.xlsx')
data.sort_values(['year', 'Week'], ascending=[False, False])
Training , Testing = np.split(data, [int(.75*len(data))])
for x in output[1:len(output)]:
    data=pd.read_excel(x+'_Data.xlsx') 
    data.sort_values(['year', 'Week'], ascending=[False, False])
    Training2 , Testing2 = np.split(data, [int(.75*len(data))])
    Testing=Testing.append(Testing2, ignore_index=True)
    Training=Training.append(Training2, ignore_index=True)
    


# In[11]:


Training.drop(columns =["information","day","Unnamed: 0"], inplace = True) 
Testing.drop(columns =["information","day","Unnamed: 0"], inplace = True) 
Training.to_excel('Training_complete.xlsx' )
Testing.to_excel('Testing_complete.xlsx' )
Training.drop(columns =["Exclusions Apply","Free Shipping","code","Retailer Style","Minimum Free Shipping"], inplace = True) 
Testing.drop(columns =["Exclusions Apply","Free Shipping","code","Retailer Style","Minimum Free Shipping"], inplace = True) 


# In[125]:


Training = pd.get_dummies(Training)
Testing = pd.get_dummies(Testing)
Training.to_excel('Training.xlsx' )
Testing.to_excel('Testing.xlsx' )

