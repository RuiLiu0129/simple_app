from qtpy.QtWidgets import QApplication,QDialog, QTabWidget, QWidget, QVBoxLayout, QDialogButtonBox, QLabel, QLineEdit
from qtpy.QtGui import QIcon
import sys

class TabWidget(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("First Python App!")
        self.setWindowIcon(QIcon("./myicon.png"))

        tabwidgt = QTabWidget()
        self.firstTab = FirstTab()
        tabwidgt.addTab(self.firstTab,"Information")

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.firstTab.save)
        buttonbox.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addWidget(tabwidgt)
        vbox.addWidget(buttonbox)
        self.setLayout(vbox)


class FirstTab(QWidget):
    def __init__(self):
        super().__init__()

        name = QLabel("Name:")
        nameEdit = QLineEdit()
        self.nameEdit = nameEdit

        dob = QLabel("Birth Date:")
        dobEdit = QLineEdit()
        self.dobEdit = dobEdit

        phone = QLabel("Phone Number:")
        phoneEdit = QLineEdit()
        self.phoneEdit = phoneEdit

        address = QLabel("Address:")
        addressEdit = QLineEdit()
        self.addressEdit = addressEdit

        layout = QVBoxLayout()
        layout.addWidget(name)
        layout.addWidget(nameEdit)
        layout.addWidget(dob)
        layout.addWidget(dobEdit)
        layout.addWidget(phone)
        layout.addWidget(phoneEdit)
        layout.addWidget(address)
        layout.addWidget(addressEdit)
        self.setLayout(layout)

    def save(self):
        name = self.nameEdit.text()
        dob = self.dobEdit.text()
        phone = self.phoneEdit.text()
        address = self.addressEdit.text()
        print(name, dob, phone, address)

if __name__=="__main__":
    app = QApplication(sys.argv)
    tabwidgt = TabWidget()
    tabwidgt.show()
    app.exec()