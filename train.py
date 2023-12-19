

# ### 1. Load packages and data


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.formula.api as smf
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics
from sklearn.feature_extraction import DictVectorizer
import re
import pickle
import xgboost
import wget

### 1. Parameters


xgb_params = {
    'eta': 0.1, 
    'max_depth': 6,
    'objective': 'reg:squarederror',
    'eval_metric': 'rmse',
    'seed': 45365745,
}



ouput_file='m_xgb_rg.bin'


####  Data

data= "https://raw.githubusercontent.com/ColombiaMRP/Capstone-project-1/main/Data/kc_house_data.csv"
data= wget.download(data)
df= pd.read_csv(data)

#### Defining relevant variables

features = ['bedrooms', 'bathrooms', 'floors', 'waterfront', 'view', 'condition', 'grade', 'yr_built','lat', 'long', 'sqft_living','sqft_lot', 'sqft_above', 'sqft_basement','sqft_living15', 'sqft_lot15']
X = df[features]
Y = np.log(df['price_boxcox'])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#### dict-vectorizer

dv = DictVectorizer(sparse=False)

train_dicts = X_train[features].to_dict(orient='records')
X_train_dv = dv.fit_transform(train_dicts)

test_dicts = X_test[features].to_dict(orient='records')
X_test_dv = dv.transform(test_dicts)

### Gradient boosting


features = dv.get_feature_names_out()
features = [re.sub(r'[\[\]<>]', '', feature) for feature in features]

dtrain = xgboost.DMatrix(X_train_dv, label=Y_train, feature_names=features)
dtest=xgboost.DMatrix(X_test_dv, label=Y_test, feature_names=features)

model_final=xgboost.train(xgb_params, dtrain, num_boost_round=175)


### Save Model

with open(ouput_file,'wb') as f_out:
    pickle.dump((dv,model_final),f_out)
