import Searcher
import Reader

filename = "Candide_Full_Text.txt"
booktitle = "Candide by Voltaire"
words_to_search = ["candide", "pangloss", "cunegonde", "cacambo", "martin"]

words = Reader.ReadFile(filename)
Searcher.Multi_Chart(words, words_to_search, booktitle)
