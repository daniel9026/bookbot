def count_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items['num']

def get_sorted_list(dict):
    char_list = [
        {'char': key, 'num': value}
        for key, value in dict.items()
        if key.isalpha()
    ]
    sorted_list = sorted(char_list, key=lambda x:x['num'], reverse=True)
    return sorted_list

