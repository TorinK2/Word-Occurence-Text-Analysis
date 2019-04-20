def ReadFile(text_file):
    FileHandler = open(text_file, "r")
    full_text = FileHandler.read()
    FileHandler.close()

    edited_full_text = ""

    for char_index in range(len(full_text)):
        char = full_text[char_index]
        if(char.isalpha() or char == "-" or char == " "):
            edited_full_text += char
            continue
        if(char == "\n"):
            edited_full_text += " "
            continue
        
    unclean_words = edited_full_text.replace("--", " ").split(" ")
    clean_words = []
    for word in unclean_words:
        if(len(word) >= 2):
            clean_words.append(word.lower())
    return clean_words


