# InstantEcho

> A fun Python utility that reads aloud your typed message, simulates sending it, and shows time-stamped alerts with clipboard support.

## 🌟 Overview

**InstantEcho** is a mini tool that mimics a message-sending experience. It asks you to input a message, reads it out loud using text-to-speech, copies it to the clipboard, and displays the sent and received timestamps in a pop-up alert.

No external chat apps or messaging APIs—just a standalone simulation for fun or prototyping!

## 🚀 Features

* 📝 Pop-up message input
* 🗋 Automatic clipboard copy
* 🕒 Timestamps for "sent" and "received"
* 🔊 Instant voice feedback with TTS
* 🪧 Clean message summary pop-up

## 🛠️ Technologies Used

* `pyautogui` – GUI alerts and prompts
* `pyttsx3` – Text-to-speech engine
* `pyperclip` – Clipboard access
* `time` – Timestamping

## ▶️ How to Run

### 1. Install the dependencies

```bash
pip install pyautogui pyttsx3 pyperclip
```

### 2. Run the script

```bash
python InstantEcho_gui.py
```

### 3. Follow the prompts

* Enter a message in the pop-up box
* Listen to it spoken aloud
* See message info in an alert box
* Message is auto-copied to your clipboard

## 📌 Use Cases

* Fun CLI-to-GUI interaction testing
* Text-to-speech demo
* Voice feedback for accessibility
* Quick simulated messaging UX

## 🡩‍💻 Author

Made with ❤️ by **Daksh Aggarwal**
[GitHub](https://github.com/Daksh-Aggarwal) • [LinkedIn](https://www.linkedin.com/in/dakshaggarwal7)

## 📄 License

This project is licensed under the MIT License.
