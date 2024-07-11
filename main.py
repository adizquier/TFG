from PySide2 import QtGui, QtWidgets, QtCore
import numpy as np
import cv2
from mainwindow import Ui_MainWindow
from PySide2.QtCore import QPoint
import fitz as pdf
from PySide2.QtWidgets import QFileDialog
import faceDetector as fd
import time




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.cap = cv2.VideoCapture(0)
        self.colorImage = np.zeros((self.imageFrame.size().width(), self.imageFrame.size().height(),3), dtype = np.uint8)
        self.grayImage = np.zeros((self.imageFrame.size().width(), self.imageFrame.size().height()), dtype = np.uint8)
        
        self.imageVisor = np.zeros((self.imageFrame.size().width(), self.imageFrame.size().height(),3), dtype = np.uint8)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.compute)
        self.timer.start(30)

        self.detector = fd.FaceDetector()

        self.pdf = None
        self.pdfloaded = False

        self.paginas_pdf = []
        self.pagina_actual = 0

        self.detections = {}

        self.spinBox.setVisible(False)

        self.xButtom.setIcon(QtGui.QIcon("./iconos/x_icon.png"))
        self.xButtom.setVisible(False)
        
        self.right_buttom.setIcon(QtGui.QIcon("./iconos/right_icon.png"))
        self.right_buttom.setVisible(False)

        self.left_buttom.setIcon(QtGui.QIcon("./iconos/left_icon.png"))
        self.left_buttom.setVisible(False)

        self.edit_buttom.setIcon(QtGui.QIcon("./iconos/edit_icon.png"))
        self.edit_buttom.setVisible(False)

        self.text_buttom.setIcon(QtGui.QIcon("./iconos/text_icon.png"))
        self.text_buttom.setVisible(False)

        self.captureButton.clicked.connect(self.start_stop_capture)
        self.useCameraButtom.clicked.connect(self.use_camera)
        self.detect_buttom.clicked.connect(self.change_text_detectButtom)
        self.pdf_buttom.clicked.connect(self.loadPDF)
        self.spinBox.valueChanged.connect(self.select_pdf_page)
        self.xButtom.clicked.connect(self.x_buttom_clicked)
        self.right_buttom.clicked.connect(self.slide_right)
        self.left_buttom.clicked.connect(self.slide_left)

    def start_stop_capture(self, detect):
        if detect:
            self.captureButton.setText("Stop capture")
        else:
            self.captureButton.setText("Start Capture")

    def use_camera(self, color):
        if color:
            self.useCameraButtom.setText("Using camera")
        else:
            self.useCameraButtom.setText("Use camera")

    def change_text_detectButtom(self, detect):
        if detect:
            self.detect_buttom.setText("Stop detection")
        else:
            self.detect_buttom.setText("Detect face")


    def active_desactive_buttoms(self, flag, buttoms):
        for bt in buttoms:
            bt.setEnabled(flag)
            bt.setVisible(flag)

    def select_pdf_page(self):
        if self.pdfloaded:
            self.pagina_actual = self.spinBox.value() - 1


    def x_buttom_clicked(self):

        self.active_desactive_buttoms(False, (self.xButtom, self.spinBox, self.left_buttom, self.right_buttom, self.edit_buttom, self.text_buttom))

        self.pdf = None
        self.paginas_pdf = []
        self.pdfloaded = False
        self.pagina_actual = 0

    def slide_left(self):
        if self.pdfloaded:
            self.pagina_actual = (self.pagina_actual-1)%len(self.paginas_pdf)
            self.spinBox.setValue(self.pagina_actual + 1)

    def slide_right(self):
        if self.pdfloaded:
            self.pagina_actual = (self.pagina_actual+1)%len(self.paginas_pdf)
            self.spinBox.setValue(self.pagina_actual + 1)
    
    def compute(self):

        ret, capImage = self.cap.read()
 
        if ret and self.captureButton.isChecked():
            self.colorImage = cv2.resize(capImage, (self.imageFrame.size().width(), self.imageFrame.size().height()))
            self.imageVisor = cv2.resize(self.imageVisor, (self.imageFrame.size().width(), self.imageFrame.size().height()))

            self.colorImage = cv2.cvtColor(self.colorImage, cv2.COLOR_BGR2RGB)
            np.copyto(self.imageVisor, self.colorImage)
            self.grayImage = cv2.cvtColor(self.colorImage, cv2.COLOR_BGR2GRAY)

        #self.profile_detector()
        if self.pdfloaded and self.detect_buttom.isChecked():
            self.pass_with_face()

        self.update()


    def select_image_visor(self):
    
        if self.useCameraButtom.isChecked():

            self.active_desactive_buttoms(False, (self.spinBox, self.xButtom, self.right_buttom, self.left_buttom, self.edit_buttom, self.text_buttom))

            return self.imageVisor
        
        else:
            if self.pdfloaded is True:

                self.active_desactive_buttoms(True, (self.spinBox, self.xButtom, self.right_buttom, self.left_buttom, self.edit_buttom, self.text_buttom))

                return self.paginas_pdf[self.pagina_actual]

    
        return None


    def paintEvent(self, e):
        qp = QtGui.QPainter(self)        

        imagen = self.select_image_visor()
        
        if imagen is not None:
            w = (self.imageFrame.size().width()//4)*4 if self.useCameraButtom.isChecked() else (self.imageFrame.size().width()//8)*4
            h = self.imageFrame.size().height()
            cvImage = cv2.resize(imagen, (w,h))

            if len(imagen.shape) == 2:
                qImg = QtGui.QImage(cvImage,w, h,QtGui.QImage.Format_Grayscale8)
            else:
                qImg = QtGui.QImage(cvImage,w, h,QtGui.QImage.Format_RGB888)

            if self.useCameraButtom.isChecked():
                qp.drawImage(self.imageFrame.pos(), qImg)
            else:
                pos = self.imageFrame.pos()
                new_pos = QPoint(pos.x() + self.imageFrame.size().width()//2 - w//2, pos.y())
                qp.drawImage(new_pos, qImg)
            
        qp.end()

    def profile_detector(self):
        if self.detect_buttom.isChecked():
            self.detector.cascade_profiles_detector(self.grayImage, self.imageVisor)        
            
    def facemark_detector(self):
        if self.detect_buttom.isChecked():
            self.detector.facemark_detector(self.grayImage, self.imageVisor)

    def check_conditions(self, detecciones):
        tiempos = list(detecciones.keys())
        diff = (tiempos[-1] - tiempos[0]) * 1000

        if diff > 200 and diff < 800:
            return True
        
        return False
    
    def pass_with_face(self):
        
        prof_detection = self.detector.cascade_profiles_detector(self.grayImage)

        if prof_detection is not None:
            tipo, detection = prof_detection
            self.detector.draw_detection(detection, self.imageVisor)
            hora = time.time()
            self.detections[hora] = (tipo, detection)
        else:
            if len(self.detections) != 0:
                if(self.check_conditions(self.detections)):
                    det = list(self.detections.values())
                    tipo, _ = det[0]

                    if tipo == 0:
                        self.slide_right()
                    if tipo == 1:
                        self.slide_left()

                self.detections.clear()
        

    def getPDFinformation(self):

        for page in self.pdf:
            pix = page.get_pixmap()
            img_array = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)

            self.paginas_pdf.append(img_array)

    def loadPDF(self):
        self.timer.timeout.disconnect(self.compute)

        rutaPDF, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)")
        self.pdf = pdf.open(rutaPDF)

        if self.pdf is not None:
            self.getPDFinformation()

            self.pdfloaded = True

            self.active_desactive_buttoms(True, (self.spinBox, self.xButtom, self.left_buttom, self.right_buttom, self.edit_buttom, self.text_buttom))

            self.spinBox.setRange(1, len(self.paginas_pdf))
            

        self.timer.timeout.connect(self.compute)

  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
