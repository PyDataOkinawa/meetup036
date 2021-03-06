# OpenCVでとことん画像処理
## 前半
- 画像を扱う際の簡単な説明(10分)
	- 画像処理のよく使われる場面などの説明
	- 表色系と色空間
		- HSV空間(マンセル表色系)について
			- 6角錐モデルと双6角錐モデル
		- RGB空間
			- チャンネルごとに画像を出力する
- 画素ごとの濃淡変換(20分)
	- トーンカーブ
		- ヒストグラム平坦化
		- 折れ線トーンカーブ
		- S字トーンカーブ 
		- ガンマ変換
	- LUT(Look Up Table) による高速濃淡変換
		- ネガポジ反転
		- ポスタリゼーション(c=2 のとき2値化)
	- salt_pepperノイズ(インパルスノイズ)
- 複数画像の利用(10分)
	- アルファブレンディング
	- ディゾルブ
- バッファ(5分)

## 後半
- 空間フィルタリング(20分)
	- 平滑化
		- 平均化フィルタ
		- 加重平均化(ガウシアン)フィルタ
		- メディアンフィルタ
	- エッジ検出
		- Cannyアルゴリズムによるエッジ検出
	- 鮮鋭化(アンシャープマスキング)
	- エッジを保存した平滑化
		- バイラテラルフィルタ
		- ノンローカルミーンフィルタ
- 二値化(10分)
	- 単純なしきい値処理
		- バイナリ形式(TOZERO形式)
		- 切り捨て形式
	- 複雑なしきい値処理
		- 大津法による二値化 
- 領域処理(10分)
	- 領域分割
        - クロマキーによるマスク処理
		- ミーンシフト法
		- grabcut法
- まとめ(5分)
- バッファ(5分)
