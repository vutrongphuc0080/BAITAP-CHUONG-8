print("[1] phòng Standard")
print("[2] phòng Superior Garden View")
print("[3] phòng siêu nhân điện quang")
print("[4] phòng công chúa phép thuật Winx")
print("[5] phòng Family room")
print("[6] phòng siêu nhân anh hùng trái đất")
print("[7] phòng siêu sao hoàng cung")
print("[8] phòng VIP , dép Vip")
a = int(input("nhập loại phòng muốn chọn: "))
b = int(input("số đêm ở lại: "))
a1 = 1260000
a2 = 1550000
a3 = 1830000
a4 = 2120000
a5 = 2540000
a6 = 4800000
if a == 1:
	print("giá 1 đêm là 1,260,000 đồng")
	if 1<b <=3:
		c = a1*0.25
	if b>3:
		c = a1*0.3
	print("tổng thiệt hại của quý khách là",a1+(c-1)*b)
elif a == 2:
	print("giá 1 đêm là 1,550,000 đồng")
	if 1<b <=3:
		c = a2*0.25
	if b>3:
		c = a2*0.3
	print("tổng thiệt hại của quý khách là",a2+(c-1)*b)
elif a == 3 or a == 4:
	print("giá 1 đêm là 1,830,000 đồng")
	if 1<b <=3:
		c = a3*0.25
	if b>3:
		c = a3*0.3
	print("tổng thiệt hại của quý khách là",a3+(c-1)*b)
elif a == 5 or a == 6:
	print("giá 1 đêm là 2,120,000 đồng")
	if 1<b <=3:
		c = a4*0.25
	if b>3:
		c = a4*0.3
	print("tổng thiệt hại của quý khách là",a4+(c-1)*b)
elif a == 7:
	print("giá 1 đêm là 2,540,000 đồng")
	if 1<b <=3:
		c = a5*0.25
	if b>3:
		c = a5*0.3
	print("tổng thiệt hại của quý khách là",a5+(c-1)*b)
else:
	print("giá 1 đêm là 4,800,000 đồng")
	if 1<b <=3:
		c = a6*0.25
	if b>3:
		c = a6*0.3
	print("tổng thiệt hại của quý khách là",a6+(c-1)*b)