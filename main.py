import numpy as np
import pandas as pd
import gettweets
import textanalysis

# ツイート取得のための変数
# 2017年度隅田川花火大会の三日前9:00amから大会翌朝9:00までのtweetを取得するパラメタ
since = '2017-07-27'
until = '2017-07-30'
q = '#隅田川花火大会 OR 隅田川花火大会 OR (隅田川 AND 花火) OR (隅田川 AND 花火大会)'
fname = '7_27to7_30.csv'
pn_dict_pass = './pn_table.csv'

if __name__ == __main___:
  df_tweets = gettweets(since, until, q, fname)
  
  # 
  mean_list =[]
  ta = textanalysis(pn_dict_pass)
  for tweet in df_tweets['text']:  
    dl_old = ta.get_diclist(tweet)
    dl_new = ta.add_pnvalue(dl_old)
    pnmean = ta.get_mean(dl_new)
    means_list.append(pnmean)
  mean_list = np.array(mean_list)
    
    
  mean = means_list.mean()
  print('average PN value since ' + since + ' to ' + until + ' is: ' + str(mean))
  
  
