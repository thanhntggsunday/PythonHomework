import  random

#Giả sử số áo của 25 cầu thủ của đội Barcelona là từ 1 đến 25
#danh sách các thủ môn:
lst_thu_mon = ['1', '2', '3']
#danh sách các hậu vệ:
lst_hau_ve_tru = ['4', '5', '6', '7', '8']
lst_hau_ve_bien = ['9', '10', '11', '12']
#danh sach cac tien ve:
lst_tien_ve = ['13', '14', '15', '16', '17', '18', '19', '20', '21']
#danh sách các tiền đạo:
lst_tien_dao = ['22', '23', '24', '25']

#Chọn ra 1 thủ môn:
lst_thu_mon_chon = random.sample(lst_thu_mon, 1)
#Chọn ra 2 hậu vệ trụ:
lst_hau_ve_tru_chon = random.sample(lst_hau_ve_tru, 2)
#Chọn ra 2 hậu vệ biên:
lst_hau_ve_bien_chon = random.sample(lst_hau_ve_bien, 2)
#Chọn ra 4 tiền vệ:\
lst_tien_ve_chon = random.sample(lst_tien_ve, 4)
#Chọn ra 2 tiền đạo:
lst_tien_dao_chon = random.sample(lst_tien_dao, 2)
#In ra danh sách đội hình được chọn:
print('Đội hình được chọn:')
print('Thủ môn: ', ', '.join(lst_thu_mon_chon))
print('Hậu vệ trụ: ', ', '.join(lst_hau_ve_tru_chon))
print('Hậu vệ biên: ', ', '.join(lst_hau_ve_bien_chon))
print('Tiền vệ: ', ', '.join(lst_tien_ve_chon))
print('Tiền đạo:', ', '.join(lst_tien_dao_chon))
