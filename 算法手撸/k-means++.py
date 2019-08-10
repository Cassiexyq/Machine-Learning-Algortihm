# -*- coding: utf-8 -*-

# @Author: xyq

import numpy as np
import random

float_max = 1e100
# class Point:
#     def __init__(self,x=0.0,y=0.0,group=0):
#         self.x = x
#         self.y = y
#         self.group = group

def distance(vecA, vecB):
    # dist = (vecA.x-vecB.x)**2 +  (vecA.y -vecB.y)**2
    dist = (vecA - vecB) * (vecA-vecB).T
    return dist[0,0]

def nearest(point, cluster_centers):
    min_dist = float_max
    m = np.shape(cluster_centers)[0]  # 当前 已经初始化的聚类中心的个数
    for i in range(m):
        d = distance(point, cluster_centers[i:])
        if min_dist > d:
            min_dist = d
    return min_dist

def get_cetroids(point, k):
    m,n = np.shape(point)
    cluster_centers = np.mat(np.zeros((k,n)))
    idx = np.random.randint(0,m)
    cluster_centers[0,] = np.copy(point[idx])
    d = [0.0 for _ in range(m)]
    for i in range(1,k):
        sum_all = 0
        for j in range(m):
            d[j] = nearest(point[j], cluster_centers[0:i,])  # 第j个数据点  Point 到各个中心点距离的最小值
            sum_all += d[i]
        sum_all *= random.random()

        for j, di in enumerate(d):  # 获得距离最远的样本点作为聚类中心点
            sum_all -= di
            if sum_all > 0:
                continue
            cluster_centers[i] = np.copy(point[j])
    return cluster_centers


def kemans(data, k, centroids):
    m,n = np.shape(data)
    subCenter = np.mat(np.zeros((m,2)))  # 记录每个样本的所属聚类以及距离
    change = True  # 判断是否需要重新计算聚类中心点
    while change:
        change = False
        for i in range(m):
            minDist = np.inf
            min_idx = 0  # 所属的类别
            for j in range(k): # 计算i和每个聚类之间的距离，给最近的那聚类
                dist = distance(data[i], centroids[j])
                if dist < minDist:
                    minDist = dist
                    min_idx = j
            if subCenter[i,0] != min_idx:
                change = True
                subCenter[i] = np.mat([min_idx,minDist])
        for j in range(k):  # 重新计算聚类中心，把每个聚类的点都加起来求平均点,每个聚类点 都要遍历一遍 subcenter
            sum_all = np.mat(np.zeros((1,n)))
            r = 0
            for i in range(m):
                if subCenter[i,0] == j:
                    sum_all += data[i]
                    r += 1  # 总共有多少点属于这个聚类点
            for z in range(n):
                try:
                    centroids[j,z] = sum_all[0,z] / r
                except:
                    print(' r is zero')
    return subCenter








