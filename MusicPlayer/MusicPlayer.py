# coding:utf-8
#  https://zhuanlan.zhihu.com/p/44146707
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import qtawesome

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):                                                                      ## one 页面总体布局设置
        # self.setFixedSize(960,700)                                                        #将窗口设置为固定大小
        self.setWindowTitle('lightmumu3/2020/6/19')
        self.main_widget = QtWidgets.QWidget()                                              # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()                                               # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()                                             # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget) # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_close.clicked.connect(self.close)
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("每日推荐")                                   # 添加控件
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("我的音乐")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.music', color='red'), "华语流行")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy', color='white'), "在线FM")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.film', color='white'), "热门MV")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), "本地音乐")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.download', color='white'), "下载管理")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='white'), "我的收藏")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "反馈建议")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "关注我们")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "遇到问题")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")                                                              ##

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        self.right_bar_widget = QtWidgets.QWidget()                                          # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()    # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索  ')                     ## 这个搜索符号怎么来的
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText("输入歌手、歌曲或用户，回车进行搜索")

        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 8)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        self.right_recommend_label = QtWidgets.QLabel("今日推荐")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("Jay")  # 设置按钮文本
        self.recommend_button_1.setIcon(QtGui.QIcon(r'E:\08__自学\other\python\Prj\MusicPlayer\images/jay.jpg'))  # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文

        self.recommend_button_2 = QtWidgets.QToolButton()
        self.recommend_button_2.setText("范特西")
        self.recommend_button_2.setIcon(QtGui.QIcon(r'E:\08__自学\other\python\Prj\MusicPlayer\images/fantasy.jpg'))
        self.recommend_button_2.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_3 = QtWidgets.QToolButton()
        self.recommend_button_3.setText("八度空间")
        self.recommend_button_3.setIcon(QtGui.QIcon(r'E:\08__自学\other\python\Prj\MusicPlayer\images/8 spaces.jpg'))
        self.recommend_button_3.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_4 = QtWidgets.QToolButton()
        self.recommend_button_4.setText("叶惠美")
        self.recommend_button_4.setIcon(QtGui.QIcon(r'E:\08__自学\other\python\Prj\MusicPlayer\images/YeHuimei.jpg'))
        self.recommend_button_4.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_5 = QtWidgets.QToolButton()
        self.recommend_button_5.setText("七里香")
        self.recommend_button_5.setIcon(QtGui.QIcon(r'E:\08__自学\other\python\Prj\MusicPlayer\images/七里香.jpg'))
        self.recommend_button_5.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_recommend_layout.addWidget(self.recommend_button_1, 0, 0)
        self.right_recommend_layout.addWidget(self.recommend_button_2, 0, 1)
        self.right_recommend_layout.addWidget(self.recommend_button_3, 0, 2)
        self.right_recommend_layout.addWidget(self.recommend_button_4, 0, 3)
        self.right_recommend_layout.addWidget(self.recommend_button_5, 0, 4)

        self.right_layout.addWidget(self.right_recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)


        self.right_newsong_lable = QtWidgets.QLabel("猜你喜欢")
        self.right_newsong_lable.setObjectName('right_lable')

        self.right_playlist_lable = QtWidgets.QLabel("热门歌单")
        self.right_playlist_lable.setObjectName('right_lable')

        self.right_newsong_widget = QtWidgets.QWidget()  # 最新歌曲部件
        self.right_newsong_layout = QtWidgets.QGridLayout()  # 最新歌曲部件网格布局
        self.right_newsong_widget.setLayout(self.right_newsong_layout)

        self.newsong_button_1 = QtWidgets.QPushButton("Mojito     周杰伦            Mojito          03::05")
        self.newsong_button_2 = QtWidgets.QPushButton("Perfect    Ed Sheeran       ÷(Deluxe)       04::23")
        self.newsong_button_3 = QtWidgets.QPushButton("NASA       Ariana Grande    Thank U,next     03::02")
        self.newsong_button_4 = QtWidgets.QPushButton("ME!        Taylor Swift     Lover            03::13")
        self.newsong_button_5 = QtWidgets.QPushButton("PUPPET     Kris Who         TESTING          03::21")
        self.newsong_button_6 = QtWidgets.QPushButton("一剪梅     费玉清            天之大          03::46")
        self.right_newsong_layout.addWidget(self.newsong_button_1, 0, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_2, 1, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_3, 2, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_4, 3, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_5, 4, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_6, 5, 1, )


        self.right_playlist_widget = QtWidgets.QWidget()  # 播放歌单部件
        self.right_playlist_layout = QtWidgets.QGridLayout()  # 播放歌单网格布局
        self.right_playlist_widget.setLayout(self.right_playlist_layout)

        self.playlist_button_1 = QtWidgets.QToolButton()
        self.playlist_button_1.setText("无法释怀的整天循环音乐…")
        self.playlist_button_1.setIcon(QtGui.QIcon(r'E:\08__自学\other\python\Prj\MusicPlayer\images/a01.jpg'))
        self.playlist_button_1.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_2 = QtWidgets.QToolButton()
        self.playlist_button_2.setText("不需要歌词,也可以打动你的心")
        self.playlist_button_2.setIcon(QtGui.QIcon(r'E:\08__自学\other\python\Prj\MusicPlayer\images/a02.jpg'))
        self.playlist_button_2.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_3 = QtWidgets.QToolButton()
        self.playlist_button_3.setText("那些你熟悉又不知道名字…")
        self.playlist_button_3.setIcon(QtGui.QIcon(r'E:\08__自学\other\python\Prj\MusicPlayer\images/a03.jpg'))
        self.playlist_button_3.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_4 = QtWidgets.QToolButton()
        self.playlist_button_4.setText("那些只听前奏就中毒的英文歌")
        self.playlist_button_4.setIcon(QtGui.QIcon(r'E:\08__自学\other\python\Prj\MusicPlayer\images/a04.jpg'))
        self.playlist_button_4.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_playlist_layout.addWidget(self.playlist_button_1, 0, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_2, 0, 1)
        self.right_playlist_layout.addWidget(self.playlist_button_3, 1, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_4, 1, 1)

        self.right_layout.addWidget(self.right_newsong_lable, 4, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_lable, 4, 5, 1, 4)
        self.right_layout.addWidget(self.right_newsong_widget, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 5, 1, 4)

        self.right_process_bar = QtWidgets.QProgressBar()  # 播放进度部件
        self.right_process_bar.setValue(12)
        self.right_process_bar.setFixedHeight(3)  # 设置进度条高度
        self.right_process_bar.setTextVisible(False)  # 不显示进度条文字

        self.right_playconsole_widget = QtWidgets.QWidget()  # 播放控制部件
        self.right_playconsole_layout = QtWidgets.QGridLayout()  # 播放控制部件网格布局层
        self.right_playconsole_widget.setLayout(self.right_playconsole_layout)

        self.console_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.backward', color='#F76677'), "")
        self.console_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.forward', color='#F76677'), "")
        self.console_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.pause', color='#F76677', font=18), "")
        self.console_button_3.setIconSize(QtCore.QSize(30, 30))

        self.right_playconsole_layout.addWidget(self.console_button_1, 0, 0)
        self.right_playconsole_layout.addWidget(self.console_button_2, 0, 2)
        self.right_playconsole_layout.addWidget(self.console_button_3, 0, 1)
        self.right_playconsole_layout.setAlignment(QtCore.Qt.AlignCenter)  # 设置布局内部件居中显示

        self.right_layout.addWidget(self.right_process_bar, 9, 0, 1, 9)
        self.right_layout.addWidget(self.right_playconsole_widget, 10, 0, 1, 9)

        self.left_close.setFixedSize(20, 20)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:10px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:7px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:7px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:5px solid #F76677;font-weight:700;}
        ''')

        self.right_bar_widget_search_input.setStyleSheet(
            '''QLineEdit{
                    border:2px solid #dddddd;
                    width:300px;
                    border-radius:10px;
                    padding:2px 5px;
            }''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.right_playlist_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')

        self.right_newsong_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:gray;
                font-size:12px;
                height:40px;
                padding-left:5px;
                padding-right:10px;
                text-align:left;
            }
            QPushButton:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')

        self.right_process_bar.setStyleSheet('''
            QProgressBar::chunk {
                background-color: #F76677;
            }
        ''')

        self.right_playconsole_widget.setStyleSheet('''
            QPushButton{
                border:none;
            }
        ''')

        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框



        self.right_widget.setStyleSheet("""
        QWidget#left_widget{
            background: gray;
            border - top: 1pxsolidwhite;
            border - bottom: 1pxsolidwhite;
            border - left: 1pxsolidwhite;
            border - top - left - radius: 10px;
            border - bottom - left - radius: 10px;}
        """)

        self.main_layout.setSpacing(0)

    def mousePressEvent(self, event):                        # 进行窗口的拖拽
        self.start_x = event.x()
        self.start_y = event.y()

    def mouseMoveEvent(self, event):  # 3
        dis_x = event.x() - self.start_x
        dis_y = event.y() - self.start_y
        self.move(self.x() + dis_x, self.y() + dis_y)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
