import Searcher
import Reader

filename = "Stranger_Full_Text copy.txt"
booktitle = "The Stranger by Albert Camus"
words_to_search = ["stranger", "man", "thing", "life", ["kill", "murder"], "strange"]

words = Reader.ReadFile(filename)
Searcher.Multi_Chart(words, words_to_search, booktitle, " or ")
