import Searcher
import Reader

filename = "Great_Gatsby_Full_Text.txt"
booktitle = "The Great Gatsby by F. Scott Fitzgerald"
words_to_search = [["jay", "gatsby"], "daisy", ["nick", "carraway"], "myrtle"]

words = Reader.ReadFile(filename)
Searcher.Multi_Chart(words, words_to_search, booktitle)
