def tinhgpa(dsdiem,dstinchi):
    tongdiem=0
    tongtinchi=0
    for i in range(len(dsdiem)):
        tongdiem+=dsdiem[i]*dstinchi[i]
        tongtinchi=sum(dstinchi)
        gpa=tongdiem/tongtinchi
    return gpa

def xeploai(gpa):
    elif 9<=gpa<=10:
        return "Xuất sắc"
    elif 8<=gpa<9:
        return "Giỏi"
    elif 7<=gpa<8:
        return "Khá"
    elif 5<=gpa<7:
        return "Trung bình"
    elif 4<=gpa<5:
        return "Yếu"
    else:
        return "Kém"

