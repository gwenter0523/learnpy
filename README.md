Python Note

 目录

# 1. Python基础

## 数据类型

- 整数(int)

- 浮点数(float)

- 字符串(str)

- 布尔值(bool)
  - True
  - False
  - 布尔值可以用and、or和not运算

- 空值(None)
  - 与空值None进行比较时，用 `is` 或者 `is not`，永远不要用等号来比较！

- 变量
  - 变量名 = 变量值( 如a = 10 )

- 常量
  - 通常用大写表示常量( 如 PI = 3.14 )
  
## python的字符串

### 字符串的编码

- python3的字符串是使用Unicode编码的，支持多语言。

- 单个字符的编码：
  - 有`ord()`方法，获取字符的整数表示。
    ```ord()
    >>>  `ord('A')`
    > 65
    ```
  - `chr()`方法则把编码转换为对应字符。
    ```chr()
    >>> `chr(25991)`
    '文'
    ```

- `'ABC'`与`b'ABC'`，前者是str，后者是bytes，每个字符只占用一个字节。
  - 用Unicode表示的str可以通过`encode()`方法编码为指定的bytes。在bytes中，无法显示为ACSCII的字符，会用\x##来表示
    ```encode()
    >>> 'ABC'.encode('ascii')
    b'ABC'
    >>> '中文'.encode('utf-8')
    b'\xe4\xb8\xad\xe6\x96\x87'
    ```
  - 反过来，可以把bytes变为str，就要用`decode()`方法
    ```decode()
    >>> b'\xe4\xb8\xad\xe6\x96\x87'
    '中'
    ```
    - 可以传入`error='ignore'`忽略错误的字节
    ```error="ignore"
    >>> b'\xe4\xb8\xad\xff'.decode('utf-8rrors='ignore')
    '中'
    ```

- 使用`len()`来计算str中包含多少字符。换成bytes，则计算字节数。

- 通常，在保存源代码的时候，要保存为utf-8格式编码。

  ```声明
  #!/usr/bin/env python
  # -*- coding: utf-8 -### 字符串格式化
  ```

### 字符串格式化

``` %
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
```

- `%`运算符用来格式化字符串。在字符串内部，`%s`表示字符串替换，`%d`表示整数替换。有几个`%?`占位符，后面就跟几个变量huo值对应。如果只有一个`%?`，括号可以省略。
- 常见占位符

  占位符 | 替换内容
  ----- | ------
  %d | 整数
  %f | 浮点数
  %s | 字符串
  %x | 十六进制整数

- `format()`也能格式化字符串。使用传入的参数依次替换字符串内的{0} {1}

  ``` format()
  >>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
  'Hello, 小明, 成绩提升了 17.1%'
  ```

- `f"str {var}"` 也可以格式化字符串，在{}内的内容可以使用变量

## list和tuple

### list

- 通过索引访问，用`len()`函数获得list元素的个数

``` list
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates[0]
'Michael'
```

- 要获取最后一个元素迈出了通过索引位置，还可以用`-1`做索引，直接获取最后一个元素。以此类推，可以得到倒数第2，3个元素

``` 倒数
>>> classmates[-1]
'Tracy'
>>> classmates[-2]
'Bob'
>>> classmates[-3]
'Michael'
```

- 追加列表元素可用`append()

``` append()
classmates.append('Adam')
```

- 元素插入指定位置，如索引为1，使用`insert(index, var)`

``` insert()
>>> classmates.insert(1, 'Jack')
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
```

- 删除末尾元素，用`pop()`方法。删除指定位置元素，用`pop(i)`方法，i表示索引

``` pop()
>>> classmates.pop(1)
'Jack'
>>> classmates
['Michael', 'Bob', 'Tracy']
```

- 直接赋值给对应索引位置可以替换某个元素

- list中可以嵌套另一个list(二维数组)

### tuple

- tuple: 元组。与list相似，但一旦初始化即不可修改

``` tuple
>>> classmates = ('Micheal', 'Bob', 'Tracy')
```

- 虽然定义tuple时使用的是`()`，但使用索引查询时，仍然要用`[]`

``` []
>>> classmate[0]
'Micheal'
```

- 定义只有一个元素的tuple时，要在元素后加`,`

``` 一个元素
>>> t = (1,)
>>> t
(1,)
```

## 条件判断

- if, elif, else

- if语句会从上往下判断，如果某个判断为true，会忽略剩下的elif和else

## 循环

### for...in循环

```for in
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
```

- for x in ... 把每个元素带入变量x，并执行缩进块内的语句

- `range(1, 100)`，生成一个整数序列，并转换为一个list。range(x)可以直接生成0到x的整数序列

### while循环

- 只要条件满足，就会不断循环

### break

- 在循环中，通过break可以提前退出循环

### continue

- 使用continue，跳过当前循环，直接开始下次循环

