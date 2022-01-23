from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 201)
        Dialog.setStyleSheet("QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #aa00ff, stop: 1 #ff00ff);\n"
"}")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.inFolderLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.inFolderLabel.setObjectName("inFolderLabel")
        self.gridLayout.addWidget(self.inFolderLabel, 1, 0, 1, 1)
        self.fromNumberEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.fromNumberEdit.setObjectName("fromNumberEdit")
        self.gridLayout.addWidget(self.fromNumberEdit, 2, 1, 1, 1)
        self.toNumberEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.toNumberEdit.setObjectName("toNumberEdit")
        self.gridLayout.addWidget(self.toNumberEdit, 2, 3, 1, 1)
        self.outFolderLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.outFolderLabel.setObjectName("outFolderLabel")
        self.gridLayout.addWidget(self.outFolderLabel, 1, 2, 1, 1)
        self.fromNumberLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fromNumberLabel.setObjectName("fromNumberLabel")
        self.gridLayout.addWidget(self.fromNumberLabel, 2, 0, 1, 1)
        self.runButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.runButton.setObjectName("runButton")
        self.gridLayout.addWidget(self.runButton, 3, 3, 1, 1)
        self.inFolderEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.inFolderEdit.setObjectName("inFolderEdit")
        self.gridLayout.addWidget(self.inFolderEdit, 1, 1, 1, 1)
        self.outFolderEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.outFolderEdit.setObjectName("outFolderEdit")
        self.gridLayout.addWidget(self.outFolderEdit, 1, 3, 1, 1)
        self.toNumberLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.toNumberLabel.setObjectName("toNumberLabel")
        self.gridLayout.addWidget(self.toNumberLabel, 2, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.runButton.clicked.connect(lambda: self.clicked())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.inFolderLabel.setText(_translate("Dialog", "In Folder"))
        self.outFolderLabel.setText(_translate("Dialog", "Out Folder"))
        self.fromNumberLabel.setText(_translate("Dialog", "From Number"))
        self.runButton.setText(_translate("Dialog", "Run"))
        self.toNumberLabel.setText(_translate("Dialog", "To Number"))

    def clicked(self):
        fromDir = self.inFolderEdit.text()
        toDir = self.outFolderEdit.text()
        startYear = int(self.fromNumberEdit.text())
        endYear = int(self.toNumberEdit.text())

        files = os.listdir(fromDir)

        # Create new destinationFolder if it does not exist
        try: 
            os.mkdir(toDir)
        except:
            print("Folder already exists")

        # For each year in the range (ending on the actual endYear)
        # move each matching file fromDir toDir
        for year in range(startYear, endYear+1):
            for file in files:
                if "_" + str(year) in file:
                    fromPath = fromDir + "\\" + file
                    toPath = toDir + "\\" + file
                    shutil.move(fromPath, toPath)
                    print(file)



if __name__ == "__main__":
    import sys
    import os
    import shutil

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
