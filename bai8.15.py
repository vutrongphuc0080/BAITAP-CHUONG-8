a = True
S = 0
while a:
    print("nhập số nguyên N: ")
    b = int(input())
    S = S + b
    print("tổng số hạng đã nhập là: ")
    print(S)
    if b == 0:
        a = False
        break

    