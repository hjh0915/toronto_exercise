def zigzagzip(s1: str, s2: str) -> str:
    """ 
    Precondition: len(s1) == len(s2).

    Return a string made up of alternating letters from s1 and s2,
    starting with s1[0], then s2[1], s1[2], and so on.

    >>> zigzagzip('abc', '123')
    'a2c'
    >>> zigzagzip('abcd', '1234')
    'a2c4'
    """
    s = ''
    for num in range(len(s1)):
        if num % 2 == 0:
            s = s + s1[num]
        else:
            s = s + s2[num] 
    return s 

if __name__ == '__main__':
    print(zigzagzip('abc', '123'))