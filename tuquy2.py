import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from tuquy2 import Ui_MainWindow  # file .ui được convert thành .py

class GiaodienChinh(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # gán nút tính và nút làm lại
        self.ui.btnthem.clicked.connect(self.tinh_gpa)
        self.ui.btnxoa.clicked.connect(self.lam_lai)

        #lưu kết quả của tổng điểm và tổng tín chỉ khi người dùng nhấn nút thêm
        self.tong_diem = 0
        self.tong_tinchi = 0

    def tinh_gpa(self):
        try:
            # gán biến "diem" và "tinchi" vào ô nhập liệu
            diem = float(self.ui.lnediem.text()) 
            tinchi = int(self.ui.lnetinchi.text()) 

            # cộng dồn điểm và tín chỉ khi bấm nút thêm
            self.tong_diem += diem * tinchi
            self.tong_tinchi += tinchi

            # tính GPA (làm tròn đến 2 chữ số thập phân)
            gpa = round(self.tong_diem / self.tong_tinchi,2)

            # hiển thị kết quả ra ô output
            self.ui.lnekq.setText(str(gpa))

            # phân loại học lực
            if 9<=gpa<=10:
                self.ui.lnekq_2.setText("Xuất sắc")
            elif 8<=gpa<9:
                self.ui.lnekq_2.setText("Giỏi")
            elif 7<=gpa<8:
                self.ui.lnekq_2.setText("Khá")
            elif 5<=gpa<7:
                self.ui.lnekq_2.setText("Trung bình")
            elif 4<=gpa<5:
                self.ui.lnekq_2.setText("Yếu")
            else:
                self.ui.lnekq_2.setText("Kém")

            # xoá ô nhập sau khi thêm điểm và tín chỉ
            self.ui.lnediem.clear()
            self.ui.lnetinchi.clear()

        except ValueError:
            # hiển thị thông báo nếu nhập sai
            self.ui.lnekq.setText("Lỗi! Nhập sai kiểu dữ liệu!")


    def lam_lai(self):
        # reset toàn bộ dữ liệu
        self.tong_diem = 0
        self.tong_tinchi = 0
        self.ui.lnekq.setText(" ")
        sel.ui.lnekq_2.setText(" ")
        self.ui.lnediem.clear()
        self.ui.lnetinchi.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = GiaodienChinh()
    main.show()
    sys.exit(app.exec())






