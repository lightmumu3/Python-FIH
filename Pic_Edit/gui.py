#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import numpy as np
import algorithms as alg
import os
from typing import Optional
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    qApp,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsItem,
    QListWidget,
    QHBoxLayout,
    QWidget,
    QStyleOptionGraphicsItem,
    QMessageBox,
    QInputDialog,
    QFileDialog)
from PyQt5.QtGui import QPainter, QMouseEvent, QColor, QImage, QPen
from PyQt5.QtCore import QRectF, Qt, QDir


class MyCanvas(QGraphicsView):

    def __init__(self, *args):
        super().__init__(*args)
        self.main_window = None
        self.list_widget = None
        self.item_dict = {}
        self.selected_id = ''

        self.status = ''
        self.temp_id = ''
        self.temp_item = None

        self.setStyleSheet("padding: 0px; border: 0px;")
        self.startX = self.startY = 0
        self.oldX = self.oldY = 0

    def insert_image(self, item_id):
        fileName = QFileDialog.getOpenFileName(self, "打开图片", QDir.currentPath())[0]
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                return
        item = MyItem(item_id, "image", [[0, 0], [600, 600]])
        item.text = fileName
        self.scene().addItem(item)
        self.item_dict[item_id] = item
        self.list_widget.addItem(item_id)
        self.finish_draw()

    def start_draw_text(self, item_id):
        self.status = 'text'
        self.temp_id = item_id

    def start_draw_line(self, item_id):
        self.status = 'line'
        self.temp_id = item_id

    def start_translate(self):
        self.status = 'translate'
        self.temp_id = ''

    def start_rotate(self):
        self.status = 'rotate'
        self.temp_id = ''

    def start_scale(self):
        self.status = 'scale'
        self.temp_id = ''

    def finish_draw(self):
        self.temp_id = self.main_window.get_id()

    def clear_selection(self):
        if self.selected_id != '':
            self.item_dict[self.selected_id].selected = False
            self.selected_id = ''

    def selection_changed(self, selected):
        self.main_window.statusBar().showMessage('图元选择： %s' % selected)
        if self.selected_id != '':
            self.item_dict[self.selected_id].selected = False
            self.item_dict[self.selected_id].update()
        self.selected_id = selected
        self.item_dict[selected].selected = True
        self.item_dict[selected].update()
        self.status = ''
        self.updateScene([self.sceneRect()])

    def mousePressEvent(self, event: QMouseEvent) -> None:
        pos = self.mapToScene(event.localPos().toPoint())
        x = int(pos.x())
        y = int(pos.y())
        self.startX = x
        self.startY = y
        self.oldX = self.oldY = 0
        if self.status == 'line':
            self.temp_item = MyItem(self.temp_id, self.status, [[x, y], [x + 1, y + 1]])
            self.scene().addItem(self.temp_item)
        elif self.status == 'text':
            self.temp_item = MyItem(self.temp_id, self.status, [[x, y], [x + 1, y + 1]])
            self.scene().addItem(self.temp_item)
        elif self.status == 'translate' or self.status == 'rotate' \
                or self.status == 'scale':
            if self.selected_id != '':
                item = self.item_dict[self.selected_id]
                self.temp_p_list = item.p_list
                boundingRect = item.boundingRect()
                self.cx = boundingRect.center().x()
                self.cy = boundingRect.center().y()
        self.updateScene([self.sceneRect()])
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        pos = self.mapToScene(event.localPos().toPoint())
        x = int(pos.x())
        y = int(pos.y())
        if self.status == 'translate' and self.selected_id != '':
            item = self.item_dict[self.selected_id]
            if self.oldX and self.oldY:
                item.p_list = alg.translate(item.p_list, x - self.oldX, y - self.oldY)
            self.oldX = x
            self.oldY = y
        elif self.status == 'rotate' and self.selected_id != '':
            item = self.item_dict[self.selected_id]
            # if item.item_type != 'text':
            v0 = [self.startX - self.cx,
                  self.startY - self.cy]
            v1 = [x - self.cx,
                  y - self.cy]
            r = np.math.atan2(np.linalg.det([v0, v1]), np.dot(v0, v1))
            r = np.degrees(r)
            # print(r)
            if item.item_type == "line":
                item.p_list = alg.rotate(self.temp_p_list, self.cx, self.cy, r)
            else:
                item.rotation = r
        elif self.status == 'scale' and self.selected_id != '':
            item = self.item_dict[self.selected_id]
            x0 = abs(self.startX - self.cx)
            y0 = abs(self.startY - self.cy)
            dx = abs(x - self.cx)
            dy = abs(y - self.cy)
            if x0 != 0 and y0 != 0:
                f = (dy + dx) / (y0 + x0)
                # print(f)
                item.p_list = alg.scale(self.temp_p_list, self.cx, self.cy, f)
        elif self.status == 'line':
            self.temp_item.p_list[1] = [x, y]
        elif self.status == 'text':
            self.temp_item.p_list[1] = [x, y]
        self.updateScene([self.sceneRect()])
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if self.status == 'line':
            self.item_dict[self.temp_id] = self.temp_item
            self.list_widget.addItem(self.temp_id)
            self.finish_draw()
        elif self.status == 'text':
            text, ok = QInputDialog.getText(self, '提示', '请输入文字：')
            if ok:
                self.temp_item.text = text
            [x0, y0] = self.temp_item.p_list[0]
            [x1, y1] = self.temp_item.p_list[1]
            min_font_size = 50
            min_height = min_font_size
            min_width = min_font_size * len(text)
            if x1 - x0 < min_width:
                self.temp_item.p_list[1][0] = x0 + min_width
            if y1 - y0 < min_height:
                self.temp_item.p_list[1][1] = y0 + min_height
            self.item_dict[self.temp_id] = self.temp_item
            self.list_widget.addItem(self.temp_id)
            self.finish_draw()
        super().mouseReleaseEvent(event)


