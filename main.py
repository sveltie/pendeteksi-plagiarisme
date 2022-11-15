import sys
import time
import itertools
import threading

from os import listdir
from utils import utils
from preprocessing import preprocessing
from model import model


def main() -> None:
    ut = utils.Utils()
    pp = preprocessing.Preprocessing()
    md = model.Model()
    files = listdir('.\data')

    file_input = 'sample.pdf'

    compare_list = []
    for file in files:
        if file != file_input:
            compare_list.append(file)

    for file in files:
        if file == file_input:
            for file_compare in compare_list:
                ext = ut.load_file(file)
                candidate = ut.load_file(file_compare)
                score = md.jaccard_similiarity(ext, candidate)
                print(score)


if __name__ == "__main__":
    main()