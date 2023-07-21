# 清一色学習アプリ

### 注意点
- Windowsで開発したためMACの動作が不安定＆UIがおかしいです(今回使用したtkinterがMACだとバグるみたいです)
- 一応起動して主要な動作はできるように修正したはずです

### 起動方法
- download zipをする
- ターミナルで
- `brew install tcl-tk`
- `brew install python-tk@3.11`を打つ
- ダウンロードしたディレクトリ(mahjong-main)で`python mahjong/main.py`を行う


### 麻雀問題設定
- 麻雀牌は7枚,10枚,13枚のみ
- 聴牌するボタンは必ず聴牌する問題がでる。しないボタンは、聴牌していない問題も出る(する問題も出る)
- 難易度は普通だと待ち牌が1,2枚、難だと3枚以上, ランダムは1枚以上となる。

### 麻雀問題解答
- 解答する際、待ち牌が3,6,9の場合
  - 369と入力欄に打つ
