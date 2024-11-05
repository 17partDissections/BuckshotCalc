from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from windowError import *

class WindowDefault(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.SetDefaultWindow()

    def SetDefaultWindow(self):
        self.errorWindow = WindowError()
        #self.setGeometry(780, 300, 400, 400)
        self.setFixedSize(300, 400)
        self.setWindowTitle('BuckshotCalc')
        self.setWindowIcon(QIcon('dealerrizz.ico'))

        self.liveAmount = 0
        self.blankAmount = 0
        self.shellsAmount = 0
        self.shots = 0



        self.shotgun = QPixmap('_internal\img\shotgun.png')
        self.shell_idk = QPixmap('_internal\img\shell_idk.png')
        self.shell_live = QPixmap('_internal\img\shell_live.png')
        self.shell_blank = QPixmap('_internal\img\shell_blank.png')

        self.shotgunLabel =QLabel(self)
        self.shellLabel_1 = QLabel(self)
        self.shellLabel_2 = QLabel(self)
        self.shellLabel_3 = QLabel(self)
        self.shellLabel_4 = QLabel(self)
        self.shellLabel_5 = QLabel(self)
        self.shellLabel_6 = QLabel(self)
        self.shellLabel_7 = QLabel(self)
        self.shellLabel_8 = QLabel(self)
        self.shellsLabels = [self.shellLabel_1, self.shellLabel_2, self.shellLabel_3, self.shellLabel_4, self.shellLabel_5, self.shellLabel_6, self.shellLabel_7, self.shellLabel_8]
        self.shotgunLabel.setPixmap(self.shotgun)
        self.shotgunLabel.move(15,25)
        self.shellLabel_1.move(0,170)
        self.shellLabel_1.setPixmap(self.shell_idk)
        self.shellLabel_1.hide()
        self.shellLabel_2.move(20,170)
        self.shellLabel_2.setPixmap(self.shell_idk)
        self.shellLabel_2.hide()
        self.shellLabel_3.move(40,170)
        self.shellLabel_3.setPixmap(self.shell_idk)
        self.shellLabel_3.hide()
        self.shellLabel_4.move(60,170)
        self.shellLabel_4.setPixmap(self.shell_idk)
        self.shellLabel_4.hide()
        self.shellLabel_5.move(80,170)
        self.shellLabel_5.setPixmap(self.shell_idk)
        self.shellLabel_5.hide()
        self.shellLabel_6.move(100,170)
        self.shellLabel_6.setPixmap(self.shell_idk)
        self.shellLabel_6.hide()
        self.shellLabel_7.move(120,170)
        self.shellLabel_7.setPixmap(self.shell_idk)
        self.shellLabel_7.hide()
        self.shellLabel_8.move(140,170)
        self.shellLabel_8.setPixmap(self.shell_idk)
        self.shellLabel_8.hide()


        self.Label = QLabel("BuckshotCalc.", self)
        self.Label.move(65,0)
        self.Label.setFont(QFont("Arial", 20))
        self.vLabel = QLabel("version 0.1   by Q17pd", self)
        self.vLabel.move(5,385)
        self.vLabel.setFont(QFont("Arial", 10))


        self.ShellAmountline = QLineEdit(self)
        self.ShellAmountline.move(0, 70)
        self.ShellAmountline.resize(200,45)
        self.ShellAmountline.setPlaceholderText("shell amount(Live/Blank(ex.:3/4))")
        self.ShellAmountButton = QPushButton("Submit", self)
        self.ShellAmountButton.move(200, 77)
        self.ShellAmountButton.resize(100,30)
        self.ShellAmountButton.clicked.connect(self.OnShellAmountSubmitButtonClick)

        self.ShellKnowledgeline = QLineEdit(self)
        self.ShellKnowledgeline.move(0, 120)
        self.ShellKnowledgeline.resize(200,45)
        self.ShellKnowledgeline.setPlaceholderText("shell knowledge([shell][l/b](ex.:3l/5b))")
        self.ShellKnowledgeButton = QPushButton("Submit", self)
        self.ShellKnowledgeButton.move(200, 128)
        self.ShellKnowledgeButton.resize(100,30)
        self.ShellKnowledgeButton.clicked.connect(self.OnShellKnowledgeSubmitButtonClick)


        self.liveFiredButton = QPushButton("LIVE FIRED", self)
        self.liveFiredButton.move(0, 315)
        self.liveFiredButton.resize(100,30)
        self.liveFiredButton.clicked.connect(self.OnLiveFiredButtonClick)

        self.blankFiredButton = QPushButton("BLANK FIRED", self)
        self.blankFiredButton.move(100, 315)
        self.blankFiredButton.resize(100,30)
        self.blankFiredButton.clicked.connect(self.OnBlankFiredButtonClick)

        self.ExitButton = QPushButton("Exit", self)
        self.ExitButton.move(225, 377)
        self.ExitButton.clicked.connect(self.Exit)


        self.LiveRemainigLabel = QLabel("live shells remaining: 0", self)
        self.LiveRemainigLabel.move(5,230)
        self.LiveRemainigLabel.resize(200, 20)
        self.LiveRemainigLabel.setFont(QFont("Arial", 12))

        self.BlankRemainigLabel = QLabel("blank shells remaining: 0", self)
        self.BlankRemainigLabel.move(5,250)
        self.BlankRemainigLabel.resize(200, 20)
        self.BlankRemainigLabel.setFont(QFont("Arial", 12))

        self.LiveChanceLabel = QLabel("live shell chance: 0%", self)
        self.LiveChanceLabel.move(5,270)
        self.LiveChanceLabel.resize(195, 20)
        self.LiveChanceLabel.setFont(QFont("Arial", 12))

        self.BlankChanceLabel = QLabel("blank shell chance: 0%", self)
        self.BlankChanceLabel.move(5,290)
        self.BlankChanceLabel.resize(200, 20)
        self.BlankChanceLabel.setFont(QFont("Arial", 12))

        self.show()

    def OnShellAmountSubmitButtonClick(self):
        if len(self.ShellAmountline.text()) == 3 and self.ShellAmountline.text()[0].isnumeric() and self.ShellAmountline.text()[1] == "/" and self.ShellAmountline.text()[2].isnumeric():
           self.liveAmount = int(self.ShellAmountline.text()[0])
           self.blankAmount = int(self.ShellAmountline.text()[2])
           self.shellsAmount = self.liveAmount + self.blankAmount
           if(self.shellsAmount == 0):
               self.errorWindow = WindowError()
               self.errorWindow.SetErrorWindow("an error occurred while taking self.shellsAmount.\nthe value cannot be zero.")
               self.ShellAmountline.setText("")
               return
           if (self.shellsAmount > 8):
               self.errorWindow = WindowError()
               self.errorWindow.SetErrorWindow("an error occurred while taking self.shellsAmount.\nthe value cannot be more than 8.")
               self.ShellAmountline.setText("")
               return
           self.shots = 0
           for shell in self.shellsLabels:
               shell.setPixmap(self.shell_idk)
               shell.show()
           uselessShellLabels = 8 - self.shellsAmount
           print(f"useless: {uselessShellLabels}")
           while uselessShellLabels != 0:
               self.shellsLabels[8 - uselessShellLabels].hide()
               uselessShellLabels-=1
           self.ShellAmountline.setText("")
           self.Update()
        else:
            self.errorWindow = WindowError()
            self.errorWindow.SetErrorWindow("an error occurred while taking self.ShellAmountline.text().\ntry again correctly.")
            self.ShellAmountline.setText("")
    def OnShellKnowledgeSubmitButtonClick(self):
        if len(self.ShellKnowledgeline.text()) == 2 and self.ShellKnowledgeline.text()[0].isnumeric():
            if self.shots == 0:
                index = int(self.ShellKnowledgeline.text()[0]) - 1
            else:
                index = int(self.ShellKnowledgeline.text()[0]) + self.shots - 1
            if self.ShellKnowledgeline.text()[1] == "l":
                self.shellsLabels[index].setPixmap(self.shell_live)
            elif self.ShellKnowledgeline.text()[1] == "b":
                self.shellsLabels[index].setPixmap(self.shell_blank)
            else:
                self.errorWindow = WindowError()
                self.errorWindow.SetErrorWindow("an error occurred while taking self.ShellKnowledgeline.text().\ntry again correctly.")
                self.ShellKnowledgeline.setText("")
                return
            self.ShellKnowledgeline.setText("")
            self.Update()
        else:
            self.errorWindow = WindowError()
            self.errorWindow.SetErrorWindow("an error occurred while taking self.ShellKnowledgeline.text().\ntry again correctly.")
            self.ShellKnowledgeline.setText("")
            return

    def OnLiveFiredButtonClick(self):
        if(self.liveAmount == 0):
            self.errorWindow = WindowError()
            self.errorWindow.SetErrorWindow("an error occurred while taking self.liveAmount.\nthe value cannot be zero.")
            return
        self.liveAmount-=1
        self.shellsLabels[self.shots].hide()
        self.shots+=1
        self.Update()
    def OnBlankFiredButtonClick(self):
        if(self.blankAmount == 0):
            self.errorWindow = WindowError()
            self.errorWindow.SetErrorWindow("an error occurred while taking self.blankAmount.\nthe value cannot be zero.")
            return
        self.blankAmount-=1
        self.shellsLabels[self.shots].hide()
        self.shots+=1
        self.Update()


    def Update(self):
        self.shellsAmount = self.liveAmount + self.blankAmount
        self.LiveRemainigLabel.setText(f"live shells remaining: {self.liveAmount}")
        self.BlankRemainigLabel.setText(f"blank shells remaining: {self.blankAmount}")
        if(self.shellsAmount == 0):
            self.LiveChanceLabel.setText(f"live shell chance: 0%")
            self.BlankChanceLabel.setText(f"blank shell chance: 0%")
            return
        liveChance = (self.liveAmount/self.shellsAmount)*100
        blankChance = (self.blankAmount/self.shellsAmount)*100
        self.LiveChanceLabel.setText(f"live shell chance: {(round(liveChance, 2))}%")
        print("Update")
        self.BlankChanceLabel.setText(f"blank shell chance: {(round(blankChance, 2))}%")
        print("Update")
        print(f"shells amount: {self.shellsAmount}")
        print(f"live amount: {self.liveAmount}")
        print(f"blank amount: {self.blankAmount}")
    def Exit(self):
        self.destroy()