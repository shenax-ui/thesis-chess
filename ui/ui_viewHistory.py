# Form implementation generated from reading ui file './viewHistory.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_viewHistoryx(object):
    def setupUi(self, viewHistoryx):
        viewHistoryx.setObjectName("viewHistoryx")
        viewHistoryx.resize(1062, 688)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/app.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        viewHistoryx.setWindowIcon(icon)
        self.viewHistory = QtWidgets.QDialogButtonBox(parent=viewHistoryx)
        self.viewHistory.setGeometry(QtCore.QRect(550, 620, 461, 32))
        self.viewHistory.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.viewHistory.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.viewHistory.setObjectName("viewHistory")
        self.chessOutput = QtWidgets.QLabel(parent=viewHistoryx)
        self.chessOutput.setGeometry(QtCore.QRect(30, 40, 541, 611))
        self.chessOutput.setText("")
        self.chessOutput.setObjectName("chessOutput")
        self.matchList = QtWidgets.QListWidget(parent=viewHistoryx)
        self.matchList.setGeometry(QtCore.QRect(720, 90, 256, 51))
        self.matchList.setObjectName("matchList")
        self.loadButton = QtWidgets.QPushButton(parent=viewHistoryx)
        self.loadButton.setGeometry(QtCore.QRect(810, 170, 91, 24))
        self.loadButton.setObjectName("loadButton")
        self.labelMovesList = QtWidgets.QLabel(parent=viewHistoryx)
        self.labelMovesList.setGeometry(QtCore.QRect(820, 270, 81, 16))
        self.labelMovesList.setObjectName("labelMovesList")
        self.movesList = QtWidgets.QListWidget(parent=viewHistoryx)
        self.movesList.setGeometry(QtCore.QRect(720, 300, 256, 192))
        self.movesList.setObjectName("movesList")

        self.retranslateUi(viewHistoryx)
        self.viewHistory.accepted.connect(viewHistoryx.accept) # type: ignore
        self.viewHistory.rejected.connect(viewHistoryx.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(viewHistoryx)

    def retranslateUi(self, viewHistoryx):
        _translate = QtCore.QCoreApplication.translate
        viewHistoryx.setWindowTitle(_translate("viewHistoryx", "History"))
        self.loadButton.setText(_translate("viewHistoryx", "Load Match"))
        self.labelMovesList.setText(_translate("viewHistoryx", "Moves List"))