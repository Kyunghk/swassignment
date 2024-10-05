def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "0으로 나눌 수 없습니다."


# 사용자 입력 받기
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 연산 선택
operation = input("연산을 선택하세요 (+ 또는 -): ")

if operation == '+':
    result = add(num1, num2)
    print(f"결과: {num1} + {num2} = {result}")
elif operation == '-':
    result = subtract(num1, num2)
    print(f"결과: {num1} - {num2} = {result}")
# 기존의 사용자 입력 코드 이후에 추가
elif operation == '*':
    result = multiply(num1, num2)
    print(f"결과: {num1} * {num2} = {result}")
elif operation == '/':
    result = divide(num1, num2)
    print(f"결과: {num1} / {num2} = {result}")
else:
    print("잘못된 연산을 선택하셨습니다. + 또는 -만 선택하세요.")