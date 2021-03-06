# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys;
sys.path.append("allinpay projects")
from imp import reload
import creditscorekeras.classkeras
#reload(creditscorekeras.classkeras)

##############################################################################
##############################################################################
#一，初始化模型数据
##############################################################################
##############################################################################
dataname = 'HMEQ'
#dataname = 'german'
#dataname = 'taiwancredit'
kerasmodel = creditscorekeras.classkeras.CreditScoreKeras(dataname)
self = kerasmodel

##############################################################################
##############################################################################
#二，设置模型参数
##############################################################################
##############################################################################
#1,粗分类和woe转换设置
#粗分类时聚类的数量
nclusters=10
#粗分类时聚类的方法,kmeans,DBSCAN,Birch，quantile(等分位数划分)，None(等距划分)
#cmethod = 'equal'
cmethod = 'quantile'
#cmethod = 'kmeans'
#cmethod = 'Birch'
#method = 'DBSCAN'
#2，训练集和测试集的划分
testsize = 0.3
nsplit = 5
#3，变量筛选设置
feature_sel = 'origin'
#feature_sel = "VarianceThreshold"
#feature_sel = "RFECV"
#feature_sel == "SelectFromModel"
#feature_sel == "SelectKBest"
cv = 10
varthreshold = 0.2
#4，Keras算法设置
batches = 100
nepoch = 10



##############################################################################
##############################################################################
#三，建模并预测
##############################################################################
##############################################################################
#1，不筛选变量的完整模型
#单次的train and test
predresult = self.keras_dnn_trainandtest(testsize, cv, feature_sel, varthreshold, nepoch, batches, nclusters, cmethod)
#K重train and test
predresult = self.keras_dnn_trainandtest_kfold(nsplit, cv, feature_sel, varthreshold, nepoch, batches, nclusters, cmethod)

##############################################################################
##############################################################################
#四，模型预测结果评估
##############################################################################
##############################################################################
self.modelmetrics_scores(predresult)




