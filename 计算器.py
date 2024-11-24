import time
import os
print("----------------")
print("| 科 学 计 算 器 |")
print("----------------")
print("|  1   2   3   |")
print("----------------")
print("|  4   5   6   |")
print("----------------")
print("|  7   8   9   |")
print("----------------")
print("| +  -  *  /   |")
print("----------------")
os.system('cls')
def progress_bar() :
    if __name__ == '__main__':
        progress_bar()
for i in range(101):
    print(f'\r清理缓存: {"#" * i}{"." * (100 - i)} {i}%', end='')
    time.sleep(0.01)
print("                            ")
number1 = int(input("请输入第1个数字:"))
number2 = int(input("请输入第2个数字:"))
def add(number1, number2):
    return number1 + number2
def subtract(number1, number2):
    return number1 - number2
def multiply(number1, number2):
    return number1 * number2
def divide(number1, number2):
    return number1 / number2
letter = input("请输入运算符号，仅支持+-*/:")
if letter == '+':
    def progress_bar():
        for i in range(101):
            print(f'\r清理缓存: {"#" * i}{"." * (100 - i)} {i}%', end='')
            time.sleep(0.004)
    print(number1, "+", number2, "=", add(number1, number2))

elif letter == '-':
    def progress_bar():
        for i in range(101):
            print(f'\r清理缓存: {"#" * i}{"." * (100 - i)} {i}%', end='')
            time.sleep(0.004)
    print(number1, "-", number2, "=", subtract(number1, number2))

elif letter == '*':
    def progress_bar():
        for i in range(101):
            print(f'\r清理缓存: {"#" * i}{"." * (100 - i)} {i}%', end='')
            time.sleep(0.004)
    print(number1, "*", number2, "=", multiply(number1, number2))

elif letter == '/':
    def progress_bar():
        for i in range(101):
            print(f'\r清理缓存: {"#" * i}{"." * (100 - i)} {i}%', end='')
            time.sleep(0.004)
    print(number1, "/", number2, "=", divide(number1, number2))

else:
    def progress_bar():
        for i in range(101):
            print(f'\r清理缓存: {"#" * i}{"." * (100 - i)} {i}%', end='')
            time.sleep(0.004)
    print("运算符号无效")
if __name__ == '__main__':
    progress_bar()





