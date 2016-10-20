#Mảng từ 1 đến 100:
listNumbers = []
#Các số chia hết cho 3:
listNumbersDivisibilityFor3 = []
#Các số chia hết cho 5:
listNumbersDivisibilityFor5 = []
#Thêm các số từ 1 đến 100 vào mảng:
for i in range(1, 101):
    listNumbers.append(i)
#Tìm các số chia hết cho 3 và cho 5, đưa vào mảng tương ứng:
for i in listNumbers:
    if i % 3 == 0:
        listNumbersDivisibilityFor3.append(i)
    if i % 5 == 0:
        listNumbersDivisibilityFor5.append(i)
#In các mảng cần tìm:
print('list Numbers Divisibility For 3:')
print(listNumbersDivisibilityFor3)
print('list Numbers Divisibility For 5')
print(listNumbersDivisibilityFor5)
