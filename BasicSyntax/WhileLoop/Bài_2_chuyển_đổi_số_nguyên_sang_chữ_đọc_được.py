numberNeedConvert = 0 #Số cần chuyển sang chữ đọc được
strResult = "" #Chuỗi kết quả chuyển số sang chữ
snumber = ""
#List các chữ tương ứng với 1 chữ số
stringValue = [ "không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
#List đơn vị của 1 chữ số trong số cần chuyển đổi
stringWeight = [["mươi", "trăm" ], ["nghìn"], [ "triệu" ],[ "tỷ" ]]
#Nhập vào số cần chuyển sang từ đọc được:
while True:
    try:
        numberNeedConvert = int(input("Nhập vào số nguyên cần chuyển sang các chữ đọc được:"))
        break
    except:
        print("Bạn nhập sai dữ liệu. Hãy nhập lại!")
#Chuỗi các chữ số từ phải sang trái của số cần chuyển đổi:
stringOfNumberNeedConvert = str(numberNeedConvert)[::-1]
#print(stringOfNumberNeedConvert)
#Số chũ số của số cần chuyển đổi:
lsonnc = len(stringOfNumberNeedConvert)
#print("stringOfNumberNeedConvert.length =", lsonnc)

#List lưu các dãy 3 chữ số một của số cần chuyển đổi:
ranges = []
#Dãy con trong ranges:
subrange = list()

# Đưa các chữ số  vào list các dãy:
for i in range(lsonnc):
    subrange.append(int(stringOfNumberNeedConvert[i]))
    if ((i + 1) % 3 == 0 or i == lsonnc - 1):
        ranges.append(subrange)
        subrange = list()

#print(ranges)
'''
for i in ranges:
    for j in i:
        print(j, end='')
    print()
'''
#biến xác định range[i][0] có phải ở đầu dãy hay không:

# Convert to words:
i = len(ranges) #chỉ số của dãy con ứng với 3 chữ số một:
#Lặp trong các dãy từ hàng nghìn, triệu, tỷ:
while (i > 1):
    i -= 1
    if (i < 3):
        k = len(ranges[i]) #Chỉ số của 1 chữ số trong dãy con của số cần chuyển đổi
        rangeHead = True
        while (k > 0):
            k -= 1
            if (k > 0):#Chữ số không ở cuối dãy con:
                rangeHead = False
                if (k != 1):#Chữ số ở chỉ số khác 1 (ở chỉ số 2 trong dãy con)
                    strResult += " " + stringValue[ranges[i][k]] + " " + stringWeight[0][k - 1]
                    if (ranges[i][k - 1] == 0 and ranges[i][k - 2] == 0):
                        strResult += " " + stringWeight[i][0] + ","
                        break
                elif (ranges[i][1] == 0):#Chữ số '0' ở chỉ số 1 trong dãy con
                        strResult += " " + "linh"
                elif (ranges[i][1] == 1):#Chữ số '1' ở chỉ số 1 trong dãy con
                    strResult += " " + "mười"
                    if (ranges[i][0] == 0):#Chữ số '0' ở chỉ số 0 trong dãy con
                        strResult += " " + stringWeight[i][0] + ","
                        break
                else:
                    strResult += " " + stringValue[ranges[i][k]] + " " + stringWeight[0][k - 1]
                    if (ranges[i][0] == 0):
                        strResult += " " + stringWeight[i][0] + ","
                        break
            elif (rangeHead):
                    strResult += "-" + stringValue[ranges[i][0]] + " "  + stringWeight[i][0] + ","
            elif (ranges[i][0] == 1):
                if (ranges[i][1] != 0 and ranges[i][1] != 1):
                    strResult += " " + "mốt " + stringWeight[i][0] + ","
                else:
                    strResult += " " + stringValue[ranges[i][0]] + " " + stringWeight[i][0] + ","
            elif (ranges[i][0] == 4):
                if (ranges[i][1] != 1):
                    strResult += " " + "tư " + stringWeight[i][0] + ","
                else:
                    strResult += " " + stringValue[ranges[i][0]] + " " + stringWeight[i][0] + ","
            elif (ranges[i][0] == 5):
                if (ranges[i][1] != 0):
                    strResult += " " + "lăm " + stringWeight[i][0] + ","
                else:
                    strResult += " " + stringValue[ranges[i][0]] + " " + stringWeight[i][0] + ","
            else:
                strResult += " " + stringValue[ranges[i][0]] + " " + stringWeight[i][0] + ","
    elif (i == 3):
            k = len(ranges[i])
            rangeHead = True
            while (k > 0):
                k -= 1
                if (k > 0):
                    rangeHead = False
                    if (k != 1):
                        strResult += " " + stringValue[ranges[i][k]] + " " + stringWeight[0][k - 1]
                        if (ranges[i][k - 1] == 0 and ranges[i][k - 2] == 0):
                            strResult += " " + stringWeight[i][0] + ","
                            break
                    elif (ranges[i][1] == 0):
                            strResult += " " + "linh"
                    elif (ranges[i][1] == 1):
                        strResult += " " + "mười"
                        if (ranges[i][0] == 0):
                            strResult += " " + stringWeight[i][0] + ","
                            break
                    else:
                        strResult += " " + stringValue[ranges[i][k]] + " " + stringWeight[0][k - 1]
                        if (ranges[i][0] == 0):
                            strResult += " " + stringWeight[i][0] + ","
                            break
                elif (rangeHead): #voi k = 0:
                        strResult += "-" + stringValue[ranges[i][0]] + " " + stringWeight[i][0] + ","
                elif (ranges[i][0] == 1):
                    if (ranges[i][1] != 0 and ranges[i][1] != 1):
                        strResult += " " + "mốt " + stringWeight[i][0] + ","
                    else:
                        strResult += " " + stringValue[ranges[i][0]] + " " + stringWeight[i][0] + ","
                elif (ranges[i][0] == 4):
                    if (ranges[i][1] != 1):
                        strResult += " " + "tư " + stringWeight[i][0] + ","
                    else:
                        strResult += " " + stringValue[ranges[i][0]] + " " + stringWeight[i][0] + ","
                elif (ranges[i][0] == 5):
                    if (ranges[i][1] != 0):
                        strResult += " " + "lăm " + stringWeight[i][0] + ","
                    else:
                        strResult += " " + stringValue[ranges[i][0]] + " " + stringWeight[i][0] + ","
                else:
                    strResult += " " + stringValue[ranges[i][0]] + " " + stringWeight[i][0] + ","
    else:
        t = i - 3 #với dãy con ứng với đơn vị nghìn tỷ trở lên sẽ giảm chỉ số đi 3
        k = len(ranges[i])
        rangeHead = True
        while (k > 0):
            k -= 1
            if (k > 0):
                rangeHead = False
                if (k != 1):
                    strResult += " " + stringValue[ranges[i][k]] + " " + stringWeight[0][k - 1]
                    if (ranges[i][k - 1] == 0 and ranges[i][k - 2] == 0):
                        #su dung voi t
                        strResult += " " + stringWeight[t][0]
                        break
                elif (ranges[i][1] == 0):
                    strResult += " " + "linh"
                elif (ranges[i][1] == 1):
                    strResult += " " + "mười"
                    if (ranges[i][0] == 0):
                        strResult += " " + stringWeight[t][0]
                        break
                else:
                    strResult += " " + stringValue[ranges[i][k]] + " " + stringWeight[0][k - 1]
                    if (ranges[i][0] == 0):
                        strResult += " " + stringWeight[t][0]
                        break
            elif (rangeHead):#voi k = 0:
                strResult += " " + stringValue[ranges[i][0]] + " " + stringWeight[t][0]
            elif (ranges[i][0] == 1):
                if (ranges[i][1] != 0 and ranges[i][1] != 1):
                    strResult += " " + "mốt " + stringWeight[t][0]
                else:
                    strResult += " " + stringValue[ranges[i][0]] + " " + stringWeight[t][0]
            elif (ranges[i][0] == 4):
                if (ranges[i][1] != 1):
                    strResult += " " + "tư " + stringWeight[t][0]
                else:
                    strResult += " " + stringValue[ranges[i][0]] + " " + stringWeight[t][0]
            elif (ranges[i][0] == 5):
                if (ranges[i][1] != 0):
                    strResult += " " + "lăm " + stringWeight[t][0]
                else:
                    strResult += " " + stringValue[ranges[i][0]] + " " + stringWeight[t][0]
            else:
                strResult += " " + stringValue[ranges[i][0]] + " " + stringWeight[t][0]

# Xet day i = 0:
#bien xac dinh range[i][0] co phai dau day hay khong:
rangeHead = True
k = len(ranges[0])
while (k > 0):
    k -= 1
    if (k > 0):
        rangeHead = False
        if (k != 1):
            strResult += " " + stringValue[ranges[0][k]] + " " + stringWeight[0][k - 1]
            if (ranges[0][k - 1] == 0 and ranges[0][k - 2] == 0):
                break
        elif (ranges[0][1] == 0):
            strResult += " " + "linh"
        elif (ranges[0][1] == 1):
            strResult += " " + "mười"
            if (ranges[0][0] == 0):
                break
        else:
            strResult += " " + stringValue[ranges[0][k]] + " " + stringWeight[0][k - 1]
            if (ranges[0][0] == 0):
                break
    elif (rangeHead):
        strResult += " " + stringValue[ranges[0][0]]
    elif (ranges[0][0] == 1):
        if (ranges[0][1] != 0 and ranges[0][1] != 1):
            strResult += " " + "mốt"
        else:
            strResult += " " + stringValue[ranges[0][0]]
    elif (ranges[0][0] == 4):
        if (ranges[0][1] != 1):
            strResult += " " + "tư"
        else:
            strResult += " " + stringValue[ranges[0][0]]
    elif (ranges[0][0] == 5):
        if (ranges[0][1] != 0):
            strResult += " " + "lăm"
        else:
            strResult += " " + stringValue[ranges[0][0]]
    else:
        strResult += " " + stringValue[ranges[0][0]]


print("Số đã nhập: ")
#In các chữ số của số cần chuyển đổi:
l = len(ranges)
while (l > 0):
    l -= 1
    m = len(ranges[l])
    while (m > 0):
        m -= 1
        print(ranges[l][m],end='')
    print(' ', end='')
print()

#Hiển thị từ tương ứng vói số đã nhập:
print("Chuỗi đọc được tương ứng số đã nhập: \n" + "\t" + strResult)

