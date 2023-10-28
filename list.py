

## リストの作成
japan_location = ["東京", "さいたまー", "グンマー帝国"]

print(japan_location) # ['東京', 'さいたまー', 'グンマー帝国']

## index で 該当Dataを取得する
print(japan_location[0]) # 東京
print(japan_location[1]) # さいたまー


## lenメソッドで、リストの長さ(要素数)を取得する
print(len(japan_location)) # 3


japan_location[0] = 'Tokyo'
print(japan_location)
# ['Tokyo', 'さいたまー', 'グンマー帝国']

## リストのスライス

# index 1から2までの List を切り取る
slice_list = japan_location[1:3]

print(slice_list) 
# ['さいたまー', 'グンマー帝国']

## 元のリストは、破壊されない
print(japan_location) 
# ['Tokyo', 'さいたまー', 'グンマー帝国']


## append() で、リストに1つの要素を追加できる
japan_location.append('ふなっしー')
print(japan_location)
# ['Tokyo', 'さいたまー', 'グンマー帝国', 'ふなっしー']

## extend() を使用してリストに要素を複数・追加する => [] の形で、複数渡すので、要注意
japan_location.extend(['北海道', '沖縄'])
print(japan_location) 
# ['Tokyo', 'さいたまー', 'グンマー帝国', 'ふなっしー', '北海道', '沖縄']


## リストの参照・Copy(Shallow Copy)

cat_list = ['白桃さん', 'ももちゃん', 'ぴうい']

# 参照・Copy
shallow_copy_list = cat_list

shallow_copy_list.append('ロボ玉')

print(cat_list) # ['白桃さん', 'ももちゃん', 'ぴうい', 'ロボ玉']
print(shallow_copy_list) # ['白桃さん', 'ももちゃん', 'ぴうい', 'ロボ玉']


## リストのクローン(Deep Copy)

cat_list = ['白桃さん', 'ももちゃん', 'ぴうい']

# 値・Copy
deep_copy_list = cat_list[:]

deep_copy_list.append('ロボ玉')

print(cat_list) # ['白桃さん', 'ももちゃん', 'ぴうい']
print(deep_copy_list) # ['白桃さん', 'ももちゃん', 'ぴうい', 'ロボ玉']


