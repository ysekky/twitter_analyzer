# twitter_analyser
# Twitter民の感情分析ツール v1.0.0

以下のブログについて一部修正，再検討を行ったコード群です．

[Aidemy Tech Blog -花火大会におけるTwitter民の感情分析](http://blog.aidemy.net/entry/2017/08/10/170715)

## 目次

- 目次
- 目的
ｰ 環境及び使用したもの
- 概要
  - Twitterからのtweetの収集
  - tweetの形態素解析及びPos/Neg判定
- 今後の方針
- アップデート

## 目的
2017年度隅田川花火大会の日は雨が降りました．数日前から悪天候が懸念され，Twitter上では悪天候を喜ぶ声と
残念がる声の双方が見受けられました．
そのため，Twitter上の感情分析を行うためのツールを開発しようと思い立ったのが本レポジトリの発端です．

## 環境及び使用したもの
- Fedora 26
- Anaconda 4.3.2
- Python 3.6.0
- [GetOldTweets-python](https://github.com/Jefferson-Henrique/GetOldTweets-python)
  - リンク先はPython3未対応です．本レポジトリにてPython3に対応済みのものを再配布しています．
- [MeCab - 形態素解析エンジン](http://taku910.github.io/mecab/)
  - Pythonとのバインディングを済ませる必要があります．詳しくは[こちら](http://qiita.com/grachro/items/4fbc9bf8174c5abb7bdd)をご覧ください．
- [PN Table - 単語感情極性対応表](http://www.lr.pi.titech.ac.jp/~takamura/pndic_ja.html)
  - PN値とは単語の感情的な極性とその強さを表す値です．
  - こちらは，再配布不可能なためリンク先からダウンロードし，UTF-8に変換してお使い下さい．

## 概要

- Twitterからのデータ収集
- tweetの形態素解析及びPos/Neg判定

### Twitterからのtweetの収集
Twitter公式APIを用いると，tweetの取得に制限が課せられます．そのため，HTTPリクエストでtweetを取得する
[GetOldTweets-python](https://github.com/Jefferson-Henrique/GetOldTweets-python)を用いました．
`gettweets()`に収集したい期間とキーワードをわたすことで，Twitterからキーワードを含む指定期間中のtweetを
すべて取得します．取得されたtweetは指定のファイルに保存され，関数は`pandas.DataFrame`型の
tweetsを返します．tweetsは時系列順に並んだデータtweetが含まれています．

### tweetの形態素解析及びPos/Neg判定
`textanalysis`クラスはテキストを形態素解析し，テキストに含まれる各単語のPN値及びテキストの
平均PN値を求めることができます．初期化時に極性辞書へのパスを渡すことでインスタンスを生成します．
`textanalysis`クラスの持つメソッドは以下の通りです．
- `get_dictlist(text)`
  - 渡されたテキストを形態素解析し，各単語の解析結果を辞書型で持ち，これらをリストで返す．
- `add_pnvalue(diclist_old)`
  - 形態素分析されたテキスト（単語ごとに分けられた辞書型）のすべての単語に対して極性辞書から得たPN値の項を付け加えたリストを返す．
  - v1.0.0では極性辞書にない単語についてはPN値を0とする．
- `get_mean(dictlist)`
  - 単語単位のPN値ぱらテキストの平均のPN値を得てこれを返す．

## 今後の方針(2017/8/18-)
 - 時系列順の平均値の算出
 - 単語間の関連性，tweetの平均PN値と含まれる単語の因果関係（tweetの平均PN値の決め手はなにか？など）
