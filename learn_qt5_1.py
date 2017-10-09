import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

label = QtWidgets.QLabel("<p style='color: blue; margin-left: 20px'><b>hell world</b></p>")
label.show()

sys.exit(app.exec_())
