# مشخصات:
# ایلیا سن سبلی
# 09028400733
# گلستان
# آق قلا
# نمونه دولتی علامه حلی
import sys

import random as ra
from winreg import SetValue
from PyQt5.QtCore import QPointF, Qt, QCoreApplication
from PyQt5.QtGui import QColor, QIntValidator, QKeyEvent, QValidator
from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsDropShadowEffect, 
    QMainWindow, 
    QPushButton, 
    QMenu, 
    QAction,
    QSizePolicy,
    QSlider,
    QStyle,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QWidget,
    QFrame,
    QMessageBox,
    QStackedWidget,
    QLineEdit,
)

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Guess my number!')
        self.ui()
        
    def ui(self):
        self.main_frame = QFrame(self)
        
        self.main_layout = QVBoxLayout(self.main_frame)
        
        self.main_menu_title = QLabel('عددمو حدس بزن! ;)')
        self.play_button = QPushButton('شروع')
        self.exit_button = QPushButton('خروج')
        
        self.main_layout.addWidget(self.main_menu_title)
        self.main_layout.addWidget(self.play_button)
        self.main_layout.addWidget(self.exit_button)
        
        self.name_ui()
        self.set_signals()
        self.set_styles()
        
    def name_ui(self):
        self.setObjectName('main_window')
        self.main_frame.setObjectName('main_frame')
        self.main_menu_title.setObjectName('main_menu_title')
        self.play_button.setObjectName('play_button')
        self.exit_button.setObjectName('exit_button')

    def set_signals(self):
        self.play_button.clicked.connect(self.view_game_window)
        self.exit_button.clicked.connect(self.exit_popup)
        
    def set_styles(self):
        self.setCentralWidget(self.main_frame)
        self.setStyleSheet(
            """ 
            * { font-family: "Simplified Arabic"; }
            
            #main_window {
                background-color: #6F73D2;
            }
            
            #main_frame {
                border: 1px solid transparent;
                border-radius: 20px;
                background-color: #EEEEFF;
                margin: 10px;
                padding: 5px;
            }
            
            #main_menu_title {
                text-align: center;
                font-size: 40px;
                color: #2A2E45;
            }
            
            .button {
                font-size: 25px;
                background-color: #588157;
                color: #EEEEFF;
                text-indent: 10px;
                border-radius: 8px;
                border: 1px solid #4A4E45;
            }
            """
        )
        self.play_button.setProperty('class', 'button')
        self.exit_button.setProperty('class', 'button')
        
        self.main_menu_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.frame_shadow = QGraphicsDropShadowEffect(
            color=QColor(42,46,69),
            offset=QPointF(5, 5),
            blurRadius=5,
        )
        self.main_frame.setGraphicsEffect(self.frame_shadow)
        
        self.play_button_shadow = QGraphicsDropShadowEffect(
            color=QColor(42,46,69),
            offset=QPointF(1, 1),
            blurRadius=1,
        )
        self.play_button.setGraphicsEffect(self.play_button_shadow)
        
        self.exit_button_shadow = QGraphicsDropShadowEffect(
            color=QColor(42,46,69),
            offset=QPointF(1, 1),
            blurRadius=1,
        )
        self.exit_button.setGraphicsEffect(self.exit_button_shadow)
        
    def exit_popup(self):
        self.exit_mb = QMessageBox(self)
        self.exit_mb.setIcon(QMessageBox.Icon.Question)
        self.exit_mb.setWindowTitle('خروج')
        self.exit_mb.setText('آیا میخواهید خارج شوید؟')
        self.exit_mb.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        self.exit_mb.buttons()[0].setText('بله')
        self.exit_mb.buttons()[1].setText('خیر')
        if self.exit_mb.exec() == QMessageBox.Yes:
            app.exit()

    def view_game_window(self):
        tabs.setCurrentIndex(1)

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_ui()
        self.reset()
        self.set_layouts()
        self.set_signals()
        self.set_names()
        self.set_styles()
        
    def reset(self):
        self.the_number = ra.randint(1, 100)
        self.attempts = 0
        self.number_input.setText('1')

    def set_ui(self):
        self.main_frame = QFrame(self)
        self.number_input = QLineEdit(text='1')
        self.input_slider = QSlider(
            Qt.Orientation.Horizontal,
            minimum=1,
            maximum=100,
            tickPosition=QSlider.TickPosition.TicksBothSides,
        )
        self.decrease_buttton = QPushButton(text='<')
        self.increase_buttton = QPushButton(text='>')
        self.attempts_label = QLabel('شما 0 بار حدس زدید.')
        self.check_button = QPushButton(text='بررسی')
        
    def set_layouts(self):
        self.setCentralWidget(self.main_frame)
        self.main_layout = QGridLayout(self.main_frame)
        self.main_layout.addWidget(self.number_input, 0, 0, 1, 2, Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.addWidget(self.input_slider, 1, 0, 1, 2, Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.addWidget(self.decrease_buttton, 2, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.addWidget(self.increase_buttton, 2, 1, 1, 1, Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.addWidget(self.attempts_label, 3, 0, 1, 2, Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.addWidget(self.check_button, 4, 0, 1, 2, Qt.AlignmentFlag.AlignVCenter)
        
    def set_signals(self):
        self.number_input.keyPressEvent = lambda event: self.number_input_filter(event)
        self.input_slider.sliderReleased.connect(
            lambda: self.number_input.setText(str(self.input_slider.value())) if self.number_input != '' else print()
        )
        self.number_input.textChanged.connect(
            lambda: self.input_slider.setValue(1) if self.number_input.text() == ''
               else self.input_slider.setValue(int(self.number_input.text()))
        )
        self.decrease_buttton.clicked.connect(lambda: \
            self.number_input.setText(str(int(self.number_input.text()) - 1)) if (int(self.number_input.text()) - 1) >= 1 else print('\a'))
        self.increase_buttton.clicked.connect(lambda: \
            self.number_input.setText(str(int(self.number_input.text()) + 1)) if (int(self.number_input.text()) + 1) <= 100 else print('\a'))
        self.check_button.clicked.connect(self.guessed)
        
    def set_names(self):
        self.setObjectName('game_window')
        self.main_frame.setObjectName('main_frame')
        self.number_input.setObjectName('number_input')
        self.main_layout.setObjectName('main_layout')
        self.input_slider.setObjectName('input_slider')
        self.decrease_buttton.setObjectName('decrease_buttton')
        self.increase_buttton.setObjectName('increase_buttton')
        self.attempts_label.setObjectName('attempts_label')
        self.check_button.setObjectName('check_button')
        
    def set_styles(self):
        self.setStyleSheet(
            """
            * { font-family: "Simplified Arabic" }
            
            #game_window {
                background: #6F73D2;
            }
            
            #main_frame {
                border: 1px solid black;
                border-radius: 20px;
                background-color: #EEEEFF;
                margin: 10px;
                padding: 5px;
            }
            
            #number_input {
                font-family: "Comic Sans MS";
                font-size: 26px;
                border-radius: 8px;
                border: 1px solid #6F73D2;
            }
            
            #input_slider {
                margin: 5px;
            }
            
            .button {
                font-size: 26px;
                background-color: #588157;
                color: #EEEEFF;
                border-radius: 8px;
                border: 1px solid #4A4E45;
                width: 100%;
            }
            
            #attempts_label {
                border-bottom-width: 3px;
                border-bottom-color: #4A4E45;
                font-size: 20px;
            }
        """)
        self.number_input.setAlignment(Qt.AlignmentFlag.AlignCenter)                
        self.attempts_label.setAlignment(Qt.AlignmentFlag.AlignCenter)                
        self.decrease_buttton.setProperty('class', 'button')
        self.increase_buttton.setProperty('class', 'button')
        self.check_button.setProperty('class', 'button')
        self.set_shadows()
        
    def set_shadows(self):
        self.frame_shadow = QGraphicsDropShadowEffect(
            color=QColor(42,46,69),
            offset=QPointF(5, 5),
            blurRadius=5,
        )
        self.main_frame.setGraphicsEffect(self.frame_shadow)
        
        self.number_input_shadow = QGraphicsDropShadowEffect(
            color=QColor(42,46,69),
            offset=QPointF(5, 5),
            blurRadius=5,
        )
        self.number_input.setGraphicsEffect(self.number_input_shadow)

        self.decrease_buttton_shadow = QGraphicsDropShadowEffect(
            color=QColor(42,46,69),
            offset=QPointF(2, 2),
            blurRadius=3,
        )
        self.decrease_buttton.setGraphicsEffect(self.decrease_buttton_shadow)
        
        self.increase_buttton_shadow = QGraphicsDropShadowEffect(
            color=QColor(42,46,69),
            offset=QPointF(2, 2),
            blurRadius=3,
        )
        self.increase_buttton.setGraphicsEffect(self.increase_buttton_shadow)
        
        self.check_button_shadow = QGraphicsDropShadowEffect(
            color=QColor(42,46,69),
            offset=QPointF(2, 2),
            blurRadius=3,
        )
        self.check_button.setGraphicsEffect(self.check_button_shadow)
        
        self.input_slider_shadow = QGraphicsDropShadowEffect(
            color=QColor(42,46,69),
            offset=QPointF(1, 1),
            blurRadius=0,
        )
        self.input_slider.setGraphicsEffect(self.input_slider_shadow)
        
    def number_input_filter(self, event):
        def save_if_inrange(x):
            if int(self.number_input.text() + chr(x)) <= 100:
                self.number_input.setText(self.number_input.text() + chr(x))
        
        match event.key():
            case Qt.Key.Key_Enter | Qt.Key.Key_Return:
                self.guessed()
                
            case Qt.Key.Key_Backspace:
                #if self.number_input.text()[:-1] != '':
                self.number_input.setText(self.number_input.text()[:-1])
                
            case Qt.Key.Key_0 if self.number_input.text() == '':
                return
                    
            case (
                Qt.Key.Key_0 | 
                Qt.Key.Key_1 | 
                Qt.Key.Key_2 | 
                Qt.Key.Key_3 | 
                Qt.Key.Key_4 | 
                Qt.Key.Key_5 | 
                Qt.Key.Key_6 | 
                Qt.Key.Key_7 | 
                Qt.Key.Key_8 | 
                Qt.Key.Key_9
            ):
                save_if_inrange(event.key())
                
    def guessed(self):
        if self.number_input.text() == '': return
        self.attempts += 1
        self.attempts_label.setText(f'شما {self.attempts} بار حدس زدید.')
        if int(self.number_input.text()) < self.the_number:
            self.guessed_popup('+')
        elif int(self.number_input.text()) > self.the_number:
            self.guessed_popup('-')
        else:
            self.guessed_popup('=')
        
    def guessed_popup(self, message_type):
        self.guess_mb = QMessageBox(self)
        self.guess_mb.setIcon(QMessageBox.Icon.Information)
        self.guess_mb.setWindowTitle('نتیجه حدس')
        self.guess_mb.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.guess_mb.buttons()[0].setText('باشه')
        self.guess_mb.setStyleSheet('font-size: 18px; font-family: "Simplified Arabic";')
        match message_type:
            case '+':
                self.guess_mb.setText('عددم بیشتر از حدسته!')
            case '-':
                self.guess_mb.setText('عددم کمتر از حدسته!')
            case '=':
                self.guess_mb.setText(f'درست حدس زدی!\nتعداد حدس: {self.attempts}')
                self.return_to_menu()
        self.guess_mb.exec()
        
    def return_to_menu(self):
        self.reset()
        tabs.setCurrentIndex(0)

app = QApplication([])
try:
    main_menu = MainMenu()
    game_window = GameWindow()
    tabs = QStackedWidget()
    tabs.addWidget(main_menu)
    tabs.addWidget(game_window)
    tabs.setWindowTitle(main_menu.windowTitle())
    tabs.show()
except:
    err = QMessageBox()
    err.setIcon(QMessageBox.Icon.Critical)
    err.setWindowTitle('خطا')
    err.setText('مشکلی در اجرای برنامه پیش آمد!')
    err.exec()
finally:
    sys.exit(app.exec())
    