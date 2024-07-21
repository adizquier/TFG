import pyaudio
import numpy as np
from aubio import notes
from mido import Message, MetaMessage, MidiFile, MidiTrack, second2tick, bpm2tempo
import time
from scipy.signal import butter, lfilter

class aubioClass:
    def __init__(self):
        # Configuración de parámetros de audio
        self.buffer_size = 256  # Ajustado para coincidir con el tamaño esperado por notes_o
        self.pyaudio_format = pyaudio.paFloat32
        self.n_channels = 1
        self.samplerate = 44100

        # Inicialización de PyAudio
        self.p = None

        # Configuración de parámetros para el análisis de notas
        self.win_s = 512  # Tamaño de la ventana FFT
        self.hop_s = 256  # Tamaño del salto entre ventanas

        # Inicialización del objeto para el análisis de notas
        self.notes_o = notes("default", self.win_s, self.hop_s, self.samplerate)

        self.tolerance = 0.97
        self.warmup_iterations = 50

        self.last_vel = 0
        self.streamOpen = False
        self.stream = None
        self.tiempo = 0


    def check_conditions(self, new_note, intensity, diff):
        if intensity < 100:
            return False
        
        if new_note[1] < self.tolerance * 127:  # Aquí usamos la tolerancia para filtrar notas de baja intensidad
            return False
        
        if new_note[0] == new_note[2] and new_note[1] < self.last_vel-2:
            return False
        
        if diff < 200:
            return False
        
        if new_note[0] < 58 or new_note[0] > 84:
            return False

        return True
    
    def open_stream(self):
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.pyaudio_format,
                channels=self.n_channels,
                rate=self.samplerate,
                input=True,
                frames_per_buffer=self.buffer_size)
        
        self.streamOpen = True

    def close_stream(self):
        self.stream.stop_stream()
        self.stream.close()

        self.p.terminate()
        self.streamOpen = False

    def detect_note(self):
        if self.streamOpen == True:        
            self.tiempo = time.time() * 1000
  
            for _ in range(self.warmup_iterations):
                self.stream.read(self.buffer_size)

            while True:
                # Leer datos del stream de audio
                audiobuffer = self.stream.read(self.buffer_size)
                signal = np.frombuffer(audiobuffer, dtype=np.float32)

                # Calcular la energía de la señal
                intensity = np.sum(signal**2)

                # Realizar el análisis de notas
                new_note = self.notes_o(signal)

                if new_note[0] != 0:
                    
                    t = time.time() *1000
                    diff = int(t - self.tiempo)

                    if not self.check_conditions(new_note, intensity, diff): continue

                    self.tiempo = t
                    self.last_vel = new_note[1]

                    print("Nota MIDI: {}, Velocidad: {}, Intensidad (suavizada): {:.2f}, Duration Anterior: {}, Anterior {}".format(int(new_note[0]), new_note[1], intensity, diff, new_note[2]))

                    return new_note[0]