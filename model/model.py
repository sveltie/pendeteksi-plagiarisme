import sys
import math
import difflib

from os import listdir
from pathlib import Path

class Model:
    def jaccard_similiarity(self, text_token1: list, text_token2: list) -> float:
        """Jaccard Index"""
        set_a = set(text_token1)
        set_b = set(text_token2)
        set_inter = set_a.intersection(set_b)
        set_union = set_a.union(set_b)
        dist_weight = float(len(set_inter)) / float(len(set_union)) * 100
        return dist_weight

    def overlap_similiarity(self, text_token1: list, text_token2: list) -> float:
        """Calculate the overlap score between two given lists"""
        seq = difflib.SequenceMatcher(a=text_token1, b=text_token2)
        overlap_weight = seq.ratio() * 100
        return overlap_weight