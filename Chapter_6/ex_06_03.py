def count(stringA, letterA):
    word = stringA
    count = 0
    for letter in word:
        if letter == letterA:
            count = count+1
    print(stringA,count,letterA)
#
word = input("Enter word to search in:")
letter = input("Enter letter to look for:")
count(word,letter)
