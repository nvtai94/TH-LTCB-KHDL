#bai1
n = int(input("nhap so nam: "))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(f"nam {n} la nam nhuan")
else:
    print (f"nam {n} khong la nam nhuan" )
#input: nhap so nam: 10
#output: nam 10 khong la nam nhuan

#bai2
x = float (input("nhap x: "))
y = float(input ("nhap y: "))
a = float(input("nhap a: "))
b = float (input ("nhap b: "))
r = float (input ("nhap r: "))
do_dai = (((x-a)**2)+((y-b)**2))**(1/2)
print(f"do dai IM: {do_dai}")
if do_dai <= r:
    print (True)
else:
    print (False)
#input:
# nhap x: 5
# nhap y: 9
# nhap a: 8
# nhap b: 7
# nhap r: 6
#output:do dai IM: 3.605551275463989
#True

#bai3
a = float (input ("nhap a: "))
b = float (input ("nhap b: "))
c = float (input ("nhap c: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("la tam giac deu")
    elif a == b or b == c or a == c:
        if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            print("la vuong can")
        else:
            print("la tam giac can")
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("la tam giac vuong")
    else:
        print("la tam giac thuong")
else:
    print("kh phai tam giac")
# input: 
# nhap a: 3
# nhap b: 6
# nhap c: 4
# output: la tam giac thuong

#bai4
a = int(input ("nhap a: "))
b = int(input ("nhap b: "))
c = int(input("nhap c: "))
so_lon_nhat = a
if b > so_lon_nhat:
    so_lon_nhat = b
if c > so_lon_nhat:
    so_lon_nhat = c
print(f"so lon nhat: {so_lon_nhat}")
#input: 
# nhap a: 3
# nhap b: 4
# nhap c: 5
#output: so lon nhat: 5

#bai5
ki_tu = str(input("nhap ki tu: "))
if ki_tu == "u" or ki_tu == "e" or ki_tu == "o" or ki_tu == "a" or ki_tu == "i":
    print(f"{ki_tu} la nguyen am")
else:
    print(f"{ki_tu} la phu am")
#intput: nhap ki tu: e
#output: e la nguyen am

#bai6
lua_chon = [
"1. phim hoat hinh"
"2. phim hanh dong:"
"3. phim tinh cam"
"4. phim giai tri", ]
lua_chon = int(input("nhap lua chon: "))
if lua_chon == 1:
    print("phim hoat hinh")
elif lua_chon == 2:
    print ("phim hanh dong")
elif lua_chon == 3:
    pint("phim tinh cam")
elif lua_chon == 4:
    print ("phim giai tri")
else:
    print("vui long nhap lai")
#input: nhap lua chon: 4
#output: phim giai tri

#bai8
diem = str(input ("nhap so diem: "))
if diem == "A":
    print ("la sv xuat sac")
elif diem == "B":
        print("la sv gioi")
elif diem == "C":
    print("la sv kha")
elif diem == "D":
    print("la sv TB")
elif diem == "E":
    print ("la sv yeu")
elif diem == "F":
        print("la sv kem")
else:
    print("vui long nhap lai")
#input: nhap so diem: S 
#output: vui long nhap lai

#bai9
luong = float(input ("nhap luong nv: "))
if luong < 7:
    luong_rong = luong - (luong * (10/100))
    print(f"luong nhap duoc la: (luong_rong)")
elif luong >= 7 and luong <= 15:
    luong_rong = luong - (luong * (20/100))
    print(f"luong nhap duoc la: {luong_rong}d")
else:
    luong_rong = luong - (luong * (30/100))
    print (f"luong nhap duoc la: {luong_rong}d")
    #intput:nhap luong nv: 8000000
    #output:luong nhap duoc la: 5600000.0d
    

#bai 10
thang = float(input("nhap thang(1-12):  "))
if thang in [ 1,3,5,7,8,10,12] :
    print("thang co 31 ngay")
elif thang in [ 4,6,9,11] :
    print("thang co 30 ngay")
elif thang == 2:
    nam = float(input("nhap nam:  "))
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("thang 2 co 29 ngay")
    else:
        print("thang 2 co 28 ngay")
else :
    print("vui long nhap lai thang")

    #input: nhap thang(1-12):  12
    #output: thang co 31 ngay
    
#bai11
chu_so = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
while True: 
    n = int(input("Nhap chu so can doc la : "))
    if  100 <= n <= 999 :
        break
    else :
        print("ban nhap ko dung , hay nhap lai ")
if n < 0 : 
    ket_qua = "âm"
    n = abs(n)
else :
    ket_qua = " "
hang_tram = n // 100 
hang_chuc = (n // 10) % 10 
hang_don_vi = n % 10 
ket_qua += chu_so[hang_tram] + " trăm"
if hang_chuc == 0 and hang_don_vi != 0 :
    ket_qua += " lẻ " + chu_so[hang_don_vi]
elif hang_chuc == 1:
    ket_qua += " mười"
    if hang_don_vi != 0:
        ket_qua += " " + chu_so[hang_don_vi]
elif hang_chuc > 1:
    ket_qua += " " + chu_so[hang_chuc] + " mươi"
    if hang_don_vi == 1:
        ket_qua += " mốt"
    elif hang_don_vi == 5:
        ket_qua += " lăm"
    elif hang_don_vi != 0:
        ket_qua += " " + chu_so[hang_don_vi]
print("Cách đọc:", ket_qua)
#input: Nhap chu so can doc la : 678
#output: Cách đọc:  Sáu trăm Bảy mươi Tám
#bai12
tnct = int(input("nhap tnct: "))
if tnct < 12:
    luong = 2.34 * 1350000
    print(f"luong: {luong}d")
elif 12<=tnct<36:
    uong = 3.33 * 1350000
    print(f"luong: {luong}d")
elif 36<=tnct<60:
    luong = 3.66 * 1350000
    print(f"luong: {luong}d")
else :
    luong = 3.99 * 1350000
    print (f"luong: {luong}d")
#input: nhap tnct: 2000000
#output: luong: 5386500.0d