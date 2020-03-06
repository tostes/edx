alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
    list_word = list(plaintext)
    alpha_list = list(alphabet)
    new_word_list = []
    for i in list_word:
        index = alpha_list.index(i)
        new_index = index + k
        if new_index > (len(alpha_list)-1):
            new_index = new_index - (len(alpha_list+1))
        new_letter = alpha_list[new_index]
        print("%s ----> %s index: %s" % (i, new_letter, new_index))
        new_word_list.append(new_letter)


    
    new_word = ''.join(map(str, new_word_list))
    return (new_word)



