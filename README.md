# ✍️ Vanish

**A "most dangerous writing app" clone — keep typing, or lose everything.**

Vanish is a minimalist Tkinter text editor with one brutal rule: if you stop typing for more than 6 seconds, every word you've written gets wiped instantly. Built to crush writer's block and force momentum, it's a race against a countdown timer that never stops ticking.

---

## ✨ Features

- ⏱️ **Live countdown timer** that resets with every keystroke
- 💀 **Text is permanently deleted** the moment the timer hits zero — no undo, no warning beyond the countdown itself
- 🔴 **Visual urgency cues** — the timer turns red in the final 2 seconds, and the text box flashes red the instant everything is erased
- 🔢 **Live word count**, updated as you type
- 🎨 Minimal dark-themed interface built to keep you focused on writing, not the UI

---

## 🛠️ Tech Stack

- **Python 3**
- **Tkinter** — GUI framework (window, text widget, labels, timing via `root.after`)
- **`time`** (standard library) — tracking elapsed time since the last keystroke

---

## 📁 Project Structure

```
vanish/
├── code.py          # Full app logic
└── README.md
```

---

## ▶️ Getting Started

### Prerequisites
- Python 3 (Tkinter ships with most standard Python installations, no extra installs needed)

### Running the App

```
git clone https://github.com/rhitamcoder/vanish.git
```
```
cd vanish
```
```
python code.py
```

Start typing in the text box. Keep going, if you pause for more than **6 seconds**, everything you've written disappears and the timer resets.

---

## 🧠 How It Works

- **`on_key_release()`** updates `last_keystroke_time` to the current time on every keystroke, and recalculates the live word count
- **`update_timer()`** runs on a repeating 200ms loop via `root.after()`, checking how much time has passed since the last keystroke
  - With more than 2 seconds remaining, the timer displays normally
  - In the final 2 seconds, the timer text turns red as a warning
  - At 0 seconds, the text box is cleared, the word count resets, and a red flash effect plays
- **`flash_box()` / `restore_box()`** briefly disable and recolor the text box to visually confirm the wipe, then restore it and return focus so you can start again immediately

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
