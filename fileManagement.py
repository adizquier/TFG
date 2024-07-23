import os
import mido
import fitz
import numpy as np
from PIL import Image
import shutil
import audiveris

BASE_DIR= os.path.expanduser("~/Documentos/")

IMAGES_DIR = BASE_DIR + "imagenesAuxiliar/"
XML_DIR = BASE_DIR + "archivosXML/"
MIDI_DIR = "./archivosMIDI/"

def getPDFinformation(rutaPDF, paginas_pdf):
    pdf = fitz.open(rutaPDF)

    for page in pdf:
        pix = page.get_pixmap()
        img_array = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)

        paginas_pdf.append(img_array)

    return pdf

def loadPDFpages(pdf, zoom_x=3.0, zoom_y=3.0):
    if os.path.exists(IMAGES_DIR):

        for i, page in enumerate(pdf):
            # Crear una matriz de transformación para ajustar la resolución (zoom)
            matrix = fitz.Matrix(zoom_x, zoom_y)
            
            # Renderizar la página con la matriz de zoom
            pix = page.get_pixmap(matrix=matrix)
            
            # Convertir el buffer de la imagen en un array de numpy
            img_array = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
            
            # Convertir el array de numpy a un objeto PIL Image
            img = Image.fromarray(img_array)
            
            # Guardar la imagen en la carpeta de salida
            img_path = os.path.join(IMAGES_DIR, f'page_{i}.png')
            img.save(img_path)

def createDir(directorio):
    if not os.path.exists(directorio):
        os.mkdir(directorio)

def deleteDir(directorio):
    if os.path.exists(directorio):
        shutil.rmtree(directorio)
    

def getMIDIpartiture(pdf, diccionarioMIDI):
    createDir(IMAGES_DIR)
    loadPDFpages(pdf)

    nombreArchivo = os.path.splitext(os.path.basename(pdf.name))[0]

    if len(os.listdir(IMAGES_DIR)) != 0:
        outputMIDI = MIDI_DIR + nombreArchivo + "/"

        createDir(XML_DIR)
        createDir(outputMIDI)

        for i, page in enumerate(sorted(os.listdir(IMAGES_DIR))):
            rutaPag = os.path.join(IMAGES_DIR, page)
   
            midi_page = audiveris.convert_pages_to_midi(rutaPag, XML_DIR, outputMIDI, os.path.splitext(page)[0])
            diccionarioMIDI[i] = midi_page


        deleteDir(XML_DIR)


    deleteDir(IMAGES_DIR)
    
