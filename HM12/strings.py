sentence = input('Type a sentence:')
print('The 3d character of the sentence: ' + sentence[2])
print('The penult character of the sentence: ' + sentence[len(sentence) - 2])
print('The first 5 characters of the sentence: ' + sentence[0:5])
print('Whole sentence without last 2 characters: ' + sentence[:len(sentence) - 2])
print('Sentence with even characters: ' + sentence[1::2])
print('Sentence with odd characters: ' + sentence[0::2])
print('Inversed sentence : ' + sentence[::-1])
print('Inversed sentence through one character: ' + sentence[::-2])
print('The length of the sentence: ' + str(len(sentence)))