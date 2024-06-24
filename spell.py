import numpy as np
import streamlit as st


class DictionaryHandler:
    def __init__(self):
        self.dictionary = set()


    def load_dictionary(self, file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    word = line.strip()
                    self.dictionary.add(word)
        except IOError as e:
            raise RuntimeError(f"Cannot open dictionary file: {file_path}")


    def is_word_in_dictionary(self, word):
        return word in self.dictionary


    def get_dictionary_words(self):
        return list(self.dictionary)


class TextPreprocessor:
    def preprocess(self, text):
        clean = text.lower()
        clean = ''.join(char for char in clean if char.isalnum() or char.isspace())
        return clean.split()


class StringEdit:
    def calculate(self, str1, str2):
        len1, len2 = len(str1), len(str2)
        dp = np.zeros((len1 + 1, len2 + 1), dtype=int)


        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[len1][len2]


class Correction:
    def __init__(self, dictionary_handler):
        self.dictionary_handler = dictionary_handler
        self.string_edit = StringEdit()


    def suggest_correction(self, word):
        min_distance = float('inf')
        best_match = None


        for dict_word in self.dictionary_handler.get_dictionary_words():
            distance = self.string_edit.calculate(word, dict_word)
            if distance < min_distance:
                min_distance = distance
                best_match = dict_word


        return best_match

dictionary_handler = DictionaryHandler()
dictionary_handler.load_dictionary('dictionary.txt')


text_preprocessor = TextPreprocessor()
correction = Correction(dictionary_handler)


def check_spelling(text):
    words = text_preprocessor.preprocess(text)
    results = []


    for word in words:
        if not dictionary_handler.is_word_in_dictionary(word):
            suggestion = correction.suggest_correction(word)
            results.append((word, suggestion))


    return results
