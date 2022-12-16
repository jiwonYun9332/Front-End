
input()
# Hello, world! (입력)

# input 함수의 결과를 변수에 할당하기

x = input()
# Hello, world! (입력)

print(x)

x = input('문자열을 입력하세요: ')

print(x)

# input 로 받은 두 숫자의 합 구하기

a = input('첫 번째 숫자를 입력하세요: ')
b = input('두 번째 숫자를 입력하세요: ')

print(a + b)

# result -> 1020
# input 에서 입력받은 값은 항상 문자열 형태이기 때문에 정수 덧셈이 아닌 문자열 덧셈이 이루어진다.

a = int(input('첫 번째 숫자를 입력하세요: ')) # int를 사용하여 입력 값을 정수로 변환
b = int(input('두 번째 숫자를 입력하세요: ')) # int를 사용하여 입력 값을 정수로 변환

print(a + b)






