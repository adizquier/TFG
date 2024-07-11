import cv2

class FaceDetector:
    """Clase para la detección de caras y perfiles utilizando clasificadores en cascada de OpenCV."""

    def __init__(self):
        """Inicializa los clasificadores de caras y perfiles y el facemark."""
        self.face_cascade = cv2.CascadeClassifier("/usr/share/opencv4/haarcascades/haarcascade_frontalface_alt.xml")
        self.profile_cascade = cv2.CascadeClassifier("/usr/share/opencv4/haarcascades/haarcascade_profileface.xml")

        # Verificar si los clasificadores se han cargado correctamente
        if self.face_cascade.empty() or self.profile_cascade.empty():
            raise IOError("No se pudo cargar uno o más clasificadores en cascada")

        self.facemark = cv2.face.createFacemarkLBF()
        self.facemark.loadModel('./lbfmodel.yaml')

    def draw_detection(self, detection, dest_image):
        if(detection is not None):
            x, y, w, h = detection
            color = (0, 255, 255)
            stroke = 5
            cv2.rectangle(dest_image, (x, y), (x + w, y + h), color, stroke)

    def select_biggest_detection(self, detections):
        maxArea = 0
        biggest = None

        for(x, y, w, h) in detections:
            if w*h > maxArea:
                maxArea = w*h
                biggest = (x, y, w, h)

        return biggest



    def cascade_profiles_detector(self, gray_image):
        """
        Detecta perfiles en una imagen en escala de grises y dibuja rectángulos alrededor de los perfiles encontrados.

        Parameters:
        gray_image (numpy.ndarray): Imagen en escala de grises donde se detectarán los perfiles.
        dest_color_image (numpy.ndarray): Imagen en color donde se dibujarán los rectángulos alrededor de los perfiles detectados.
        """
        #cv2.equalizeHist(gray_image, gray_image)

        # Detectar perfiles izquierdos
        left_profiles = self.profile_cascade.detectMultiScale(
            gray_image, 
            scaleFactor=1.20, 
            minNeighbors=8, 
            minSize=(50, 50), 
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        if len(left_profiles) > 0: return (0, self.select_biggest_detection(left_profiles))

        #self.draw_detection(self.select_biggest_detection(left_profiles), dest_color_image)

        # Detectar perfiles derechos
        gray_invert = cv2.flip(gray_image, 1)
        right_profiles = self.profile_cascade.detectMultiScale(
            gray_invert, 
            scaleFactor=1.20, 
            minNeighbors=8, 
            minSize=(50, 50), 
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        if len(right_profiles) > 0: return (1, self.select_biggest_detection(right_profiles))

        return None

        #self.draw_detection(self.select_biggest_detection(right_profiles), dest_color_image)


    def facemark_detector(self, grayImage, destColorImage):
        faces = self.face_cascade.detectMultiScale(grayImage, 1.1, 4)
        if len(faces) == 0: return

        success, landmarks = self.facemark.fit(grayImage, faces)

        if success:
            for f in range(len(landmarks)):
                cv2.face.drawFacemarks(destColorImage, landmarks[f])

    