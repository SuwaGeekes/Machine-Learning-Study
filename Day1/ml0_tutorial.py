# 基本型

# int(整数)型
a = 123
print(type(a)) # <class 'int'>
print(a)  # 123

# float(小数)型
b = 123.123
print(type(b))  # <class 'float'>
print(b) #123.123

# string(文字列)型
str = 'SuwaGeeks'
print(type(str)) # <class 'str'>
print(str)  # SuwaGeeks


#シーケンス型

# tuple型
tuple = (32, 35, 54)
print(type(tuple)) # <class 'tuple'>
print(tuple)   # (32, 35, 54)
print(tuple[0]) # 32

# list型
list = [23, 32, 21]
print(type(list))  # <class 'list'>
print(list)    # [23, 32, 21]
print(list[0]) # 23

# 辞書型
dict = {'key1':123, 'key2': 456}
print(type(dict))   # <class 'dict'>
print(dict) # {'key1': 123, 'key2': 456}
print(dict['key1']) #123


# 演算

print(1+2)  # 3
print(4-3)  # 1
print(3*4)  # 12
print(5/2)  # 2.5
print(5//2)  # 2
print(5%2)  # 1
print(2**10)  # 1024

a = 4
if a == 4:
    print(4) # 4
elif a == 3:
    print(3)

for i in range(4):
    print(i, end=' ') # 0 1 2 3
print('')

while a > 0:
    print(a, end=' ') # 4 3 2 1
    a -= 1
print('')


# 関数

# 引数、戻り値あり
def fx(x):
    y = x**2
    return y

# 引数、戻り値なし
def hello():
    print('Hello')

print(fx(8))    # 64
hello()     # Hello
