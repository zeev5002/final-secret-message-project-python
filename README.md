# 🕵️ Secret Message from the Spy

**Final project for the Python & Cryptography course.**  
A complete decryption tool with Caesar Cipher brute-force cracking, text analysis, and an interactive Tkinter GUI.

---

## 📜 Project Story

You are part of a team of agents who received an encrypted message from a spy.  
The message is encoded with an unknown Caesar cipher shift.  
Your mission: decrypt, analyze, and visualize the message.

---

## ✨ Features

- 🔓 Caesar Cipher brute-force decryption (auto-detects correct shift)
- 📊 Text analysis using 10+ built-in Python functions
- 💾 Save decrypted message to a file
- 🔁 Re-encrypt message with custom shift
- 📈 Bar chart of word lengths using Tkinter Canvas
- 🖥️ Friendly and clean GUI interface with Tkinter

---

## 🧠 Built-in Python Functions Used

- `len`, `max`, `min`, `set`, `sum`
- `map`, `zip`, `enumerate`
- `all`, `any`, `split`, `count`, `str.islower`, `sorted`

---

## 🧪 How to Run

1. Make sure you have **Python 3** installed.
2. Clone or download this repository.
3. Place your encrypted message in the file `encrypted.txt`.
4. Run the GUI:
   ```bash
   python gui.py
   ```
5. Use the GUI to decrypt and analyze the message.

---

## 📂 File Structure

```
├── analysis.py         # Text analysis functions
├── decrypt.py          # Caesar decryption logic
├── encrypted.txt       # Encrypted message file
├── gui.py              # Tkinter GUI interface
├── main.py             # Optional main entry point
├── README.md           # This file
├── .gitignore          # Virtual environment and IDE ignores
```

---

## ✅ Example Screenshot

*(You can upload one later in the repo)*

---

## 💡 Notes

- You can change the content of `encrypted.txt` to test different messages.
- The GUI allows you to re-encrypt messages with your own Caesar shift.

---

## 👨‍💻 Created by

Zeev5002 – for the final assignment in *Python & Cryptography* course.