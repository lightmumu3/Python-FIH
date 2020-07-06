# -*- coding: utf-8 -*-
import socket
import threading
from GUI_Settings import *
import stopThreading
import sys

class TCPSocket(GUI_Settings):
    def __init__(self,parent=None):
        super(TCPSocket,self).__init__(parent)
        self.tcp_socket = None
        self.client_th = None
        self.link = False  # 用于标记是否开启了连接

    def tcp_client_start(self):
        """
        功能函数，TCP客户端连接其他服务端的方法
        :return:
        """
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            print("tcp_ip:"+globalVal.global_tcp_ip)
            address = (str(globalVal.global_tcp_ip), int(globalVal.global_tcp_port))
        except Exception as ret:
            msg = '请检查目标IP，目标端口\n'
            self.statusBar().showMessage(msg)
            print(ret)
            output_log_message(msg+" "+ret)
            self.signal_write_msg.emit(msg)
        else:
            try:
                msg = '正在连接目标服务器\n'
                self.statusBar().showMessage(msg)
                print(msg)
                output_log_message(msg)
                self.signal_write_msg.emit(msg)
                self.tcp_socket.connect(address)
                self.link = False

            except Exception as ret:
                msg = '无法连接目标服务器\n'
                self.statusBar().showMessage(msg)
                output_log_message(msg+" "+str(ret))
                print(ret)
                self.signal_write_msg.emit(msg)
                self.link = False

            else:
                self.client_th = threading.Thread(target=self.tcp_client_concurrency, args=(address,))
                self.client_th.start()
                msg = 'TCP客户端已连接IP:%s端口:%s\n' % address
                self.statusBar().showMessage(msg)
                output_log_message(msg)
                self.link = True
                self.signal_write_msg.emit(msg)

    def tcp_client_concurrency(self, address):
        """
        功能函数，用于TCP客户端创建子线程的方法，阻塞式接收
        :return:
        """
        while True:
            recv_msg = self.tcp_socket.recv(1024)
            if recv_msg:
                msg = recv_msg.decode('utf-8')
                print_msg = '来自IP:{}端口:{}:\n{}\n'.format(address[0], address[1], msg)
                output_log_message(print_msg)
                # print(print_msg)
                self.signal_write_msg.emit(msg)
            else:
                self.tcp_socket.close()
                self.reset()
                msg = '从服务器断开连接\n'
                self.statusBar().showMessage(msg)
                output_log_message(msg)
                self.signal_write_msg.emit(msg)
                self.link = False
                break

    def tcp_send(self,send_data):
        """
        功能函数，用于TCP服务端和TCP客户端发送消息
        :return: None
        """
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.statusBar().showMessage(msg)
            self.signal_write_msg.emit(msg)
        else:
            try:
                # print(send_data)
                ver = sys.version
                if ver.find('2.7') == 0:
                    if isinstance(send_data,unicode):
                        send_data = send_data.decode("utf-8")
                else:
                    send_data = (str(send_data)).encode('utf-8')
                send_msg = send_data
                self.tcp_socket.send(send_msg)
                msg = 'TCP客户端已发送\n'
                output_log_message(msg)
                self.signal_write_msg.emit(msg)

            except Exception as ret:
                print(ret)
                msg = '发送失败\n'
                self.statusBar().showMessage(msg)
                output_log_message(msg+"  "+ret)
                self.signal_write_msg.emit(msg)

    def tcp_close(self):
        """
        功能函数，关闭网络连接的方法
        :return:
        """
        try:
            self.tcp_socket.close()
            if self.link is True:
                msg = '已断开网络\n'
                self.statusBar().showMessage(msg)
                output_log_message(msg)
                self.signal_write_msg.emit(msg)
        except Exception as ret:
            pass
        try:
            stopThreading.stop_thread(self.client_th)
        except Exception:
            pass
