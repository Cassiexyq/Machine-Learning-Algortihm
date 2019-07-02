### 逻辑回归



```python
from sklearn.linear_model import LogisticRegression

#数据标准化处理： 
from sklearn.preprocessing import StandardScaler 
X_std = preprocessing.StandardScaler().fit_transform(X)

#默认用法： 
LogisticRegression(penalty=’l2’, dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver=’liblinear’, max_iter=100, multi_class=’ovr’, verbose=0, warm_start=False, n_jobs=1)
```

> penalty：选择L2一般就够了，如果L2发现过拟合，预测效果差，可以考虑L1，如果模型特征非常多，模型特征稀疏化，可以使用L1，penalty参数的选择会影响我们损失函数优化算法的选择。即参数solver的选择，如果是L2正则化，那么4种可选的算法{‘newton-cg’, ‘lbfgs’, ‘liblinear’, ‘sag’}都可以选择。但是如果penalty是L1正则化的话，就只能选择‘liblinear’了。这是因为L1正则化的损失函数不是连续可导的，而{‘newton-cg’, ‘lbfgs’,‘sag’}这三种优化算法时都需要损失函数的一阶或者二阶连续导数。而‘liblinear’并没有这个依赖。
>
> 如果选择了ovr，则4种损失函数的优化方法liblinear，newton-cg, lbfgs和sag都可以选择。但是如果选择了multinomial,则只能选择newton-cg, lbfgs和sag了。
>
> max_iter：是指最大循环次数，也就是说当loss不在减少，就不在循环了
>
> solver优化方法：
>
> （1）liblinear：使用了开源的liblinear库实现，内部使用了坐标轴下降法来迭代优化损失函数。 
> （2）lbfgs：拟牛顿法的一种，利用损失函数二阶导数矩阵即海森矩阵来迭代优化损失函数。 
> （3）newton-cg：也是牛顿法家族的一种，利用损失函数二阶导数矩阵即海森矩阵来迭代优化损失函数。 
>
> （4）sag：即随机平均梯度下降，是梯度下降法的变种，和普通梯度下降法的区别是每次迭代仅仅用一部分的样本来计算梯度，适合于样本数据多的时候，SAG是一种线性收敛算法，这个速度远比SGD快。



class_weight ='balanced'  ，类库根据训练样本来计算权重

*大量样本（6W+）、高维度（93）， --> 可选用saga优化求解器*

交叉验证 -》  LogisticRegressionCV，可传入Cs(正则化数的集合，数越小，正则化强度越大，传入整个数据集)

 **维度<10000时，lbfgs法比较好，   维度>10000时， cg法比较好，显卡计算的时候，lbfgs和cg都比seg快**

| L1   | liblinear                  | liblinear适用于小数据集,如果选择L2正则化发现还是过拟合，即预测效果差的时候，就可以考虑L1正则化；如果模型的特征非常多，希望一些不重要的特征系数归零，从而让模型系数稀疏化的话，也可以使用L1正则化 |
| ---- | -------------------------- | ------------------------------------------------------------ |
| L2   | liblinear                  | 只支持多元逻辑回归的OvR，不支持MvM，但MVM相对精确            |
| L2   | 2 lbfgs/newton-cg/sag/saga | 较大数据集，支持one-vs-rest(OvR)和many-vs-many(MvM)两种多元逻辑回归 |
| L2   | saga/sag                   | 如果样本量非常大，比如大于10万，sag是第一选择；但不能用于L1正则化 |



### 搜索参数

scoring 的选择

<https://scikit-learn.org/stable/modules/model_evaluation.html>

