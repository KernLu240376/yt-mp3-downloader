import tkinter as tk
from tkinter import ttk, messagebox
import yt_dlp
import threading
import os

def download_mp3():
    url = url_entry.get()
    if not url.strip():
        messagebox.showerror("Fehler", "Bitte YouTube-Link eingeben!")
        return

    def run():
        progress_var.set(0)
        download_button.config(state="disabled")
        status_label.config(text="Lade herunter...")

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join("downloads", "%(title)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "progress_hooks": [hook],
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            status_label.config(text="Download fertig ✅")
        except Exception as e:
            messagebox.showerror("Fehler", str(e))
            status_label.config(text="Fehler")
        finally:
            download_button.config(state="normal")

    threading.Thread(target=run).start()

def hook(d):
    if d['status'] == 'downloading':
        percent_str = d.get('_percent_str', '').strip().replace('%', '')
        if percent_str.replace('.', '', 1).isdigit():  # prüft ob Zahl
            percent = float(percent_str)
            progress_var.set(percent)
    elif d['status'] == 'finished':
        progress_var.set(100)


# GUI
root = tk.Tk()
root.title("YouTube → MP3 Downloader")
root.geometry("400x200")

tk.Label(root, text="YouTube-Link:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_mp3)
download_button.pack(pady=10)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, length=300)
progress_bar.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
