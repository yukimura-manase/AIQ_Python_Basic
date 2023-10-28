
## ディクショナリの作成
robotama_dict = {"robotama": 'ロボ玉', 'from': '東京', 'hamflag': True, 'power': 2000, }

## key を使用して、value を取得する
val1 = robotama_dict["robotama"]
val2 = robotama_dict["hamflag"]

print(val1) # ロボ玉
print(val2) # True


# dict から すべての key を取得
dict_keys = robotama_dict.keys()

print(dict_keys) # dict_keys(['robotama', 'from', 'hamflag', 'power'])

## values()メソッドを使用して、ディクショナリの全ての値を取得する

# dict から　すべての vallue を取得
dict_vals = robotama_dict.values()
print(dict_vals) # dict_values(['ロボ玉', '東京', True, 2000])


## 新しい key & value の追加

robotama_dict['rival'] = '白桃さん'

print(robotama_dict)
# {'robotama': 'ロボ玉', 'from': '東京', 'hamflag': True, 'power': 2000, 'rival': '白桃さん'}


## ディクショナリの作成
robotama_dict = {"robotama": 'ロボ玉', 'from': '東京', 'hamflag': True, 'power': 2000, }

## 既存の Value の Update

robotama_dict['hamflag'] = False

print(robotama_dict)
# {'robotama': 'ロボ玉', 'from': '東京', 'hamflag': False, 'power': 2000}


## Value を削除する

## ディクショナリの作成
robotama_dict = {"robotama": 'ロボ玉', 'from': '東京', 'hamflag': True, 'power': 2000, }

# ディクショナリからエントリを削除
del(robotama_dict['power'])

print(robotama_dict)
# {'robotama': 'ロボ玉', 'from': '東京', 'hamflag': True}

## key の存在確認

## ディクショナリの作成
robotama_dict = {"robotama": 'ロボ玉', 'from': '東京', 'hamflag': True, 'power': 2000, }

# ディクショナリに特定の key が存在するかどうかを確認するには、inキーワードを使用します。
print('robotama' in robotama_dict) # True
print('speed' in robotama_dict) # False














