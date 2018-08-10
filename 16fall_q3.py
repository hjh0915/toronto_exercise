from typing import List

def get_positions(text):
    """ (str) -> dict of {str: list of int}

    Return a dictionary where the keys are the individual words in text, and
    the values are the positions in the text where the words occur (starting
    at 1). Include punctuation and numbers in words, and convert alphabetic
    characters to lowercase.

    >>> result = get_positions('cats Cats CATS CATS!!!')
    >>> result == {'cats': [1, 2, 3], 'cats!!!': [4]}
    True
    >>> result = get_positions('I think I like CSC108.')
    >>> result == {'i': [1, 3], 'think': [2], 'like': [4], 'csc108.': [5]}
    True
    """
    d = {}
    x = text.split()
    for i in range(len(x)):
        y = x[i].lower()
        if y not in d:
            d[y] = []
        d[y].append(i + 1)
    return d

if __name__ == '__main__':
    result = get_positions('cats Cats CATS CATS!!!')
    print(result == {'cats': [1, 2, 3], 'cats!!!': [4]})