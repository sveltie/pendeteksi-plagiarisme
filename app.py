import sys
import fitz
import tkinter as tk
import os

from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

from os import listdir
from pathlib import Path
from utils import utils
from preprocessing import preprocessing
from model import model


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pendeteksi Plagiarisme Tugas")

        self.canvas = tk.Canvas(self, width=600, height=300)
        self.canvas.grid(columnspan=4, rowspan=4)


        self.instructions = tk.Label(self, text="PENDETEKSI PLAGIARISME", font=("Ubuntu", 17, "italic"))
        self.instructions.grid(columnspan=4, column=0, row=1, sticky='n')

        self.input_box = tk.Text(self, height=10, width=50, padx=15, pady=15, bg="white")
        self.input_box.tag_configure("center", justify="center")
        self.input_box.tag_add("center", 1.0, "end")
        self.input_box.grid(columnspan=4, column=0, row=3)

        self.upload_btn = tk.Button(self, text="Upload", command=lambda:self.open_file(), background="#d9d9d9")
        self.upload_btn.grid(column=0, row=5, columnspan=2, pady=5)

        self.check_btn = tk.Button(self, text="Check", command=lambda:self.btn_event(), background="#d9d9d9")
        self.check_btn.grid(column=1, row=5)

        self.result_label = tk.Label(self, text="Result:", font="Ubuntu", justify="left")
        self.result_label.grid(column=0, row=6)

        self.prediction_label = tk.Label(self, text="", font="Ubuntu", justify="left")
        self.prediction_label.grid(column=0, row=7)

        self.canvas = tk.Canvas(self, width=600, height=250)
        self.canvas.grid(columnspan=4)

    def btn_event(self):
        self.prediction_label["text"] = "Success"

    def open_file(self):
        ut = utils.Utils()
        pp = preprocessing.Preprocessing()
        md = model.Model()
        files = listdir('.\data')

        compare_list = []
        for file in files:
            compare_list.append(file)
        
        file = askopenfile(parent=self, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
        res = []
        if file:
            with fitz.open(file) as pdf:
                raw_text = ""
                for page in pdf:
                    raw_text += page.get_text()
            text = pp.filter_text(raw_text)
            for file_compare in compare_list:
                if file_compare != os.path.basename(file.name):
                    candidate = ut.load_file(file_compare)
                    score = md.jaccard_similiarity(text, candidate)
                    res.append([f'{os.path.basename(file.name)} {file_compare}', score])
                self.result_label["text"] = f'Indeks Jaccard: {res}'


if __name__ == "__main__":
    try:
        app = App()
        app.mainloop()
    except(ImportError,):
        print("Error while importing module")