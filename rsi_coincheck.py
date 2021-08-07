import pandas as pd
import requests
import json
import time
 
# ---Parameter---
# インターバル区間(何秒周期で値段を取得するか？)
INTERVAL_SEC = 10
# 取引するBitcoinの量
BITCOIN_SIZE = 0.005
# RSIの期間(学習中)
RSI_DURATION = 14
# APIのキー
API_KEY = 0
API_SECRET = 0
# CoinCheckへのリクエストを送信する際のURL
URL = 'https://coincheck.com/api/rate/'
# ---Parameter---

# ---固定値---
# コインの種別。前者は分かりやすくタグ付け、後者はURL時に添付するもの。
COINS = {'BTC': 'btc_jpy', 'ETH': 'eth_jpy', 'XEM': 'xem_jpy', 'BCH': 'bch_jpy'}
# ---固定値---

def virtualCoin_value_get( coin_type ):
	"""
	仮想通貨コインの現在価格を取得する。	
	Parameters
	----------
	coin_type : String
		仮想通貨コインの種別。COINSの変数を参照。

	Returns
	-------
	coincheck['rate']: int
		現在の仮想通貨コインの現在価格
	"""

	# 指定されたパラメータに沿った仮想通貨をGETしにいく。
	coincheck = requests.get(URL+COINS[coin_type]).json()
	print("%-4s : %-10s" % (coin_type, coincheck['rate']))
	return coincheck['rate']

while True:
	# Step1.仮想通貨の現在情報を取得する。
	virtualCoin_value_get( "BTC" )

	# パラメータで指定した分だけWaitする
	time.sleep( INTERVAL_SEC )

# クライテリア
# Step1.BTCの値段を取得して、printで表示
# Step2.BTCの値段と、RSIを表示
# Step3.BTCの値段から、RSIを用い、買い売りの判定を行う
# Step4.RSIによる自動取引成功
