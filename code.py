import tkinter as tk
import time

root = tk.Tk()
root.title("Vanish")
root.geometry("800x600")
root.configure(bg="#1b272e")

timer_label = tk.Label(root, text="5s", font=("Arial", 24), fg="#E4E7EC", bg="#1b272e")
timer_label.pack(pady=20)

word_count_label = tk.Label(root, text="Words: 0", font=("Arial", 12), fg="#8B93A7", bg="#1b272e")
word_count_label.pack(pady=(0, 10))

text_box = tk.Text(root, font=("Arial", 14), fg="#E4E7EC", bg="#30505A", wrap="word", insertbackground="#FFFFFF", relief="flat", padx=20, pady=20)
text_box.pack(expand=True, fill="both", padx=40, pady=20)

last_keystroke_time = time.time()

def on_key_release(event):
    global last_keystroke_time
    last_keystroke_time = time.time()

    current_text = text_box.get("1.0", "end-1c")
    word_count = len(current_text.split())
    word_count_label.config(text=f"Words: {word_count}")
    # print(f"Last keystroke updated: {last_keystroke_time}")

def update_timer():
    global last_keystroke_time

    time_since_last_keystroke = time.time() - last_keystroke_time
    time_remaining = 6 - time_since_last_keystroke

    if time_remaining <= 0:
        timer_label.config(text="0s", fg="#E4677A")
        text_box.delete("1.0", "end")
        word_count_label.config(text="Words: 0")
        flash_box()
        last_keystroke_time = time.time()
    elif time_remaining <=2:
        timer_label.config(text=f"{int(time_remaining)}s", fg="#E4677A")
    else:
        timer_label.config(text=f"{int(time_remaining)}s", fg="#E4E7EC")

    root.after(200, update_timer)

def flash_box():
    text_box.config(bg="#E4677A", state="disabled")
    root.after(150, restore_box)

def restore_box():
    text_box.config(bg="#30505A", state="normal")
    text_box.focus_set()

text_box.bind("<KeyRelease>", on_key_release)

update_timer()

root.mainloop()
