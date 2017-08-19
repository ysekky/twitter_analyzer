import pandas as pd
import numpy as np
import re
import MeCab


class PNAnalyzer:

    # 初期化．辞書のデータフレームを作成．引数はパス
    def __init__(self, pn_dict_path):
        self.pn_dict = self._create_pn_dict(pn_dict_path)

        # MeCabインスタンスの作成．引数を無指定にするとIPA辞書になります．
        self.m = MeCab.Tagger('')

    def _create_pn_dict(self, pn_dict_path):
        pn_df = pd.read_csv(pn_dict_path, sep=':', encoding='utf-8',
                            names=('Word', 'Reading', 'POS', 'PN'))
        word_list = list(pn_df['Word'])
        pn_list = list(pn_df['PN'])
        return dict(zip(word_list, pn_list))

    def get_pnvalue_list(self, text):
        parsed = self.m.parse(text)      # 形態素解析結果（改行を含む文字列として得られる）
        lines = parsed.split('\n')  # 解析結果を1行（1語）ごとに分けてリストにする
        lines = lines[0:-2]         # MeCabの返す後ろ2行は不要なので削除
        pn_value_list = []

        for word in lines:
            l = re.split('\t|,', word)  # 各行はタブとカンマで区切られてるので
            base = l[7]
            if base not in self.pn_dict:
                continue
            pn_value_list.append(float(self.pn_dict[base]))

        return pn_value_list

    def get_pn_mean(self, text):
        pn_value_list = self.get_pnvalue_list(text)
        return np.mean(pn_value_list)
