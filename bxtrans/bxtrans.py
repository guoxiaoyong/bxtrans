# Author: Guo Xiaoyong

import time

import tkinter as tk
from googletrans import Translator


def _translate(text):
    translator = Translator()
    text_en = translator.translate(text).text
    return text_en


def translate(text):
    text_list = text.split('\n')
    res = []
    for line in text_list:
        line_en = _translate(line)
        res.append(line_en)
    time.sleep(1)
    return '\n'.join(res)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.button = None
        self.text = {'cn': None, 'en': None}
        self['bg'] = 'azure2'
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self)
        self.button['text'] = 'translate'
        self.button['command'] = self.translate
        self.button.pack()
        self.text['cn'] = tk.Text(self, relief=tk.GROOVE, bg='ivory2')
        self.text['en'] = tk.Text(self, relief=tk.GROOVE, bg='PaleGreen1')
        self.text['cn'].pack(side=tk.LEFT)
        self.text['en'].pack(side=tk.RIGHT)

    def translate(self):
        text = self.text['cn'].get("1.0", tk.END)
        text_en = translate(text)
        self.text['en'].insert("1.0", text_en)


def main():
    root = tk.Tk()
    root.title('Chinese -> English')
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
