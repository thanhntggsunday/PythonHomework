#Khởi tạo các biến
n1 = 0
n2 = 0
#Nhập vào số nguyên thứ nhất
while True:
    try:
        n1 = int(input('Enter first integer: '))
        break
    except:
        print('Your input wrong data type. try again!')
#Nhập vào số nguyên thứ hai:
while True:
    try:
        n2 = float(input('Enter second integer: '))
        break
    except:
        print('Your input wrong data type. try again!')

gcd = 1 #khởi tạo số chia lớn nhất là 1
k = 2; #possible gcd

while (k <= n1 and k <= n2):
    if (n1 % k == 0 and n2 % k == 0):
        gcd = k #Cập nhật gcd
    k += 1
print('Greatest common divisor for %d and %d is %d' %(n1, n2, gcd))
