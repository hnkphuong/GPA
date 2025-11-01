def tinhgpa(dsdiem,dstinchi):
    tongdiem=0
    tongtinchi=0
    for i in range(len(dsdiem)):
        tongdiem+=dsdiem[i]*dstinchi[i]
        tongtinchi=sum(dstinchi)
        gpa=tongdiem/tongtinchi
        print(gpa)

def xeploai(gpa):
    if 9<=gpa<=10:
        print("Xuất sắc")
    if 8<=gpa<9:
        print("Giỏi")
    if 7<=gpa<8:
        print("Khá")
    if 5<=gpa<7:
        print("Trung bình")
    if 4<=gpa<5:
        print("Yếu")
    else:
        print("Kém")

