from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
from langdetect import detect
import os

# ---------------- WINDOW ----------------

root = Tk()
root.title(" Language Translation Tool")
root.geometry("700x900")
root.config(bg="#e6f2ff")

# ---------------- LANGUAGES ----------------

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

# ---------------- FUNCTIONS ----------------

def translate_text():

    try:
        text = input_text.get("1.0", END).strip()

        if text == "":
            messagebox.showwarning(
                "Warning",
                "Please enter the text to translate"
            )
            return

        selected_source = languages[source_combo.get()]
        selected_target = languages[target_combo.get()]

        # Detect Language
        detected_lang = detect(text)

        # Validate Source Language
        if detected_lang != selected_source:

            messagebox.showerror(
                "Language Error",
                f"Selected source language does not match input text.\n\nDetected Language: {detected_lang}"
            )

            return

        # Translation API
        translated = GoogleTranslator(
            source=selected_source,
            target=selected_target
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

        status_label.config(
            text="Translation Successful ✅",
            fg="green"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            f"Something went wrong\n\n{e}"
        )


def copy_text():

    try:
        translated = output_text.get("1.0", END).strip()

        if translated == "":
            messagebox.showwarning(
                "Warning",
                "Nothing to copy"
            )
            return

        root.clipboard_clear()
        root.clipboard_append(translated)

        status_label.config(
            text="Copied to Clipboard ✅",
            fg="blue"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


def speak_text():

    try:
        translated = output_text.get("1.0", END).strip()

        if translated == "":
            messagebox.showwarning(
                "Warning",
                "No translated text available"
            )
            return

        target_lang = languages[target_combo.get()]

        tts = gTTS(
            text=translated,
            lang=target_lang
        )

        tts.save("voice.mp3")

        playsound("voice.mp3")

        os.remove("voice.mp3")

        status_label.config(
            text="Voice Played Successfully 🔊",
            fg="purple"
        )

    except Exception as e:

        messagebox.showerror(
            "Voice Error",
            str(e)
        )


def clear_text():

    input_text.delete("1.0", END)
    output_text.delete("1.0", END)

    status_label.config(
        text="Cleared ✅",
        fg="red"
    )

# ---------------- TITLE ----------------

title = Label(
    root,
    text="🌍 Language Translation Tool",
    font=("Segoe UI", 22, "bold"),
    bg="#e6f2ff",
    fg="darkblue"
)

title.pack(pady=10)

# ---------------- INPUT LABEL ----------------

input_label = Label(
    root,
    text="Enter Text",
    font=("Segoe UI", 14),
    bg="#e6f2ff"
)

input_label.pack()

# ---------------- INPUT BOX ----------------

input_text = Text(
    root,
    height=4,
    width=55,
    font=("Segoe UI", 13)
)

input_text.pack(pady=10)

# ---------------- SOURCE LANGUAGE ----------------

source_label = Label(
    root,
    text="Source Language",
    font=("Segoe UI", 13),
    bg="#e6f2ff"
)

source_label.pack()

source_combo = ttk.Combobox(
    root,
    values=list(languages.keys()),
    font=("Segoe UI", 12),
    state="readonly",
    width=20
)

source_combo.pack(pady=5)

source_combo.set("English")

# ---------------- TARGET LANGUAGE ----------------

target_label = Label(
    root,
    text="Target Language",
    font=("Segoe UI", 13),
    bg="#e6f2ff"
)

target_label.pack()

target_combo = ttk.Combobox(
    root,
    values=list(languages.keys()),
    font=("Segoe UI", 12),
    state="readonly",
    width=20
)

target_combo.pack(pady=5)

target_combo.set("Telugu")

# ---------------- OUTPUT LABEL ----------------

output_label = Label(
    root,
    text="Translated Text",
    font=("Segoe UI", 14),
    bg="#e6f2ff"
)

output_label.pack(pady=10)

# ---------------- OUTPUT BOX ----------------

output_text = Text(
    root,
    height=4,
    width=55,
    font=("Segoe UI", 13)
)

output_text.pack(pady=10)

# ---------------- TRANSLATE BUTTON ----------------

translate_btn = Button(
    root,
    text="Translate",
    font=("Segoe UI", 13, "bold"),
    bg="green",
    fg="white",
    width=20,
    command=translate_text
)

translate_btn.pack(pady=10)

# ---------------- COPY BUTTON ----------------

copy_btn = Button(
    root,
    text="Copy Text",
    font=("Segoe UI", 13, "bold"),
    bg="blue",
    fg="white",
    width=20,
    command=copy_text
)

copy_btn.pack(pady=10)

# ---------------- SPEAK BUTTON ----------------

speak_btn = Button(
    root,
    text="Speak Translation 🔊",
    font=("Segoe UI", 13, "bold"),
    bg="purple",
    fg="white",
    width=20,
    command=speak_text
)

speak_btn.pack(pady=10)

# ---------------- CLEAR BUTTON ----------------

clear_btn = Button(
    root,
    text="Clear",
    font=("Segoe UI", 13, "bold"),
    bg="red",
    fg="white",
    width=20,
    command=clear_text
)

clear_btn.pack(pady=10)

# ---------------- STATUS LABEL ----------------

status_label = Label(
    root,
    text="",
    font=("Segoe UI", 11, "bold"),
    bg="#e6f2ff"
)

status_label.pack(pady=10)

# ---------------- FOOTER ----------------

footer = Label(
    root,
    text="Developed by Revathi",
    font=("Segoe UI", 10, "italic"),
    bg="#e6f2ff",
    fg="gray"
)

footer.pack(side=BOTTOM, pady=10)

# ---------------- RUN ----------------

root.mainloop()