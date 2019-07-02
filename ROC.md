ROC曲线的画图

AUC 线下面积的计算下面两者均可

roc_auc_score = roc_curve + auc

```python
y_score = clf.decision_function(X_test) #这个获得是置信值,confidence value
fpr,tpr,threshold = roc_curve(y_test,y_score)
roc_auc = auc(fpr,tpr)

from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_test, y_score)
```

y_score 可以传入的值：

Target scores, can either be probability estimates of the positive class, confidence values, or non-thresholded measure of decisions (as returned by “decision_function” on some classifiers).

