from collections import Counter

def filter_evens(numbers):
    l=[ i for i in numbers if i % 2==0]
    return l

def get_top_word(word_list):
    w=Counter(word_list)
    return w.most_common(1)[0][0]

