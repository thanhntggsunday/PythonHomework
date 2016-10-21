soDuong = int(input('Mời bạn vào số đường zig zag: '))
soDiem = int(input('Mời bạn nhập vào số điểm trên mỗi đường: '))
isPrinted = False

for i in range(soDiem):
    for j in range(soDuong * (soDiem - 1) + 1):
        for k in range(1, soDuong + 1):
            if (k % 2 != 0):
                if ((j + i) == (soDiem - 1) * k or (j - i) == (soDiem - 1) * k):
                    print('*', end='')
                    isPrinted = True
                    break
        if (not isPrinted):
            print(' ', end='')
        isPrinted = False
    print()

