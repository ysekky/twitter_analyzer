import pandas as pd
import got3

def gettweets(since, until, q, fname):
  tweetCriteria = got3.manager.TweetCriteria().setSince(since).setUntil(until).setQuerySearch(q)
  tweets = got3.manager.TweetManager.getTweets(tweetCriteria)

  # 取得したtweetを指定した名前のファイルに保存
  f = open(fname, 'w')
  for tweet in tweets:
    tweet_list = [str(tweet.text.replace(',','')), str(tweet.date)]
    f.write(','.join(tweet_list) + '\n')
  f.close()

  # csvファイルからDataFrameに読み込み，時系列順にソート
  df_tweets = pd.read_csv(fname, names=['text', 'date'], index_col='date')
  df_tweets.index = pd.to_datetime(df_tweets.index)
  df_tweets = df_tweets[['text']].sort_index(ascending=True)
  
  return df_tweets
