

# replaceメソッド

# replaceメソッドは、文字列の一部（サブストリング）を新しい文字列に置き換えるメソッドです。

# 文字列内の古いサブストリングを新しいサブストリングに置き換える
hakutou = "白桃さんは、ロボ玉を食べたい！"
momo = hakutou.replace('白桃さん', 'ももちゃん')
print(momo)
# ももちゃんは、ロボ玉を食べたい！


# findメソッド

# return は、最初に発見した index番号 見つからない場合は、-1

piui = 'ピウイは、やんちゃな子猫です'

resutl = piui.find('猫')
print(resutl) # 11


## split() を使って、特定の文字で、文字列を区切る・分割する・リスト化する

hakutou = '白桃さん'
# Defaultは、空白で区切る
result = hakutou.split()
print(result) # ['Robotama', 'is', 'so', 'Cute！']

robotama = 'Robotama is so Cute！'

# Defaultは、空白で区切る
result = robotama.split()
print(result) # ['Robotama', 'is', 'so', 'Cute！']

lang = 'JavaScript,Python,PHP,TypeScript,HTML,CSS'
# 区切り文字を指定する場合
result = lang.split(',')
print(result) # ['JavaScript', 'Python', 'PHP', 'TypeScript', 'HTML', 'CSS']


lang = 'JavaScript ,Python, PHP, TypeScript, HTML, CSS'
result = lang.split(', ')
print(result) # ['JavaScript ,Python', 'PHP', 'TypeScript', 'HTML', 'CSS']