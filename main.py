from PyQt6.QtWidgets import QApplication, QMainWindow

from backend.OrderComfirmExt import OrderConfirmExt

app = QApplication([])
MainWindow = QMainWindow()
mp = OrderConfirmExt()
mp.setupUi(MainWindow)
mp.show()
app.exec()




