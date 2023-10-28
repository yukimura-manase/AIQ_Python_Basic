
### Python入門講座 Vol.01 ###

### 目次 ###

# 1. 標準出力とは？
# 2. 変数とは？
# 3. データの種類と、型定義とは？
# 4. 型変換(キャスト)とは？
# 5. 数値計算をする


### 1. 標準出力とは？ ###

## 
# NOTE: 標準出力とは、プログラムの実行結果を出力すること
# => Python の場合は、printメソッドで 標準出力を実行する
## 

print('-------------------------- 標準出力 ---------------------------')

print('Hellow World') # Hellow World

### 2. 変数とは？ ### 

## 
# NOTE: 変数とは、データを入れることのできる箱のようなものです。
# => 「 変数名 = Data 」の形で、Data を変数に入れます。
## 
hello = 'Hellow World'

# 同じ変数名に、違うデータを入れると、データが Updateされます。
hello = 'Hellow AIQ'
print(hello) # Hellow AIQ

print('-----------------------------------------------------')

### 3. データの種類と、型定義 ###

## 
# NOTE: Python には str(文字列), int(整数), bool(真偽値), list(リスト), dict(辞書型) などの「データの種類」(データの型)があります。
# => typeメソッドを使用することで「データの型」(データの種類)を確認することができます。
## 

print('-------------------------- データの種類と、型定義 ---------------------------')

# 1. str型：文字列
string: str = 'ロボ玉'

print(string) # ロボ玉
print(type(string)) # <class 'str'>

# 2. int型：整数
integer: int = 12

print(integer) # 12
print(type(integer)) # <class 'int'>

# 3. float型：小数点
double: float = 12.34

print(double) # 12.34
print(type(double)) # <class 'float'>

# 4. bool型：真偽値
boolean_true: bool = True
boolean_false: bool = False

print(boolean_true) # True
print(boolean_false) # False

print(type(boolean_true)) # <class 'bool'>
print(type(boolean_false)) # <class 'bool'>

# 5. list型：リスト
array: list = ['ロボ玉試作1号機', 'ロボ玉試作2号機', 'ロボ玉試作3号機']

print(array) # ['ロボ玉試作1号機', 'ロボ玉試作2号機', 'ロボ玉試作3号機']
print(type(array)) # <class 'list'>


# 6. tuple型：タプル => 定数-List
tupleData: tuple = ('robotama', 'hakutou', 'momo')

print(tupleData) # ('robotama', 'hakutou', 'momo')
print(type(tupleData)) # <class 'tuple'>

# 7. dict型：辞書
dictionary: dict = {
    'robotama-1': 'ロボ玉試作1号機',
    'robotama-2': 'ロボ玉試作2号機',
    'robotama-3': 'ロボ玉試作3号機',
}

print(dictionary) # {'robotama-1': 'ロボ玉試作1号機', 'robotama-2': 'ロボ玉試作2号機', 'robotama-3': 'ロボ玉試作3号機'}
print(type(dictionary)) # <class 'dict'>


print('-----------------------------------------------------')

### 4. 型変換(キャスト)とは？ ###

## 
# NOTE: 型メソッドを使用することで、データの型を別のものに変換(型変換)することができます。
##

print('-------------------------- 型変換(キャスト)をする ---------------------------')

# 文字列: '12' を int型 に変換する
print(int('12'), type(int('12')))
# 12 <class 'int'>


# 文字列: '12.34' を float型(浮動小数点・型)に変換する
print(float('12.34'), type(float('12.34'))) 
# 12.34 <class 'float'>


# 整数: 30 を str型に変換する
print(str(30), type(str(30)))
# 30 <class 'str'>

# 浮動小数点: 30.45 を str型に変換する
print(str(30.45), type(str(30.45)))
# 30.45 <class 'str'>

# bool: True を int型に変換する
print(int(True), type(int(True)))

# bool: False を int型に変換する
print(int(False), type(int(False)))

# int: 1 を bool型に変換する
print(bool(1), type(bool(1)))

# int: 0 を bool型に変換する
print(bool(0), type(bool(0)))


# bool: True を float型に変換する
print(float(True), type(float(True)))

# bool: False を float型に変換する
print(float(False), type(float(False)))


print('-----------------------------------------------------')


print('-------------------------- 数値計算をする ---------------------------')

### 5. 数値計算をする ###

# 足し算
print(12 + 15 + 50) # 77

# 引き算
print(30 - 15) # 15

# 掛け算
print(5 * 5) # 25

# 割り算
print(12 / 3) # 4.0

# 割り算 Ver. 割り切れない場合
print(15 / 7) # 2.142857142857143

# // で、小数点を切り捨てる
print(12 // 3) # 4
print(15 // 7) # 2








