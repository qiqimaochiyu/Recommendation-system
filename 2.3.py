#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 19:04:17 2018

@author: macbook_wy
"""

import random

def SplitData(data, M, k, seed):
    # 将数据集随机分成训练和测试集
    test = []
    train = []
    random.seed(seed)
    for user, item in data:
        if random.randint(0, M) == k:
            test.append([user, item])
        else:
            train.append([user, item])
    return train, test
    

def Recall(train, test, N):
    # 召回率
    hit = 0
    n_all = 0
    for user in train.keys():
        tu = test[user]
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            if item in tu:
                hit += 1
        n_all += len(tu)
    return hit / (n_all * 1.0)

def Precision(train, test, N):
    # 准确率
    hit = 0
    n_all = 0
    for user in train.keys():
        tu = test[user]
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            if item in tu:
                hit += 1
        n_all += N
    return hit / (n_all * 1.0)


def Coverage(train, test, N):
    recommend_items = set()
    all_items = set()
    for user in train.keys():
        for item in train[user].keys():
            all_items.add(item)
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            recommend_items.add(item)
    return len(recommend_items) / (len(all_items) * 1.0)
