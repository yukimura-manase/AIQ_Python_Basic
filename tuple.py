

# タプルは、valueのUpdateが不可能なリスト => つまり、定数・List
robotama_tuple = ("ロボ玉", '東京', 2000)
print(robotama_tuple) # ('ロボ玉', '東京', 2000)

# index で value を取得する
print(robotama_tuple[0]) # ロボ玉
print(robotama_tuple[1]) # 東京
print(robotama_tuple[2]) # 2000

## Errorパターン => value の Update操作はできない
# print(robotama_tuple[0] = 'ピウイ')

## タプルの長さ

# タプルの長さを取得
tuple_len = len(robotama_tuple)

print(tuple_len) # 3


## タプルの結合

# 2つのタプルを結合
merge_tuple = robotama_tuple + ("白桃さん", '千葉県', 8000)
print(merge_tuple) # ('ロボ玉', '東京', 2000, '白桃さん', '千葉県', 8000)


## タプルのスライス

# インデックス0からインデックス2までの要素を取得
slice_tuple = merge_tuple[0:3]

print(merge_tuple) # ('ロボ玉', '東京', 2000, '白桃さん', '千葉県', 8000)
print(slice_tuple) # ('ロボ玉', '東京', 2000)