class MyItem(QGraphicsItem):
    """
    自定义图元类，继承自QGraphicsItem
    """

    def __init__(self, item_id: str, item_type: str, p_list: list, parent: QGraphicsItem = None):
        """
        :param item_id: 图元ID
        :param item_type: 图元类型
        :param p_list: 图元参数
        :param parent:
        """
        super().__init__(parent)
        self.id = item_id
        self.item_type = item_type
        self.p_list = p_list
        self.rotation = 0
        self.selected = False
        self.text = ""
        rect = self.mapToScene(self.boundingRect()).boundingRect();
        self.center = rect.center()
        self.pen = QPen(Qt.red, 5)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = ...) -> None:
        painter.setPen(self.pen);
        x0, y0 = self.p_list[0]
        x1, y1 = self.p_list[1]
        if self.rotation != 0:
            center = QRectF(x0, y0, x1 - x0, y1 - y0).center()
            painter.translate(center)
            painter.rotate(self.rotation)
            painter.translate(-center)
        if self.item_type == 'line':
            painter.drawLine(x0, y0, x1, y1)
        elif self.item_type == 'text':
            x = min(x0, x1)
            y = min(y0, y1)
            w = max(x0, x1) - x
            h = max(y0, y1) - y
            font = painter.font()
            font.setPixelSize(min(w, h))
            painter.setFont(font)
            painter.drawText(QRectF(x, y, w, h), Qt.AlignCenter, self.text)
        elif self.item_type == 'image':
            image = QImage(self.text)
            painter.drawImage(QRectF(x0, y0, x1 - x0, y1 - y0), image)
        if self.selected:
            painter.setPen(QColor(255, 0, 0))
            painter.drawRect(self.boundingRect())

    def boundingRect(self) -> QRectF:
        x0, y0 = self.p_list[0]
        x1, y1 = self.p_list[1]
        x = min(x0, x1)
        y = min(y0, y1)
        w = max(x0, x1) - x
        h = max(y0, y1) - y
        return QRectF(x - 1, y - 1, w + 2, h + 2)


