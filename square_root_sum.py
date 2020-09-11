import numpy
import decimal

number = input("Select number: ")

decimal.getcontext().prec = 1000000

sqrt_result = numpy.sqrt(decimal.Decimal(int(number)))

sqrt_digits = list(str(sqrt_result))
del sqrt_digits[1]

sqrt_int_digits = list(map(int, sqrt_digits))

digits_sum = sum(sqrt_int_digits)
print(digits_sum)