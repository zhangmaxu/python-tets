print(0.123456789)

print(float())
print(float(118.2))
print(float('118'))

#科学技术法
print(float(2.3e8))
print(2.3e8)
print(float(2.3e-4))
print(2.3e-4)

print(1.1 + 2.2 -3.3)

from decimal import Decimal
print(Decimal('1.1')+ Decimal('2.2')-Decimal('3.3'))

from fractions import Fraction
print(Fraction(11, 10)+ Fraction(22, 10)-Fraction(33, 10)) #代表11/10， 22/10， 33/10 对浮点型进行精确计算