print(type(18))
print(type(5.6))
print(type('Hello'))

print(118)
print(0b1110110)
print(0o166)
print(0x76)

# 整数转换为不同进制的字符串
print(bin(118))
print(oct(118))
print(hex(118))

print(int())
print(int(118))
print(int(118.2))
print(int('118'))

#传递两个参数时，第一个参数必须是字符串，第二个参数指定进制
print(int('1110110', 2))
print(int('0o166', 8))
