def find_occurrences(msg, sub):
    """ (str, str) -> list of int

    Return a list containing all of the indicies at in msg
    where sub appears.

    >>> find_occurrences('Paul eats lollipops', 'lol')
    [10]
    >>> find_occurrences('lololol', 'lol')
    [0, 4]
    """
    result = []
    occurrence = msg.find(sub)
    while occurrence != -1:
        result.append(occurrence)
        occurrences = occurrence + len(sub)
        occurrence = msg.find(sub, occurrences)
    return result

if __name__ == '__main__':
    print(find_occurrences('Paul eats lollipops', 'lol'))

    print(find_occurrences('lololol', 'lol'))