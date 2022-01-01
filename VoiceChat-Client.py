import logging
import socket
from _thread import start_new_thread
import pyaudio


class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '0.0.0.0'
        self.port = 9999
        self.chunk = 1024
        self.buffer = 2048
        self.rate = 20000
        self.audio = pyaudio.PyAudio()
        self.playing_stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=self.rate, output=True,
                                              frames_per_buffer=self.chunk)
        self.recording_stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=self.rate, input=True,
                                                frames_per_buffer=self.chunk)

    def start(self):
        try:
            self.socket.connect((self.host, self.port))
        except Exception as e:
            print('Error: ' + str(e))
            exit()
        start_new_thread(self.receive, ())
        self.send()

    def receive(self):
        while True:
            try:
                data = self.socket.recv(self.buffer)
                if data == ''.encode():
                    self.close('Error: data is None')
                else:
                    self.playing_stream.write(data)
            except socket.error as e:
                self.close('Error: ' + str(e))

    def send(self):
        while True:
            try:
                data = self.recording_stream.read(self.buffer)
                if data == ''.encode():
                    continue
                else:
                    self.socket.send(data)
            except socket.error as e:
                self.close('Error: ' + str(e))
            except KeyboardInterrupt:
                exit()

    def close(self, e):
        print(e)
        self.socket.close()
        exit()


client = Client()
client.start()
