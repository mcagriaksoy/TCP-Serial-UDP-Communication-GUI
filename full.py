__author__ = 'Mehmet Cagri Aksoy - github.com/mcagriaksoy'

import binascii
import socket
import sys
import time
import warnings

import serial
import serial.tools.list_ports
from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QInputDialog, QLineEdit, QFileDialog, QTabWidget
from ui_qt import Ui_qt

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# port tespit etme - baslangic

ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'USB' or 'COM' in p.description
]

baudrate = [1200, 2400, 4800, 9600, 115200]

if not ports:
    raise IOError("Seri Baglantili cihaz yok!")

if len(ports) > 1:
    warnings.warn('Baglanildi....')

ser = serial.Serial(ports[0], baudrate[3])


# port tespit etme - son


class Worker(QObject):
    finished = Signal()
    intReady = Signal(str)

    def __init__(self):
        super(Worker, self).__init__()
        self.working = True

    def work(self):
        while self.working:
            line = ser.readline().decode('utf-8')
            # print(line)
            time.sleep(0.05)
            self.intReady.emit(line)
            # if line != '':
            # self.textEdit_3.append(line)

        self.finished.emit()


class Worker2(QObject):
    finished = Signal()
    intReady = Signal(str)

    def __init__(self):
        super(Worker2, self).__init__()
        self.working = True

    def work(self):
        while self.working:
            data, address = receiver.recvfrom(1024)
            print('received {} bytes from {}'.format(len(data), address))
            # time.sleep(0.05)
            data2 = data.decode('utf-8')
            self.intReady.emit(data2)
        self.finished.emit()


class Worker3(QObject):
    finished = Signal()
    intReady = Signal(str)

    def __init__(self):
        super(Worker3, self).__init__()
        self.working = True

    def work(self):
        # host = self.textEdit_10.toPlainText()
        # port_tcp = self.textEdit_12.toPlainText()
        host = socket.gethostname()
        s.connect(('127.0.0.1', 4448))  # Connect to server address


        while self.working:
            msg = s.recv(1024)
            print('data=%s', (msg))
            # f.write(msg)
            print("Message from server : " + msg.strip().decode('ascii'))
            msg2 = msg.decode('ascii')
            self.intReady.emit(msg2)
        self.finished.emit()


class Worker4(QObject):
    finished = Signal()
    intReady = Signal(str)

    def __init__(self):
        super(Worker4, self).__init__()
        self.working = True


    def work(self):
        server_address = ('127.0.0.1', 4448)
        print("connected:")
        s2.bind(server_address)
        s2.listen(1)

        print("Listening for connections.. ")

        while self.working:
            # f = open(a.txt, 'rb')
            # l = f.read(1024)
            # print(l)
            print("Bağlantılar Aranıyor...... ")
            q, addr = s2.accept()

            q.send(b"deneme")
            # print('Sent ', repr(l))

        self.finished.emit()


