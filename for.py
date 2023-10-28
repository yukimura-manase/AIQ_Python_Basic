

my_animals = ["ロボ玉", "まり玉", "ピウイ", "白桃さん", "ももちゃん"]

# 通常の for文
for animal in my_animals:
    print(animal)

# range関数で、設定した数の数値を繰り返し出力する(注意: 0 始まり)
for num in range(3):
    print(num)

# for 文で indexを取得する場合
for index in range(len(my_animals)):
    animal = my_animals[index]
    print(index, animal)


# タプルは、valueのUpdateが不可能なリスト => つまり、定数・List
robotama_tuple = ("ロボ玉", '東京', 2000)


# タプルの要素を順番に取り出す
for robo in robotama_tuple:
    print(robo)


## 辞書（dict）の要素をforループで取り出す方法:
robotama_dict = {"robotama": 'ロボ玉', 'from': '東京', 'hamflag': True, 'power': 2000, }

# key & value 両方、取り出す
for key, value in robotama_dict.items():
    print(key, value)

# key のみを取り出す
for key in robotama_dict:
    print(key)

# value のみを取り出す
for value in robotama_dict.values():
    print(value)
