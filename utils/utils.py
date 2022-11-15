import fitz

from os import path
from preprocessing import preprocessing


class Utils:
    def __init__(self):
        self.data_path = '.\data'
        self.pp = preprocessing.Preprocessing()

    def extract_pdf(self, file: str) -> list:
        """
        Extract the text from a PDF file.
        :param file: The path to the file.
        """
        data_path = self.data_path
        # To-Do: Fix WARNING (doesn't really cause errors)
        with fitz.open(f"{data_path}\\{file}") as pdf:
            raw_text = ""
            for page in pdf:
                raw_text += page.get_text()
        text = self.pp.filter_text(raw_text)
        return text

    def load_file(self, file: str) -> list:
        """
        Load and initialize the file.
        :param file: The path to the file.
        """

        file_extension = path.splitext(file)[1]
        if file_extension == ".pdf":
            return self.extract_pdf(file)
        else:
            print("Not supported")