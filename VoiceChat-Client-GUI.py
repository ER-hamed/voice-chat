import socket
from _thread import start_new_thread
import pyaudio
from tkinter import Tk, Button, messagebox


class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.top = Tk()
        self.button = Button(command=lambda: self.microphone())
        self.host = '176.97.218.224'
        self.port = 9999
        self.buffer = 512
        self.rate = 10000
        self.enable = True
        self.audio = pyaudio.PyAudio()
        self.playing_stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=self.rate, output=True,
                                              frames_per_buffer=self.buffer)
        self.recording_stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=self.rate, input=True,
                                                frames_per_buffer=self.buffer)

    def start(self):
        try:
            self.socket.connect((self.host, self.port))
        except Exception as e:
            messagebox.showerror(title='Error', message=str(e))
            exit()

        self.top.geometry('400x400')
        self.top.resizable(False, False)
        self.top.title('Voice Chat - Connected')
        self.button.place(x=50, y=100, width=300, height=200)
        self.button.configure(text='Microphone On', font=('times', 30), bg='#005500')

        start_new_thread(self.receive, ())
        start_new_thread(self.send, ())
        self.top.mainloop()

    def receive(self):
        while True:
            try:
                data = self.socket.recv(self.buffer)
                if data == ''.encode():
                    self.close('Receive None')
                self.playing_stream.write(data)
            except socket.error as e:
                self.close('Error: ' + str(e))

    def send(self):
        while True:
            try:
                data = self.recording_stream.read(self.buffer)
                if data == ''.encode():
                    pass
                elif not self.enable:
                    pass
                else:
                    self.socket.send(data)
            except socket.error as e:
                self.close('Error: ' + str(e))
            except KeyboardInterrupt:
                self.close('End')

    def microphone(self):
        if self.enable:
            self.enable = False
            self.button.configure(text='Microphone Off', bg='#550000')
        else:
            self.enable = True
            self.button.configure(text='Microphone On', bg='#005500')

    def close(self, e):
        print(e)
        self.socket.close()
        self.playing_stream.close()
        self.recording_stream.close()
        self.top.destroy()
        exit()


client = Client()
client.start()
