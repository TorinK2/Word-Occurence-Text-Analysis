import Searcher
import Reader

filename = "Metamorphisis_Full_Text.txt"
booktitle = "The Metamorphisis by Franz Kafka"
words_to_search = ["gregor", "samsa", "man", "money", "work"]

words = Reader.ReadFile(filename)
Searcher.Multi_Chart(words, words_to_search, booktitle)
