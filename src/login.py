import sys
from PySide2 import QtWidgets, QtGui

"Created a basic login widget to practice a bit of pyside"


class Login():
    def __init__(self):

        self.app = QtWidgets.QApplication(sys.argv)

        self.window = QtWidgets.QMainWindow()
        self.imagePath = "images.png"

        self.initGui()

        self.window.setWindowTitle("Login Page")
        self.window.setGeometry(500,100,300,600)

        self.stylesheet = """
        
        QMainWindow {
            background-color : black;
        }
        """
        self.app.setStyleSheet(self.stylesheet)
        self.window.show()

        sys.exit(self.app.exec_())

    def initGui(self):

        #create label
        self.image = QtGui.QImage(self.imagePath)
        self.label = QtWidgets.QLabel(self.window)
        self.label.setGeometry(50, 20, 200, 200)
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)

        # username field
        self.username = QtWidgets.QLineEdit(self.window)
        self.username.setGeometry(25,270,250,40)
        self.username.setText('Username')

        # password field
        self.password = QtWidgets.QLineEdit(self.window)
        self.password.setGeometry(25, 330, 250, 40)
        self.password.setText('Password')

        # email
        self.email = QtWidgets.QLineEdit(self.window)
        self.email.setGeometry(25, 390, 250, 40)
        self.email.setText('Email')

        #button login
        self.login = QtWidgets.QPushButton(self.window)
        self.login.setText("Login")
        self.login.setGeometry(25, 450, 250, 40)
        self.login.clicked.connect(self.logged_in)

        #button signup
        self.signup = QtWidgets.QPushButton(self.window)
        self.signup.setText("Sign Up")
        self.signup.setGeometry(25, 510, 250, 40)

    def logged_in(self):
        print("Logged in User : " + self.username.text())

if __name__ == "__main__":
    login = Login()
