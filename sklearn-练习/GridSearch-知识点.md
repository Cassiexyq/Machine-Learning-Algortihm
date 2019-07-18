#### GridSearch 

* 里面的cv是怎样操作的

* 所有参数是怎么排列组合的，有嵌套的话

  > cv_results_:  字典  cv=5
  >
  > ```python
  > dict_keys(['mean_fit_time', 'std_fit_time', 'mean_score_time', 'std_score_time', 'param_C', 'param_gamma', 'param_kernel', 'params', 'split0_test_score', 'split1_test_score', 'split2_test_score', 'split3_test_score', 'split4_test_score', 'mean_test_score', 'std_test_score', 'rank_test_score', 'split0_train_score', 'split1_train_score', 'split2_train_score', 'split3_train_score', 'split4_train_score', 'mean_train_score', 'std_train_score'])
  > ```
  >
  > ```
  > {
  > 'param_kernel': masked_array(data = ['poly', 'poly', 'rbf', 'rbf'],
  >                              mask = [False False False False]...)
  > 'param_gamma': masked_array(data = [-- -- 0.1 0.2],
  >                             mask = [ True  True False False]...),
  > 'param_degree': masked_array(data = [2.0 3.0 -- --],
  >                              mask = [False False  True  True]...),
  > 'split0_test_score'  : [0.80, 0.70, 0.80, 0.93],
  > 'split1_test_score'  : [0.82, 0.50, 0.70, 0.78],
  > 'mean_test_score'    : [0.81, 0.60, 0.75, 0.85],
  > 'std_test_score'     : [0.01, 0.10, 0.05, 0.08],
  > 'rank_test_score'    : [2, 4, 3, 1],
  > 'split0_train_score' : [0.80, 0.92, 0.70, 0.93],
  > 'split1_train_score' : [0.82, 0.55, 0.70, 0.87],
  > 'mean_train_score'   : [0.81, 0.74, 0.70, 0.90],
  > 'std_train_score'    : [0.01, 0.19, 0.00, 0.03],
  > 'mean_fit_time'      : [0.73, 0.63, 0.43, 0.49],
  > 'std_fit_time'       : [0.01, 0.02, 0.01, 0.01],
  > 'mean_score_time'    : [0.01, 0.06, 0.04, 0.04],
  > 'std_score_time'     : [0.00, 0.00, 0.00, 0.01],
  > 'params'             : [{'kernel': 'poly', 'degree': 2}, ...],
  > }
  > ```
  >
  > mean_test_score =  split0_test_score + split1_test_score
  >
  > mean_train_score = split0_train_score + split1_train_score
  >
  > 每个split-数字的数组表示cv = 数字时候每种参数选择的训练/测试结果
  >
  > 也就是说每种参数的组合方式都要经过cv次运行得到最终的mean_score
  >
  > 如果多个满足的话会按顺序选择最前面那个，
  >
  > 有一个rank_test_score排名，params有所有的排列组合形式

