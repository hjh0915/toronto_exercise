def read_lines(play, character):
    """ (file open for reading, str) -> list of str

    Return the list of dialogs (with all newlines removed) made by character in play.

    >>> file = open('play.txt')
    >>> actual = read_lines(file, 'MARK ANTONY')
    >>> expected = \
    ['I am sorry to give breathing to my purpose,--', \
    'Now, my dearest queen,--', \
    "What's the matter?"]
    >>> actual == expected
    True
    >>> file.close()
    """
    result = []

    line = play.readline().strip()

    #name记录段落归属

    need_be_inserted = False

    while line:
        #先判断是否有[xxxxxxxxxx]存在
        if ('[' in line) and (']' in line):

            #[索引位置 => start
            start = line.index('[') + 1
            #]索引位置 => end
            end = line.index(']')

            #人名
            name = line[start:end].strip()

            if name == character:
                #第一行的说话内容
                sentence = line[end+1:].strip()
                need_be_inserted = True
            else:
                if need_be_inserted:
                    result.append(sentence)

        else:
            #如果section段落记录的仍然是之前的人名
            #就连接这行内容
            if name == character:
                sentence = sentence + ' ' + line

        line = play.readline().strip()

    if name == character:
        result.append(sentence) 

    return result

if __name__ == '__main__':
    file = open('play.txt')
    actual = read_lines(file, 'MARK ANTONY')
    print(actual)
    file.close()




        