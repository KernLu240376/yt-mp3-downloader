# YouTube → MP3 Downloader Beta

A lightweight and stable YouTube to MP3 downloader built with Python. Simply enter a YouTube URL, click download, and the MP3 file is saved in your system's native Downloads folder.

---

## 🛠 Features

* Minimalistic GUI built with **Tkinter**
* Download YouTube videos as **MP3**
* Automatically names MP3 after the video title
* Saves files directly in the system's **Downloads folder**
* Real-time **progress bar**
* Checks if **FFmpeg** is installed
* Cross-platform: Windows, macOS, Linux

---

## ⚡ Installation

1. **Clone the repository or download ZIP**

```bash
git clone https://github.com/<your-username>/YT-MP3-Downloader.git
cd YT-MP3-Downloader
```

2. **Install Python**

* Python 3.10+ required
* Verify installation:

```bash
python --version
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Install FFmpeg**

* **Windows:** Download FFmpeg → extract → add `bin` folder to PATH
* **macOS:**

```bash
brew install ffmpeg
```

* **Linux (Ubuntu/Debian):**

```bash
sudo apt install ffmpeg -y
```

---

## 🚀 Usage

Run the program:

```bash
python downloader_beta.py
```

* Enter a **YouTube URL**
* Click **Download MP3**
* MP3 file will appear in the **Downloads folder**

---


## ⚖️ Legal Notice

* Only download content you are **allowed to use**.
* Respect copyright laws. Private use may be allowed in some countries.

---

## 🔧 Notes

* Progress bar may behave differently on very short videos or slow internet
* If you get `ffmpeg not found`, make sure FFmpeg is installed and in your PATH

---

## 🏷 Badges (optional)

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![GitHub](https://img.shields.io/badge/GitHub-Project-black)

---

## 👨‍💻 GitHub & Version Control

* `.gitignore` includes `downloads/` and `__pycache__/`
* Perfect for showcasing **Python and GUI skills** in your portfolio

---

## ✅ Done!

A clean, functional, beginner-friendly YouTube → MP3 downloader. Great for personal use or showcasing programming skills on GitHub.

