def func(word):
    
    word = word + 'Na'
    print ('0:', word)
    return word

if __name__ == '__main__':
    word = 'Hey'
    print('1:', word)
    func(word)
    print('2:', word)
    word = func(word) + '!'
    print('3:', word)