class MainWindow(QMainWindow):
    """
    主窗口类
    """

    def __init__(self):
        super().__init__()
        self.item_cnt = 0

        # 使用QListWidget来记录已有的图元，并用于选择图元。注：这是图元选择的简单实现方法，更好的实现是在画布中直接用鼠标选择图元
        self.list_widget = QListWidget(self)
        self.list_widget.setMinimumWidth(200)

        # 使用QGraphicsView作为画布
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 600, 600)
        self.canvas_widget = MyCanvas(self.scene, self)
        self.canvas_widget.setFixedSize(600, 600)
        self.canvas_widget.main_window = self
        self.canvas_widget.list_widget = self.list_widget

        # 设置菜单栏
        menubar = self.menuBar()
        file_menu = menubar.addMenu('文件')
        export_image_act = file_menu.addAction('导出图片')
        exit_act = file_menu.addAction('退出')
        draw_menu = menubar.addMenu('插入')
        image_act = draw_menu.addAction('图片')
        text_act = draw_menu.addAction('文字')
        line_act = draw_menu.addAction('线段')
        edit_menu = menubar.addMenu('编辑')
        translate_act = edit_menu.addAction('平移')
        rotate_act = edit_menu.addAction('旋转')
        scale_act = edit_menu.addAction('缩放')

        # 连接信号和槽函数
        exit_act.triggered.connect(qApp.quit)
        export_image_act.triggered.connect(self.export_image_action)
        image_act.triggered.connect(self.image_action)
        text_act.triggered.connect(self.text_action)
        line_act.triggered.connect(self.line_action)
        translate_act.triggered.connect(self.translate_action)
        rotate_act.triggered.connect(self.rotate_action)
        scale_act.triggered.connect(self.scale_action)
        self.list_widget.currentTextChanged.connect(self.canvas_widget.selection_changed)

        # 设置主窗口的布局
        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.canvas_widget)
        self.hbox_layout.addWidget(self.list_widget, stretch=1)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.hbox_layout)
        self.setCentralWidget(self.central_widget)
        self.statusBar().showMessage('空闲')
        self.resize(600, 600)
        self.setWindowTitle('图片编辑器')

    def get_id(self):
        _id = str(self.item_cnt)
        self.item_cnt += 1
        return _id

    def export_image_action(self):
        rect = QRectF(0, 0, 600, 600)
        image = QImage(600, 600, QImage.Format_RGB32)
        image.fill(Qt.GlobalColor.white)
        painter = QPainter(image)
        self.scene.render(painter, rect, rect)
        painter.end()
        image.save("export.jpg", format='jpeg')
        QMessageBox.information(self,
                                "提示",
                                "保存成功！",
                                QMessageBox.Yes)

    def image_action(self):
        self.canvas_widget.insert_image(self.get_id())
        self.statusBar().showMessage('插入图片')
        self.list_widget.clearSelection()
        self.canvas_widget.clear_selection()

    def text_action(self):
        self.canvas_widget.start_draw_text(self.get_id())
        self.statusBar().showMessage('插入文字')
        self.list_widget.clearSelection()
        self.canvas_widget.clear_selection()

    def line_action(self):
        self.canvas_widget.start_draw_line(self.get_id())
        self.statusBar().showMessage('插入线段')
        self.list_widget.clearSelection()
        self.canvas_widget.clear_selection()

    def check_selected(self):
        if self.canvas_widget.selected_id == '':
            QMessageBox.information(self,
                                    "错误",
                                    "请选择一个图元！",
                                    QMessageBox.Yes)
            return False
        else:
            return True

    def translate_action(self):
        if self.check_selected():
            self.canvas_widget.start_translate()
            self.statusBar().showMessage('平移')

    def rotate_action(self):
        if self.check_selected():
            self.canvas_widget.start_rotate()
            self.statusBar().showMessage('旋转')

    def scale_action(self):
        if self.check_selected():
            self.canvas_widget.start_scale()
            self.statusBar().showMessage('缩放')


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    e = app.exec_()
    if e == 773:
        restart_program()
    sys.exit(e)

