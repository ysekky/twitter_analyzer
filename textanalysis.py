import pandas as pd
import numpy  as np
import re
import MeCab

class textanalysis:

    # 初期化．辞書のデータフレームを作成．引数はパス
    def __init__(self, pn_dict_pass):
      self.pn_df = pd.read_csv(pn_dict_pass, sep=':', encoding='utf-8', \
                                      names=('Word','Reading','POS', 'PN'))
      # 各列の分割
      self.word_list = list(self.pn_df['Word'])
      self.pn_list   = list(self.pn_df['PN'])
      self.pn_dict   = dict(zip(self.word_list, self.pn_list))

      # MeCabインスタンスの作成．引数を無指定にするとIPA辞書になります．
      self.m = MeCab.Tagger('')
    
  # テキストを形態素解析し辞書のリストを返す関数
  def get_diclist(self, text):
    parsed = self.m.parse(text)      # 形態素解析結果（改行を含む文字列として得られる）
    lines = parsed.split('\n')  # 解析結果を1行（1語）ごとに分けてリストにする
    lines = lines[0:-2]         # MeCabの返す後ろ2行は不要なので削除
    self.diclist = []
    for word in lines:
      l = re.split('\t|,',word)  # 各行はタブとカンマで区切られてるので
      d = {'Surface':l[0], 'POS1':l[1], 'POS2':l[2], 'BaseForm':l[7]}
      self.diclist.append(d)
    return self.diclist

  # 形態素解析結果の単語ごとのdictデータにPN値を追加する関数
  def add_pnvalue(self, diclist_old):
    self.diclist_new = []
    for word in diclist_old:
      base = word['BaseForm']        # 個々の辞書から基本形を取得
      if base in self.pn_dict:
        pn = float(self.pn_dict[base]) 
      else:
        pn = 'notfound'            # その語がPN Tableになかった場合
        word['PN'] = pn
        self.diclist_new.append(word)
    return self.diclist_new

  # 各ツイートのPN平均値を求める
  def get_mean(self, dictlist):
    pn_list = []
    for word in dictlist:
      pn = word['PN']
      if pn!='notfound':
        pn_list.append(pn)
    if len(pn_list)>0:
      pnmean = np.mean(pn_list)
    else:
      pnmean=0
    return pnmean
