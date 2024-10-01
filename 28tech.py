# Contest 2 
# Bài 1
"""
x=int(input("Nhaajp số nguyên x: "))
A= x ** 3 + 3 * (x**2) +x +1
print(A)

"""
# Bài 2
"""
a,b,c=map(int,input().split())
print(a*(b+c)+b*(a+c))

"""
# Bài 3
"""
C=int(input("Nhập độ c:"))
F = (C * 9/5) + 32  
print("%.2f" %F)
"""
# Bài 4
"""
R=int(input("Nhập vào số n:"))
C = 2 * 3.14 * R
D = 3.14 * R * R
print("%.4f" %C,"%.2f" %D)
"""
# Bài 5
"""
from math import *
x1,y1,x2,y2=map(int,input().split())
KC=sqrt((x1-x2)**2+(y1-y2)**2) 
print("%.2f" %KC)
"""
# Bài 6 Luyện tập viết câu điều kiện

"""
n=int(input("Nhập vào số n: "))
if n % 2 == 0:
    print("Yes")
else :
    print("No")   
if n % 3 == 0 and n % 5 == 0:
    print("Yes")
else :
    print("No")
if n % 3 == 0 and n % 7 != 0:
    print("Yes")
else :
    print("No")
if n % 3 == 0 or n % 7 == 0:
    print("Yes")
else :
    print("No")
if 30 < n < 50 :
    print("Yes")
else :
    print("No")
if n > 30 and ( n % 2 == 0 or n % 3 == 0 or n % 5 == 0):
    print("Yes")
else :
    print("No")
r = n % 10
if n >= 10 and n <= 99 and (r == 2 or r ==3 or r == 5 or r ==7):
    print("Yes")
else :
    print("No")
if n <= 100 and n % 23 == 0:
    print("Yes")
else :
    print("No")
if n < 10 or n > 20:
    print("Yes")
else :
    print("No")
if r % 3 == 0:
    print("Yes")
else :
    print("No")
"""
# Bài 7 Số lớn nhất và nhỏ nhất
# Số lớn nhất <= a mà chia hết cho b
# Số nhỏ nhất >=a mà chia hết cho b
"""
a,b=map(int,input().split())
res1 = a // b * b
print(res1)
if a % b == 0:
    print(a)
else:
    print((a // b )* b + b)
"""
# Bài 8
"""
n,m=map(int,input().split())
print(n + m)
print(n - m)
print(n * m)
if m == 0:
    print("Không tồn tại")
else :
    print("%.4f" ( n/m))
"""
# Bài 9 Kiểm Tra Năm Nhuận

"""
n=int(input())
if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    print("Yes")
else :
    print("No")
"""
# Bài 10 Kiểm Tra Tam Giác
"""
a,b,c= map(int, input().split())
if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
    print("Yes")
else :
    print("No")
"""
# Bài 11 Kiểm Tra Tam Giác Vuông  Cân  Đều

