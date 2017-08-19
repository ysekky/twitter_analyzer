import numpy as np
from gettweets import gettweets
from textanalysis import PNAnalyzer

# ツイート取得のための変数
# 2017年度隅田川花火大会の三日前9:00amから大会翌朝9:00までのtweetを取得するパラメタ
since = '2017-07-27'
until = '2017-07-30'
q = '#隅田川花火大会 OR 隅田川花火大会 OR (隅田川 AND 花火) OR (隅田川 AND 花火大会)'
fname = '7_27to7_30.csv'
pn_dict_pass = './pn_table.csv'

if __name__ == '__main___':
    df_tweets = gettweets(since, until, q, fname)
  
    mean_list = []
    analyzer = PNAnalyzer(pn_dict_pass)
    for tweet in df_tweets['text']:
        pnmean = analyzer.get_pn_mean(tweet)
        mean_list.append(pnmean)
    mean_list = np.array(mean_list)
    mean = mean_list.mean()
    print('average PN value since ' + since + ' to ' + until + ' is: ' + str(mean))
  
  
