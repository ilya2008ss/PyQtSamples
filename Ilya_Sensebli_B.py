# مشخصات:
# ایلیا سن سبلی
# 09028400733
# گلستان
# آق قلا
# نمونه دولتی علامه حلیimport sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QFrame, 
    QGridLayout,
    QMessageBox,
    QSizePolicy, 
    QVBoxLayout, 
    QPushButton, 
    QLabel, 
    QStackedWidget,
    QWidget, 
)

base_styles = '''
* { 
    font-family: "Simplified Arabic";
}

#window {
    background-color: #6F73D2;
}

#main_frame {
    border: 1px solid transparent;
    border-radius: 20px;
    background-color: #EEEEFF;
    margin: 10px;
    padding: 5px;
}

.button {
    font-size: 25px;
    background-color: #588157;
    color: #EEEEFF;
    text-indent: 10px;
    border-radius: 8px;
    border: 1px solid #4A4E45;
}

QLabel {
    font-size: 26px;
}
'''

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tic Tac Toe Game')
        self.set_ui()
        self.set_layouts()
        self.set_signals()
        self.set_names()
        self.set_styles()
        self.set_classes()
        
    def set_ui(self):
        self.main_frame = QFrame()
        self.main_layout = QVBoxLayout(self.main_frame)
        self.main_title = QLabel('                 بازی دو نفره دوز')
        self.play_button = QPushButton('شروع')
        self.quit_button = QPushButton('خروج')
     
    def set_layouts(self):
        self.main_frame.setParent(self)
        self.setCentralWidget(self.main_frame)
        self.main_layout.addWidget(self.main_title, Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(QWidget(), Qt.AlignmentFlag.AlignBottom)
        self.main_layout.addWidget(self.play_button, Qt.AlignmentFlag.AlignBottom)
        self.main_layout.addWidget(self.quit_button, Qt.AlignmentFlag.AlignBottom)

    def set_signals(self):
        self.play_button.clicked.connect(lambda: tabs.setCurrentIndex(1))
        self.quit_button.clicked.connect(app.quit)

    def set_names(self):
        self.setObjectName('window')
        self.main_frame.setObjectName('main_frame')
        self.main_layout.setObjectName('main_layout')
        self.main_title.setObjectName('main_title')
        self.play_button.setObjectName('play_button')
        self.quit_button.setObjectName('quit_button')
        
    def set_styles(self):
        self.setStyleSheet('#main_title { font-size: 32px !important; }')
        
    def set_classes(self):
        self.play_button.setProperty('class', 'button')
        self.quit_button.setProperty('class', 'button')

class SelectRoles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_ui()
        self.set_layouts()
        self.set_signals()
        self.set_names()
        self.set_classes()
        self.player_1 = 'X'
        
    def set_ui(self):
        self.main_frame = QFrame()
        self.main_layout = QGridLayout(self.main_frame)
        self.main_title = QLabel('بازیکن اول نقش خود را انتخاب کند.')
        self.x_button = QPushButton('X')
        self.o_button = QPushButton('O')
        self.return_button = QPushButton('بازگشت')
    
    def set_layouts(self):
        self.main_frame.setParent(self)
        self.setCentralWidget(self.main_frame)
        self.main_layout.addWidget(self.main_title, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.x_button, 1, 0, 1, 1, Qt.AlignmentFlag.AlignBottom)
        self.main_layout.addWidget(self.o_button, 1, 1, 1, 1, Qt.AlignmentFlag.AlignBottom)
        self.main_layout.addWidget(self.return_button, 2, 0, 1, 2, Qt.AlignmentFlag.AlignBottom)
    
    def set_signals(self):
        self.x_button.clicked.connect(lambda: self.role_selected('X'))
        self.o_button.clicked.connect(lambda: self.role_selected('O'))
        self.return_button.clicked.connect(lambda: tabs.setCurrentIndex(0))
    
    def set_names(self):
        self.setObjectName('window')
        self.main_frame.setObjectName('main_frame')
        self.main_layout.setObjectName('main_layout')
        self.main_title.setObjectName('main_title')
        self.x_button.setObjectName('x_button')
        self.o_button.setObjectName('o_button')
        self.return_button.setObjectName('return_button')
    
    def set_classes(self):
        self.x_button.setProperty('class', 'button')
        self.o_button.setProperty('class', 'button')
        self.return_button.setProperty('class', 'button')
    
    def role_selected(self, player_1_role):
        self.player_1 = player_1_role
        tabs.widget(2).reset()
        tabs.widget(2).update_turn_label()
        tabs.setCurrentIndex(2)
        
class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player_1 = 'X'
        self.is_p1_turn = True
        self.whose_turn = lambda: self.player_1 if self.is_p1_turn else ('O' if self.player_1 == 'X' else 'X')
        self.update_turn_label = lambda: self.turn_label.setText('نوبت بازیکن: ' + self.whose_turn())
        self.set_ui()
        self.set_layouts()
        self.set_signals()
        self.set_names()
        self.set_styles()
        self.set_props()
        
    def set_ui(self):
        self.main_frame = QFrame()
        self.main_layout = QGridLayout(self.main_frame)
        self.left_space = QWidget()
        self.right_space = QWidget()
        self.turn_label = QLabel('نوبت بازیکن: ' + self.whose_turn())
        self.board = [[QPushButton() for _ in range(3)] for _ in range(3)]
        self.return_button = QPushButton('بازگشت')
    
    def set_layouts(self):
        self.main_frame.setParent(self)
        self.setCentralWidget(self.main_frame)
        self.main_layout.addWidget(self.left_space, 0, 0, 5, 1)
        self.main_layout.addWidget(self.right_space, 0, 4, 5, 1)
        self.main_layout.addWidget(self.turn_label, 0, 1, 1, 3, Qt.AlignmentFlag.AlignHCenter)
        for i, row in enumerate(self.board):
            for j, button in enumerate(row):
                self.main_layout.addWidget(button, i + 1, j + 1, 1, 1)
        self.main_layout.addWidget(self.return_button, 4, 1, 1, 3, Qt.AlignmentFlag.AlignBottom)
    
    def set_signals(self):
        for i_index, row in enumerate(self.board):
            for j_index, button in enumerate(row):
                button.clicked.connect(lambda checked, i=i_index, j=j_index: self.board_slot_clicked(i, j))
        self.return_button.clicked.connect(lambda: tabs.setCurrentIndex(0))
    
    def set_names(self):
        self.setObjectName('window')
        self.main_frame.setObjectName('main_frame')
        self.main_layout.setObjectName('main_layout')
        self.left_space.setObjectName('left_space')
        self.right_space.setObjectName('right_space')
        self.turn_label.setObjectName('turn_label')
        self.return_button.setObjectName('return_button')
    
    def set_styles(self):
        self.setStyleSheet(
            """
            .board_button {
                border: 3px solid black;
                width: 100%;
                height: 100%;
            }
            """
        )
        self.main_layout.setSpacing(0)
        
        # board alignments
        self.main_layout.setAlignment(self.board[0][0], Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        self.main_layout.setAlignment(self.board[0][1], Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.setAlignment(self.board[0][2], Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)
        self.main_layout.setAlignment(self.board[1][0], Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        self.main_layout.setAlignment(self.board[1][1], Qt.AlignmentFlag.AlignCenter)
        self.main_layout.setAlignment(self.board[1][2], Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        self.main_layout.setAlignment(self.board[2][0], Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        self.main_layout.setAlignment(self.board[2][1], Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.setAlignment(self.board[2][2], Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
    
    def set_props(self):
        self.return_button.setProperty('class', 'button')
        for i in self.board:
            for j in i:
                j.setProperty('class', 'board_button')

    def board_slot_clicked(self, i, j):
        if self.board[i][j].text() == '':
            self.board[i][j].setText(self.whose_turn())
            if self.check_win():
                self.won(self.whose_turn())
            else:
                if self.has_empty_slot():
                    self.is_p1_turn = not self.is_p1_turn
                    self.turn_label.setText('نوبت بازیکن: ' + self.whose_turn())
                else:
                    self.won('=')
        else:
            print('\a') # Make error sound
            
    def has_empty_slot(self) -> bool:
        for i in self.board:
            for j in i:
                if j.text() == '':
                    return True
        return False
            
    def check_win(self):
        for i in range(3):
            if self.board[i][0].text() == self.board[i][1].text() == self.board[i][2].text() != '':
                return True
            if self.board[0][i].text() == self.board[1][i].text() == self.board[2][i].text() != '':
                return True
            
        if self.board[0][0].text() == self.board[1][1].text() == self.board[2][2].text() != '':
            return True
        if self.board[0][2].text() == self.board[1][1].text() == self.board[2][0].text() != '':
            return True
        
        return False
    
    def won(self, winner: str):
        win_mb = QMessageBox()
        win_mb.setIcon(QMessageBox.Icon.Information)
        if winner == '=':
            win_mb.setWindowTitle('مساوی!')
            win_mb.setText('برنده ای نداریم!')
        else:
            win_mb.setWindowTitle('برد!')
            win_mb.setText(f'بازیکن {winner} برنده شد!')
        win_mb.setStandardButtons(QMessageBox.StandardButton.Retry | QMessageBox.StandardButton.Close)
        win_mb.buttons()[0].setText('دوباره بریم')
        win_mb.buttons()[1].setText('بازگشت به منو')
        result = win_mb.exec()
        if result == QMessageBox.Retry:
            self.reset()
            tabs.setCurrentIndex(1)
        else:
            self.reset()
            tabs.setCurrentIndex(0)
            
    def reset(self):
        self.player_1 = tabs.widget(1).player_1
        self.is_p1_turn = True
        for i in self.board:
            for j in i:
                j.setText('')
    
app = QApplication(sys.argv)
tabs = QStackedWidget()
tabs.setFixedSize(562, 562)
tabs.setStyleSheet(base_styles)
tabs.setWindowTitle('Tic Tac Toe')
tabs.addWidget(MainMenu())
tabs.addWidget(SelectRoles())
tabs.addWidget(TicTacToe())
tabs.show()
sys.exit(app.exec_())
