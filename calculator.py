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
        return "0���� ���� �� �����ϴ�."


# ����� �Է� �ޱ�
num1 = float(input("ù ��° ���ڸ� �Է��ϼ���: "))
num2 = float(input("�� ��° ���ڸ� �Է��ϼ���: "))

# ���� ����
operation = input("������ �����ϼ��� (+ �Ǵ� -): ")

if operation == '+':
    result = add(num1, num2)
    print(f"���: {num1} + {num2} = {result}")
elif operation == '-':
    result = subtract(num1, num2)
    print(f"���: {num1} - {num2} = {result}")
# ������ ����� �Է� �ڵ� ���Ŀ� �߰�
elif operation == '*':
    result = multiply(num1, num2)
    print(f"���: {num1} * {num2} = {result}")
elif operation == '/':
    result = divide(num1, num2)
    print(f"���: {num1} / {num2} = {result}")
else:
    print("�߸��� ������ �����ϼ̽��ϴ�. + �Ǵ� -�� �����ϼ���.")