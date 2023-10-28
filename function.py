
## 関数の定義

def hello(name):
    """
    挨拶をする関数
    """
    result = 'Hello ' + name + 'さん！'
    return result

print(hello('ロボ玉')) # Hello ロボ玉さん！
print(hello('ピウイ')) # Hello ピウイさん！

# print(help(hello))
## [ 出力結果 ] ##
# Help on function hello in module __main__:

# hello(name)
#     挨拶をする関数


## 関数内でのグローバル変数の作り方

# 関数内は、通常、ローカル・スコープですが、global 変数名 で　グローバル変数を定義することができます。

robotama = "ロボ玉"
def cute(robotama):
    # グローバル変数を定義
    global piui 
    piui= "ピウイ"
    print(robotama, "は可愛い！！")

cute(robotama) # ロボ玉 は可愛い！！
cute(piui) # ピウイ は可愛い！！


## 引数のデフォルト値設定

# デフォルト値を持つ引数の例
def plusTwo(x, y=2): 
   return x + y

print(plusTwo(3)) # 5
print(plusTwo(5)) # 7


## 可変長引数 => 関数の引数の数が不明な場合、それらはすべてタプルにパックすることができます。

# すべての引数は params という引数に「パック」される
def printPrameter(*params): 
    print('引数の数', len(params)) # 引数の数: 5 
    print('Type:', type(params)) # Type: <class 'tuple'>

    # タプルなので、for で取り出す
    for param in params:
        print(param)

printPrameter('ロボ玉','まり玉','ピウイ', '白桃さん', 'ももちゃん')


def calucNum(x, y, *num):
    result = x + y
    for n in num:
        result = result + n
    return result

print('calucNum-1:', calucNum(5,7,5)) # calucNum-1: 17
print('calucNum-2', calucNum(5,7,5,7,7)) # calucNum-2 31


## 可変長引数を、タプルではなく、辞書型で、パックする場合

def dictPack(**robotama):
    print('robotama: ', robotama) # robotama:  {'robotama': 'ロボ玉', 'live': '東京', 'hamflag': True, 'power': 2000}
    print('Type: ', type(robotama)) # Type:  <class 'dict'>

    for key in robotama:
        print(f'{key}: {robotama[key]}')

# 辞書型の可変長引数の場合は、「key=value」の形で、引数をSetする
dictPack(robotama='ロボ玉', live='東京',hamflag=True, power=2000)

# robotama: ロボ玉
# live: 東京
# hamflag: True
# power: 2000








