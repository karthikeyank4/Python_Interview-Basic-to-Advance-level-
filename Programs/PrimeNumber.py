num = 101
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

print("Prime Number" if is_prime else "Not a Prime Number")

# number =2
# primenumber=True
# if number<2:
#     primeNumber=False
# else:
#     for i in range(2,number):
#         if number%2==0:
#             primenumber=False
#             break
# print(primenumber)