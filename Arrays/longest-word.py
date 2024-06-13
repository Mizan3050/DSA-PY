#Find the largest word in a given string
#Examples
#Input: "fun&!! time"
#Output: time

def easy_longest_word(character):
    count = 0
    maximum = 0
    word = ''

    for c in character:
        if c.isalnum():
            count +=1
            word +=c
        else:
            maximum =  max(maximum, count)
            count = 0
            word = ''
    
    maximum = max(maximum, count)
    return maximum, word


string = 'fun!@#$# times'
print(easy_longest_word(string))