from pytube import *
from pathlib import Path
from tkinter import ttk


def downloadmp4(yt):
    if type(yt) == str:
        yt = YouTube(yt, use_oauth=True,allow_oauth_cache=True)
        path = Path.home() / "Desktop"
        
        stream = yt.streams.get_highest_resolution()
        stream.download(path)

def downloadmp3(yt):
    if type(yt) == str:
        yt = YouTube(yt, use_oauth=True,allow_oauth_cache=True)
        path = Path.home() / "Desktop"
        
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(path)
        
