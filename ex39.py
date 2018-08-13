# dict
# 字典
# del dict[key] 从字典中删除东西

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michgan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY states has: ", cities['NY'])
print("OR states has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michgan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

# print every states abbreviation
print('-' * 10)
# 遍历字典类型
# states.items() 意思是把states中的每一项转化为dict_items类型的实例
# dict_item类型：dict_items([('name': 'zed'), (b: c)])
# list(dict_item) 则是把它转化为list类型，转换结果如下
# [('name': 'zed'), (b: c)]
# 每一项是一个元组（tuple）
for state, abbrev in list(states.items()):
    print(f"{states} state is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} states is a abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("-" * 10)
# safely get a abbreviation by state that mighy not be there
# dic.get(key)，从字典中通过key获取元素
# 如果没找到这个key，则返回一个nonetype
state = states.get("Texas")

if not state:
    print("Sorry")


# get a city with a default value
# 使用get获取字典元素时，如果传入第二个参数，表示如果没有获取到任何值时，返回的默认值
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")