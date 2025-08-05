import tkinter as tk
from tkinter import messagebox, filedialog
from decrypt import brute_force_decrypt
from analysis import analyze_text


def read_encrypted_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def show_decrypted_text():
    encrypted_text = read_encrypted_file('encrypted.txt')
    shift, decrypted = brute_force_decrypt(encrypted_text)
    analyze_text(decrypted)  # אפשר לשמור את זה אם נרצה להרחיב בעתיד

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, f"Shift detected: {shift}\n\n{decrypted}")

    global decrypted_result
    decrypted_result = decrypted


def save_to_file():
    if not decrypted_result:
        messagebox.showwarning("Warning", "No decrypted text to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as f:
            f.write(decrypted_result)
        messagebox.showinfo("Success", "File saved successfully!")


def reencrypt_text():
    if not decrypted_result:
        messagebox.showwarning("Warning", "No decrypted text to re-encrypt.")
        return

    try:
        shift = int(shift_entry.get())
        if not 0 <= shift <= 25:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift (0-25).")
        return

    encrypted = ''
    for char in decrypted_result:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, f"Encrypted with shift {shift}:\n\n{encrypted}")

    shift_entry.delete(0, tk.END)


def show_bar_chart():
    if not decrypted_result:
        messagebox.showwarning("Warning", "Please decrypt the message first.")
        return

    words = decrypted_result.split()
    word_lengths = list(map(len, words))

    chart_window = tk.Toplevel(window)
    chart_window.title("Word Length Bar Chart")

    canvas_width = 600
    canvas_height = 300
    canvas = tk.Canvas(chart_window, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    max_height = max(word_lengths)
    bar_width = canvas_width // len(word_lengths)

    for i, length in enumerate(word_lengths):
        x0 = i * bar_width + 10
        y0 = canvas_height - (length / max_height * 200)
        x1 = x0 + bar_width - 20
        y1 = canvas_height - 10

        canvas.create_rectangle(x0, y0, x1, y1, fill="skyblue")
        canvas.create_text((x0 + x1) / 2, y1 + 10, text=str(length), anchor=tk.N)
        canvas.create_text((x0 + x1) / 2, canvas_height - 5, text=words[i], anchor=tk.S, font=("Arial", 8))


window = tk.Tk()
window.title("Secret Message Decryption")
window.geometry("600x500")

decrypt_button = tk.Button(window, text="Decrypt Message", command=show_decrypted_text)
decrypt_button.pack(pady=10)

text_output = tk.Text(window, height=15, width=70)
text_output.pack(pady=10)

save_button = tk.Button(window, text="Save to File", command=save_to_file)
save_button.pack(pady=5)

shift_frame = tk.Frame(window)
shift_frame.pack(pady=10)

tk.Label(shift_frame, text="New Shift:").pack(side=tk.LEFT, padx=5)
shift_entry = tk.Entry(shift_frame, width=5)
shift_entry.pack(side=tk.LEFT, padx=5)

reencrypt_button = tk.Button(shift_frame, text="Re-encrypt", command=reencrypt_text)
reencrypt_button.pack(side=tk.LEFT, padx=5)


chart_button = tk.Button(window, text="Show Word Length Chart", command=show_bar_chart)
chart_button.pack(pady=10)


decrypted_result = ""
window.mainloop()
