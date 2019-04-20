import matplotlib.pyplot as plt
from pylab import *
import numpy as np
import Reader

def Search(words, search_word, y):
    instances = []
    for word_index in range(len(words)):
        word = words[word_index]
        if(word == search_word):
            instances.append(word_index + 1)
    return [instances, [y for i in instances]]


def Multi_Chart(words, search_words, name="Untitled", appender=" "):
    axes = figure(figsize=(12, 6)).add_subplot(111)
    titles = []
    count = 0
    for word in search_words:
        if(isinstance(word, list)):
            graph_datas = []
            title_name = ""
            for part_word in word:
                graph_datas.append(Search(words, part_word, count))
                title_name += part_word.capitalize() + appender
            sum1 = []
            sum2 = []
            for gd in graph_datas:
                sum1 += gd[0]
                sum2 += gd[1]
            plt.plot(sum1, sum2, "go", markersize="5")
            titles.append(title_name[:-len(appender)])
            count += 1
            continue
        graph_data = Search(words, word, count)
        plt.plot(graph_data[0], graph_data[1], "go", markersize="5")
        titles.append(word.capitalize())
        count += 1
    yticks(np.arange(len(search_words)), titles)
    plt.title("Word Usage in the Book " + name)
    plt.xlabel("Order of Occurence of Word in Book")
    plt.show()




