# Lector de partituras digital con IA #

En este proyecto se ha desarrollado una herramienta basada en métodos y modelos de inteligencia artificial para asistir a músicos durante sus interpretaciones. La herramienta se centrará en facilitar tareas que pueden resultar complicadas para algunos músicos, como el paso de páginas de una partitura usando un lector de partituras digital sin usar las manos. Mediante el uso e integración de técnicas que permitan resolver cuestiones como el **reconocimiento de gestos** o el **reconocimiento de notas musicales** para su posterior comparación con las notas de la partitura, la herramienta permitirá que la interpretación sea más fluida y accesible sin el uso de elementos adicionales como pedales.

In this project, a tool has been developed based on artificial intelligence methods and models to assist musicians during their performances. The tool focuses on facilitating tasks that can be challenging for some musicians, such as turning pages of a score using a digital sheet music reader without using their hands. By employing and integrating techniques that address issues such as **gesture recognition** or the **recognition of musical notes** for subsequent comparison with the notes on the score, the tool will allow for a smoother and more accessible performance without the need for additional elements like pedals.

## Guía de instalación ##
### 1. Instalación de instaladores de paquetes:
`sudo apt install python3-pip`
`sudo apt install flatpak`

### 2. Instalación de paquetes:
`pip install <paquete>`

Los paquetes a instalar son: PySide2, numpy, opencv-python, mido, PyMuPDF, Pillow, music21, pyaudio y aubio

### 3. Instalación de herramientas adiccionales:
`flatpak install flathub org.audiveris.audiveris`

Puede comprobarse su correcta instalación con: `flatpak run org.audiveris.audiveris`

`sudo apt install timidity`
