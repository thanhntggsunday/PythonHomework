n = 0
while True:
    try:
        n = int(input("Input an odd number: "))
        if n % 2 == 0:
            print('Sorry, the number you input is a even number.')
        else:
            break
    except:
        print("Sorry, you input wrong data type.")

i = n #Khởi tạo số cần in bằng n
numberSpace = 0 # Số dấu cách cần in trong hàng tương ứng
while i >= 1:
    j = 1
    k = numberSpace
    while k > 0:
        print(' ', end='')
        k -= 1
    while j <= i:
        print(i, end='')
        j += 1
    print()
    list_i = [i] * i #mảng i số i
    list_i_next = [i - 2] * (i - 2) #Mảng (i - 2) số (i - 2)
    #Số dấu cách cần in ra bằng nửa hiệu số ký tự giữa hàng với các số i và hàng các số (i - 2):
    numberSpace += (len(list_i) * len(str(i)) - len(list_i_next) * len(str(i - 2))) // 2
    i -= 2







