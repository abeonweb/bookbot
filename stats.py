from operator import itemgetter

def get_word_count(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

def get_characters_count(text):
    characters = {}
    text_length = len(text)
    for i in range(0, text_length):
        character = text[i].lower()
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sorted_characters(characters):
    list_of_chars = []
    for key in characters:
        list_of_chars.append({"char": key, "num": characters[key]})
    new_list = sorted(list_of_chars, key=itemgetter("num"), reverse=True)
    return new_list