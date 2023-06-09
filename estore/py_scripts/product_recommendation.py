# -*- coding: utf-8 -*-
"""product-recommendation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ek5B6IGqELO5hM8yVQZlE3U8dIf43oxT

## Introduction
"""

pip install scikit-surprise

"""## Importing Libraries"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from surprise import SVD, Reader, Dataset , KNNBasic
from surprise.model_selection import cross_validate

"""## Loading Datasets"""

column_names=['userId','productId','rating','timestamp']
df=pd.read_csv('/content/ratings_Electronics (1).csv',names=column_names)

df.head()

df.shape

df.info()

df.isnull().sum()

"""We can see that there is no missing data and the data is clean.

## Exploratory Data Analysis

First we analyze the number of recorded ratings.
"""

df_rating=pd.DataFrame({'Number of Rating':df.groupby('productId').count()['rating'], 'Mean Rating':df.groupby('productId').mean()['rating']})

df_rating.head()



"""## Recommender Systems

### Popularity-Based Recommender

Based on the df_rating dataframe created above, we already have v or the Number of Rating, and R or Mean Rating for each product. So we calculate C.
"""

df_rating['Mean Rating'].mean()

"""The mean rating for all the products (C) is approximately 3.9 on a scale of 5.

The next step is to determine an appropriate value for m, the minimum number of votes required for a product to be listed in the chart. We use 90th percentile as our cutoff. In other words, for a product to feature in the charts, the number of its votes should be higher than that of 90% of the products in the list.
"""

df_rating['Number of Rating'].quantile(q=0.9)

"""Now, we filter the products that qualify for the chart and put them in a new dataframe called df_filtered."""

df_filtered=df_rating[df_rating['Number of Rating']>df_rating['Number of Rating'].quantile(q=0.9)]

df_filtered.shape

"""We see that there are 46553 products which qualify to be in this list.

Now, we calculate score for each qualified product. To do this, we define a function, weighted_rating(), and apply this function to the DataFrame of qualified products.
"""

def product_score(x):
    v=x['Number of Rating']
    m=df_rating['Number of Rating'].quantile(q=0.9)
    R=x['Mean Rating']
    C=df_rating['Mean Rating'].mean()
    return ((R*v)/(v+m))+((C*m)/(v+m))

df_filtered['score']=df_filtered.apply(product_score, axis=1)

df_filtered.head()

"""Finally, we sort the dataframe based on the score feature, and we output the the top 10 popular products."""

df_highscore=df_filtered.sort_values(by='score', ascending=False).head(10)

df_highscore

df_highscore.index

"""### Collaborative Recommender

#### SVD: Matrix Factorization Based Algorithm

Here we will use the famous SVD algorithm.
"""

svd = SVD()

reader = Reader()

"""Now we load the df dataset."""

data = Dataset.load_from_df(df[['userId', 'productId', 'rating']], reader)

"""Then we run 5-fold cross-validation and print the results."""

cross_validate(svd, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

"""We get a mean Root Mean Sqaure Error of 1.29 approx which is good enough for our case. Let us now train on our dataset and arrive at predictions."""

trainset = data.build_full_trainset()

"""We train the algorithm on the trainset."""

svd.fit(trainset)

df[df['userId'] == 'AKM1MP6P0OYPR']



"""As an example, we use the algorithm to predict the score that might be given to the productId of '0970407998' by this specific userId."""

decoy = ('A17HMM1M7T9PJ1','0970407998')
svd.predict(decoy)

svd.predict(uid='A17HMM1M7T9PJ1', iid='0970407998', r_ui=None).est

"""Our model predicts that userId of 'A17HMM1M7T9PJ1' will give 3.89 as the rating for productId of '0970407998'."""

import pickle

filename = "fed_model.sav"
pickle.dump(svd,open(filename,"wb"))





