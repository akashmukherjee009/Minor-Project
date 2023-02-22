import pandas as pd
import numpy as np
import pickle


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# In[146]:


data= pd.read_csv('D:/Minor Project/framework.csv')
data['Web_Based_Framework'].unique()
data['Javascript'].unique()

data['Javascript']= data['Javascript'].map(lambda x: 0 if x==False else 1)

data['Python']= data['Python'].map(lambda x: 0 if x==False else 1)

data['OOP']= data['OOP'].map(lambda x: 0 if x==False else 1)
data['C_programming']= data['C_programming'].map(lambda x: 0 if x==False else 1)
data['Front_end']= data['Front_end'].map(lambda x: 0 if x==False else 1)
data['DB']= data['DB'].map(lambda x: 0 if x==False else 1)
data['Eligibilty'].unique()
eli= {'Graduate':0, 'PostGraduate':1, 'Any':2, 'Graduation Not Required':3}


# In[124]:
print("Hello World")

data['Eligibilty']= data['Eligibilty'].map(lambda x: eli[x])


# In[125]:


data['Location'].unique()


# In[126]:


loc= {'Bangalore':0, 'Ahmedabad':1, 'Kochi':2, 'Noida':3, 'Chennai':4, 'Pune':5,
       'Hyderabad':6, 'Gurugram':7,'Kolkata':8, 'Mumbai':9,
       'Gurgaon':10,'Delhi':12, 'Mysore':13, 'Indore':14,'Chandigarh':15,'Coimbatore':16, 
      'Bhubaneswar':17, 'Thiruvananthapuram':18, 'Nagpur':19,
        'Lucknow':20, 'Coimatore':21,
       'Amritsar':22, 'Zirakpur':23,'India':24,'None of these:':25}


# In[127]:


data['Location']= data['Location'].map(lambda x: loc[x])


# In[128]:


x= data.iloc[:,2:11]
y=data.iloc[:,0]
#import numpy as np
log= LogisticRegression(random_state=0,solver='lbfgs', max_iter=1000)
log.fit(x,y)





#lin= LinearRegression()


# In[133]:



# Make pickle file of our model
pickle.dump(log, open("model.pkl", "wb"))

