import langid
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Preprocessing:
    def filter_stop_words(self, text: str) -> list:
        """
        Remove stop words.
        Only support EN and ID by classifying the text.
        :param text: The text to be filtered.
        """
        stop_words_en = set(stopwords.words("english"))
        stop_words_id = set(stopwords.words("indonesian")) 
        text_lang = langid.classify(text)[0]
        word_tokens = word_tokenize(text)
        if text_lang == "en":
            filtered_text = [w for w in word_tokens if not w in stop_words_en]
        else:
            filtered_text = [w for w in word_tokens if not w in stop_words_id]
        return filtered_text

    def filter_text(self, raw: str) -> list:
        """
        Remove punctuations and other stuffs from the text.
        :param raw: The raw data to be cleaned.
        """
        text = [raw]
        for i, _ in enumerate(text):
                text[i] = text[i].replace("\n", " ")
                text[i] = re.sub(r"[<(.|)*?/,->−+]", " ", str(text[i]))
                text[i] = re.sub(r"http://\S+|https://\S+", "", str(text[i]))
        text = " ".join(text)
        text = re.sub("(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)", "", text)
        text = self.filter_stop_words(text)
        return text