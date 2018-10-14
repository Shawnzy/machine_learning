# -*- coding: utf-8 -*-

import numpy as np

import sklearn.model_selection as ms
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
churn = pd.read_csv('dataset.csv')
churnX = churn.drop('Churn',1).copy().values
churnY = churn['Churn'].copy().values
import pdb





churn_trgX, churn_tstX, churn_trgY, churn_tstY = ms.train_test_split(churnX, churnY, test_size=0.3, random_state=0, stratify=churnY)

pipe = Pipeline([('Scale',StandardScaler()),])
trgX = pipe.fit_transform(churn_trgX,churn_trgY)
trgY = np.atleast_2d(churn_trgY).T
tstX = pipe.transform(churn_tstX)
tstY = np.atleast_2d(churn_tstY).T
trgX, valX, trgY, valY = ms.train_test_split(trgX, trgY, test_size=0.2, random_state=1,stratify=trgY)
tst = pd.DataFrame(np.hstack((tstX,tstY)))
trg = pd.DataFrame(np.hstack((trgX,trgY)))
val = pd.DataFrame(np.hstack((valX,valY)))
print(len(val.columns))
tst.to_csv('c_test.csv',index=False,header=False)
trg.to_csv('c_trg.csv',index=False,header=False)
val.to_csv('c_val.csv',index=False,header=False)