"""
a,b,c=map(int,input().split())
if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
    if a == b and a == c:
        print("Đều")
    elif a == b and b == c and a == c:
        print("Cân")
    elif a ** 2 == b ** 2 + c ** 2 or c * c == b * b + a * a or b * b == a * a + c * c :
        print("Vuông")
    else :
        print("Thường")
else :
    print("KHông hợp lệ")
"""
# Bài 12  Số ngày của tháng 
"""
t,n=map(int,input().split())
if t >= 1 and t <=12 and n >0:
    if t == 1 or t == 3 or t == 5 or t == 7 or t == 8 or t == 10 or t == 12:
        print("Tháng có 31 ngày")
    elif t == 4 or t == 6 or t == 9 or t == 11:
        print("Tháng này có 30 ngày")
    else:
        if n % 400 == 0 or (n % 4 ==0 and n % 100 != 0):
            print("Tháng 2 có 29 ngày")
        else :
            print("Tháng 28 không nhuận có 28 ngày")
else:
    print("Không hợp lệ")
"""
# Bài 13 ĐỔi số qua ngày tháng năm
"""
n = int(input("Nhập ngày: "))
nam = n // 365 #chia để lấy năm
n = n % 365 #Số ngày dư còn lại
tuan = n // 7 #chia để lấy tuần
n = n % 7 #Số ngày còn lại
print( nam , tuan , n)
"""
# Bài 14 Xếp loại học sinh
"""
a,b,c,d=map(float,input().split())
tong = (a + b + c * 2 + d * 3)/7
if tong >= 8:
    print("Giỏi")
elif tong >= 6.5:
    print("Khá")
elif tong >= 5:
    print("Trung Bình")
else:
    print("Yếu")
"""
# Bài 15 Mua Nước . Mua sao để ít tiền nhất
# n là số lít nước cần mua 
# a là chai 1 lít 
# b là chai 2 lít
"""
n,a,b=map(int,input().split())
if  a <= b / 2 : #Chai 1 lít có giá nhỏ hơn hoặc bằng chai hai lít
    print( n * a)
else :
    if n % 2 == 0:# Số lượng lít mua là chẵn
        print(n // 2 * b) 
    else :
        print( (n - 1) //2*b)
"""
# BÀi 16 Kí tự kế tiếp
#cho kí tự in hoa hoặc thường in ra kí tự kế tiếp trong bản chữ cái ở dạng in thường
#VD A-b và Z-a
#A-Z :65-90
#a-z;97-122
#ord : A-> 65
#chr : 65-> A
"""
c = input()
if c == 'z ' or c == 'Z':
    print('a')
else :
    tmp = ord(c)
    tmp += 1
    print(chr(tmp).lower()) #lower chuyển in hoa sang in thường
"""
# Bài 17 Kiểm tra chữ cái
"""
c = input()
if c.isupper():
    print("Hoa")
elif c.islower():
    print("Thường")
elif c.isdigit():
    print("Số")
else:
    print("Specil")
"""
# Bài 18 Chuyển đổi in hoa in thường

"""
c=input()
if c.islower():
    print(c.upper())
elif c.isupper():
    print(c.lower())
else :
    print(c)
"""
# Bài 19 Domino
"""
n,m=map(int,input().split())
if n % 2 == 0:
    print((n/2)*m)
else :
    print((n-1) // 2 * m + m // 2 )
"""
#Bài 20 lát đá quảng trường
# Kích thước viên gạch là a*a 
#Quảng trường có kích thước là n*m
"""
n,m,a =map(int,input().split())
x , y = 0 , 0
if n % a == 0:#Tính số viên gạch có ở cột
    x = n // a
else:
    x = n // a + 1
if m % a == 0 :#Tính số viên gạch có ở hàng
    y = m // a
else:
    y = m // a + 1
print( x * y) #in ra số viên gạch cần tìm

"""
#Bài 21 Frog :Vị trí con ếch sau bước nhảy

"""
a,b,k=map(int,input().split())
left , right = 0 , 0
if k % 2 == 0:
    left = k // 2
    right = k // 2
else :
    left = k // 2 
    right = left + 1
print( right * a - left * b)  
"""
#Bài 22 Đồng Xu
"""
n,S=map(int,input().split())#n là số tờ tiền ,S là tổng mệnh giá
if S % n == 0:
    print( S // n)
else:
    print(S // n +1)
"""
#Bài 23 Doremon leo cầu thang
# n là số bậc cần leo
#m là bội số di chuyển 
"""
n,m=map(int,input().split())
min_step , max_step = 0 , n
if n % 2 == 0 :
    min_step = n // 2
else:
    min_step = n // 2 + 1
ans = (min_step + m - 1)// m * m
if ans <= max_step :
    print(ans)
else :
    print("-1")
"""
#Bài 24 Đi đường ngắn nhất
# d1 là cửa hàng 1 , d2 là cửa hàng 2 , d3 là con đường khác
# xuất phát từ nhà chọn con đường nào để vừa đến hai của hàng mà nhanh nhất
#d1 nhà d2 
#    d3
"""
d1,d2,d3=map(int,input().split())
print(min(d1 + d2 + d3, 2*(d1 + d3), 2*(d1 + d2),2 *(d2 +d3)))
"""
#Bài 25 Đổi tiền
# có n tiền , các mệnh giá tờ tiền là 1 5 10 20 100 đô
# số tờ tiền sau khi rút được toàn bộ là bao nhiêu
"""
n=int(input())
ans = n // 100
n %= 100
ans += n //20
n %= 20
ans += n // 10
n %= 10
ans += n // 5
n %= 5
ans += n// 1
print(ans)
"""

