import os
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import platform
import shutil
import sys

# --- yt-dlp importieren ---
try:
    import yt_dlp
except ImportError:
    messagebox.showerror("Missing Module", "yt-dlp is not installed.\nRun: pip install -U yt-dlp")
    sys.exit()

# ------------------------------
# FFmpeg Check
# ------------------------------
def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        messagebox.showerror("FFmpeg not found", "FFmpeg is not installed or not in PATH. MP3 conversion will fail.")
        return False
    return True

# ------------------------------
# Native Download-Ordner
# ------------------------------
def get_download_path():
    return os.path.join(os.path.expanduser("~"), "Downloads")

DOWNLOAD_FOLDER = get_download_path()

# ------------------------------
# Download Video als MP3
# ------------------------------
def download_video():
    if not check_ffmpeg():
        return

    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    def run_download():
        download_button.config(state="disabled")
        progress_var.set(0)
        status_label.config(text="Downloading...")

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "progress_hooks": [hook],
            "noplaylist": True
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            status_label.config(text=f"Download finished ✅\nSaved to {DOWNLOAD_FOLDER}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            status_label.config(text="Download failed")
        finally:
            download_button.config(state="normal")

    threading.Thread(target=run_download, daemon=True).start()

# ------------------------------
# Fortschrittsbalken
# ------------------------------
def hook(d):
    if d['status'] == 'downloading':
        percent_str = d.get('_percent_str', '').strip().replace('%', '')
        if percent_str.replace('.', '', 1).isdigit():
            progress_var.set(float(percent_str))
    elif d['status'] == 'finished':
        progress_var.set(100)

def update_progressbar():
    progress_bar.update()
    root.after(500, update_progressbar)

# ------------------------------
# GUI
# ------------------------------
root = tk.Tk()
root.title("YouTube → MP3 Downloader")
root.geometry("600x250")

# URL Eingabe
tk.Label(root, text="YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

# Download Button
download_button = tk.Button(root, text="Download MP3", command=download_video)
download_button.pack(pady=10)

# Fortschrittsbalken
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, length=500)
progress_bar.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="")
status_label.pack()

# Progressbar updater starten
update_progressbar()

root.mainloop()

