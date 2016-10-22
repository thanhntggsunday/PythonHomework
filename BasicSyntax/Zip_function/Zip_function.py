x = [9, 2, 3, 2, 1, 2]
y = [4, 5, 6, 7, 12, 15]
#tạo các list x1, y1 mà sẽ có x1[i] + y1[i] <= 10
x1 = []
y1 = []
lenght = len(x)
i = 0
while i < lenght:
    if(x[i] + y[i] < 10):
       x1.append(x[i])
       y1.append(y[i])
    i += 1
zipped = zip(x1, y1)
lstZipped = list(zipped)#lstZipped là list chứa các tuple có tổng 2 phần tử  <= 10
print(lstZipped)
