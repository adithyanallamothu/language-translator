from tkinter import *
from deep_translator import GoogleTranslator


def translate_text():

    text = input_text.get("1.0", END)

    target_language = language_var.get()

    translated = GoogleTranslator(source='auto', target=target_language).translate(text)

    output_text.delete("1.0", END)

    output_text.insert(END, translated)


root = Tk()

root.title("Language Translator")

root.geometry("500x400")


Label(root, text="Enter Text").pack()


input_text = Text(root, height=5)

input_text.pack()


Label(root, text="Target Language Code").pack()


language_var = StringVar()

language_var.set("te")

Entry(root, textvariable=language_var).pack()


Button(root, text="Translate", command=translate_text).pack(pady=10)

Label(root, text="Translated Text").pack()


output_text = Text(root, height=5)

output_text.pack()

root.mainloop()