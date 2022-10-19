import calculator as cal

num1 = int(input("첫 번째 수는 ? : "))
num2 = int(input("두 번째 수는 ? : "))

print(num1, "+", num2, "=", cal.add(num1, num2))
print(num1, "-", num2, "=", cal.sub(num1, num2))
print(num1, "*", num2, "=", cal.mul(num1, num2))
print(num1, "/", num2, "=", cal.div(num1, num2))
