#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix

def model():
    training =pd.read_excel('Model/Training.xlsx')
    training.drop(columns =['year'], inplace = True)


    # In[2]:


    from sklearn.linear_model import LogisticRegression
    y=training ['Promotion']
    X=training 
    X.drop(columns =['Promotion'], inplace = True)
    clf = LogisticRegression(random_state=0, max_iter=60000).fit(X, y)


    # In[9]:


    
    r=[]
    z=clf.intercept_ 

    for x in X.columns.values:
        if x not in r:
            r.append(x)
    print(r)
    Model= pd.DataFrame(clf.coef_,columns=[r])
    Model["Interception"]=z
    Model
    Model.to_excel('Model/Coeficients.xlsx' )


    # In[8]:


    test =pd.read_excel('Model/Testing.xlsx')
    test.drop(columns =['year','Unnamed: 0'], inplace = True)

    y1=test['Promotion']
    X1=test
    X1.drop(columns =['Promotion'], inplace = True)

    r1=list(X.columns.values)
    r2=list(X1.columns.values)
    r=list(set(r) - set(r2))
    for x in r:
        X1[x]=0


    # In[29]:

    X1=X1.reindex(columns=r1) 
    for x in r1:
        X1[x].fillna(0,inplace=True)

    Test=clf.score(X1, y1)
    Trainig=clf.score(X, y)
    E=[]
    E.append(Trainig)
    E.append(Test)
    Errors= pd.DataFrame(E,columns=["error"],index=["Training","Testing"])
    Errors.to_excel('Model/Errors.xlsx' )


    # In[30]:

    y_P=clf.predict(X) 
    f1=f1_score(y, y_P, average='macro')
    recal=recall_score(y, y_P, average='macro')
    CM=confusion_matrix(y, y_P)

    y_P=clf.predict(X1) 
    f1_t=f1_score(y1, y_P, average='macro')
    recal_t=recall_score(y1, y_P, average='macro')
    CM_T=confusion_matrix(y1, y_P)

    Va=[]
    Va.append(recal)
    Va.append(f1)
    Va.append(recal_t)
    Va.append(f1_t)

    Stats= pd.DataFrame(Va,columns=["Value"],index=["Recall", "F1" ,"Recall Test", "F1 Test"])
    Stats.to_excel('Model/Stats.xlsx' )
    
if __name__ == "__main__":
    model()

