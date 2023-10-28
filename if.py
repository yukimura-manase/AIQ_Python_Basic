
### Python の条件文 ###

## 比較演算子 ##
# 

# 以下は、よく使われる比較演算子の一覧です：

# 等しい: ==
# 等しくない: !=
# より大きい: >
# より小さい: <
# 以上: >=
# 以下: <=



# 1.「等しいかどうか？」を比較・判定する

robotamaPower = 1000
hakutouPower = 3000
piuiPower = 1000

# 値が「等しいかどうか？」を比較・判定する
result = robotamaPower == hakutouPower
result2 = robotamaPower == piuiPower

print(result) # False
print(result2) # True


# 2.「等しくないかどうか？」を比較・判定する

robotamaPower = 1000
hakutouPower = 3000
piuiPower = 1000

# 値が「等しくないかどうか？」を比較・判定する
result = robotamaPower != hakutouPower
result2 = robotamaPower != piuiPower

print(result) # True
print(result2) # False


# 3. 以上と以下の比較・判定 

robotamaPower = 1000
hakutouPower = 3000
maritamaPower = 1500

# maritamaPower は、robotamaPower 以上 で hakutouPower 以下
result = robotamaPower <= maritamaPower <= hakutouPower
result2 = not (robotamaPower <= maritamaPower <= hakutouPower)

print(result) # True
print(result2) # False


## 条件分岐

print('成人・Checker')
# 年齢
age = 20 

if age > 20:
    print("大人だね🌟")
elif age == 20:
    print("成人の儀式！バンジージャンプ🔥")
else:
    print("まだ、お酒は飲めません。。。ぴえん🥺")



## 論理演算子による条件の組み合わせ
# and 演算子: すべての条件がTrueの場合にTrueになる
# or 演算子: 条件のうちの1つ以上がTrueなら、Trueになる
# not 演算子: 条件の真偽を反転する


season = '夏'
favoritePlace = '海'

if season == '夏' and favoritePlace == '海':
  print('夏だ！ビーチに行こう！')
elif season == '夏' and season == '山':
  print('夏だ！山に行こう！')


age = 28

# 年齢が20以下、または、30以上かどうかを判断
if (age <= 20) or (age >= 30):
    print("年齢は20以下、または、30以上です")
else:
    print("年齢は20以下、または、30以上ではありません")



age = 25
# 20ではない場合
if not (age == 20):
    print("20では、ありません")
# 20の場合
else:
    print("20です🌟")