# port tespit etme - baslangic
class qt(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        # Setup UI from generated Python module and copy widget attributes onto self
        self.ui = Ui_qt()
        self.ui.setupUi(self)
        # copy attributes (widgets) from the Ui instance to this window for compatibility
        for name, val in self.ui.__dict__.items():
            if not name.startswith('__'):
                try:
                    setattr(self, name, val)
                except Exception:
                    pass

        self.thread = None
        self.worker = None
        self.thread2 = None
        self.thread3 = None
        self.thread4 = None
        self.pushButton.clicked.connect(self.start_loop)
        self.label_11.setText(ports[0])
        self.pushButton_6.clicked.connect(self.start_loop2)
        self.pushButton_9.clicked.connect(self.start_loop3)
        self.pushButton_38.clicked.connect(self.start_loop4)
        self.pushButton_17.clicked.connect(self.getOpenFileName)


    # def pushButton_17_clicked(self):
    #     getOpenFileName()

    def getOpenFileName(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        # self.trigger.connect(self.fileName)
        # self.trigger.emit(fileName)
        if fileName:
            self.label_26.setText(fileName)

    def on_pushButton_16_clicked(self):

        self.trigger.connect(self.work)
        self.trigger.emit(fileName)

    def loop_finished(self):
        print('Looped Finished')
        s.close()
        s2.close()

    def start_loop(self):

        self.worker = Worker()  # a new worker to perform those tasks
        self.thread = QThread()  # a new thread to run our background tasks in
        self.worker.moveToThread(
            self.thread)  # move the worker into the thread, do this first before connecting the signals

        self.thread.started.connect(self.worker.work)
        # begin our worker object's loop when the thread starts running

        self.worker.intReady.connect(self.onIntReady)

        self.pushButton_2.clicked.connect(self.stop_loop)  # stop the loop on the stop button click

        self.worker.finished.connect(self.loop_finished)  # do something in the gui when the worker loop ends
        self.worker.finished.connect(self.thread.quit)  # tell the thread it's time to stop running
        self.worker.finished.connect(self.worker.deleteLater)  # have worker mark itself for deletion
        self.thread.finished.connect(self.thread.deleteLater)  # have thread mark itself for deletion
        # make sure those last two are connected to themselves or you will get random crashes
        self.thread.start()

    def start_loop2(self):
        print("thread is started")
        self.worker = Worker2()  # a new worker to perform those tasks
        self.thread2 = QThread()  # a new thread to run our background tasks in
        self.worker.moveToThread(self.thread2)
        # move the worker into the thread, do this first before connecting the signals
        self.thread2.started.connect(self.worker.work)
        # begin our worker object's loop when the thread starts running
        self.worker.intReady.connect(self.onintready2)
        self.worker.finished.connect(self.loop_finished)  # do something in the gui when the worker loop ends
        self.pushButton_7.clicked.connect(self.stop_loop)  # stop the loop on the stop button click

        self.worker.finished.connect(self.thread2.quit)  # tell the thread it's time to stop running
        self.worker.finished.connect(self.worker.deleteLater)  # have worker mark itself for deletion
        self.thread2.finished.connect(self.thread2.deleteLater)  # have thread mark itself for deletion
        # make sure those last two are connected to themselves or you will get random crashes
        self.thread2.start()
        self.label_19.setText("Bağlantı Başarılı")
        self.label_19.setStyleSheet('color: green')

    def start_loop3(self):
        print("thread is started")
        self.worker = Worker3()  # a new worker to perform those tasks
        self.thread3 = QThread()  # a new thread to run our background tasks in
        self.worker.moveToThread(self.thread3)
        # move the worker into the thread, do this first before connecting the signals
        self.thread3.started.connect(self.worker.work)
        # begin our worker object's loop when the thread starts running
        self.worker.intReady.connect(self.onintready3)
        self.worker.finished.connect(self.loop_finished)  # do something in the gui when the worker loop ends
        self.pushButton_10.clicked.connect(self.stop_loop)  # stop the loop on the stop button click

        self.worker.finished.connect(self.thread3.quit)  # tell the thread it's time to stop running

        self.thread3.start()

    def start_loop4(self):
        print("thread is started")
        self.worker = Worker4()  # a new worker to perform those tasks
        self.thread4 = QThread()  # a new thread to run our background tasks in
        self.worker.moveToThread(self.thread4)
        self.label_27.setText("Bağlantı Başarılı")
        self.label_27.setStyleSheet('color: green')

        # move the worker into the thread, do this first before connecting the signals
        self.thread4.started.connect(self.worker.work)
        self.worker.intReady.connect(self.onintready4)
        # # begin our worker object's loop when the thread starts running
        # self.worker.fileName.connect(self.onintready4)
        self.worker.finished.connect(self.loop_finished)  # do something in the gui when the worker loop ends
        self.pushButton_39.clicked.connect(self.stop_loop)  # stop the loop on the stop button click

        self.worker.finished.connect(self.thread4.quit)  # tell the thread it's time to stop running
        self.worker.finished.connect(self.worker.deleteLater)  # have worker mark itself for deletion
        self.thread4.finished.connect(self.thread4.deleteLater)
        self.thread4.start()

    def on_pushButton_11_clicked(self):
        host = self.textEdit_10.toPlainText()
        port_tcp = self.textEdit_12.toPlainText()

    # def on_pushButton_13_clicked(self):

    #
    # global host2 = self.textEdit_38.toPlainText()
    # global port_tcp2 = self.textEdit_39.toPlainText()

    def onintready3(self, msg2):
        self.textEdit_3.append("{}".format(msg2))

    def onintready4(self,fileName):
        print('mmm')
        self.intReady.emit(fileName)

    def on_pushButton_3_clicked(self):
        mytext = self.textEdit_2.toPlainText()
        print(mytext)
        ser.write(mytext.encode())

    def on_pushButton_14_clicked(self):
        mytext = self.textEdit_2.toPlainText()

        mytext2 = binascii.unhexlify(mytext)

        ser.write(mytext2)

    def stop_loop(self):
        self.worker.working = False

    def onIntReady(self, i):
        self.textEdit_8.append("{}".format(i))

    def on_pushButton_4_clicked(self):
        self.textEdit.setText('Ayarlar Kaydedildi!')
        # else:
        #     # print('hata')
        #     self.textEdit.setText('Lütfen Port ve Hızı girin!')

        # TXT YAZDIRMA ------ KAYDETME

    def on_pushButton_5_clicked(self):
        with open('Sonuc.txt', 'w') as f:
            kaydet = self.textEdit_3.toPlainText()
            f.write(kaydet)

    def on_pushButton_2_clicked(self):
        self.textEdit.setText('Durduruldu! Yeniden Baglanmak icin BAGLAN-a basin...')

    def on_pushButton_clicked(self):

        self.completed = 0
        while self.completed < 100:
            self.completed += 0.001
            self.progressBar.setValue(self.completed)

        self.textEdit.setText('Veri Aliniyor...')

        # self.label_5.setText('OK!')

        self.label_5.setText("BAĞLANDI!")
        self.label_5.setStyleSheet('color: green')
        x = 1
        # self.textEdit_3.setText(":")

    # MULTI-THREADING

    def on_pushButton_8_clicked(self):

        self.completed2 = 0
        while self.completed2 < 100:
            self.completed2 += 0.001
            self.progressBar_2.setValue(self.completed2)

        mesaj = self.textEdit_6.toPlainText().encode('utf-8')
        # sock.sendto(mesaj, server_address)
        port = self.textEdit_7.toPlainText()
        ip = self.textEdit_11.toPlainText()
        sock.sendto(mesaj, (ip, int(port)))

    def on_pushButton_7_clicked(self):
        sock.close()
        self.textEdit_4.setText("Soket Kapatıldı...")

    def on_pushButton_6_clicked(self):
        port = self.textEdit_5.toPlainText()
        ip = self.textEdit_11.toPlainText()
        server_address = (ip, int(port))
        receiver.bind(server_address)

    def loop_finished(self):
        self.textEdit_4.setText("Durduruldu!")

    def onintready2(self, data2):
        self.textEdit_4.append("{}".format(data2))
        print(data2)

    def stop_loop(self):
        self.worker.working = False

    def on_pushButton_12_clicked(self):
        with open('Sonuc_UDP.txt', 'w') as f:
            kaydet = self.textEdit_6.toPlainText()
            f.write(kaydet)

    # TCP CLIENT:

    def on_pushButton_10_clicked(self):
        self.textEdit_3.setText("Baglanti Kapatildi")
        s.close()

    # TCP SERVER:
    def on_pushButton_37_clicked(self):
        self.completed2 = 0
        while self.completed2 < 100:
            self.completed2 += 0.001
            self.progressBar_10.setValue(self.completed2)

        data = self.textEdit_37.toPlainText()
        # q, addr = s2.accept()
        # time.sleep(0.1)
        # data.encode()
        # q.send(data)

    def on_pushButton_39_clicked(self):
        self.textEdit_40.setText("Baglanti Kapatildi")
        s2.close()


def run():
    app = QApplication(sys.argv)
    widget = qt()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()
