
def hiddenAnswerWriter():
    for letters in range(lengthOfTheAnswer):
        listOfPhraseBeingGuessed.append("_ ")
    return listOfPhraseBeingGuessed

def createPhrase(listOfPhrase):
    phraseBeingGuessed = ''.join(listOfPhrase)
    return phraseBeingGuessed

def checkIfTheLetterIsInTheAnswer(letter):
    for i in range(lengthOfTheAnswer):
        if letter == answerBeingGuessed[i]:
            listOfPhraseBeingGuessed[i] = answerBeingGuessed[i]
    phraseAnswer = createPhrase(listOfPhraseBeingGuessed)
    return phraseAnswer

def guesser(phraseAnswer):
    phraseAnswer = checkIfTheLetterIsInTheAnswer(letterUsed)
    print("Guess the phrase: " + phraseAnswer)
    return phraseAnswer

def typeLetter(usedLetters):
    print("Letters used: " + str(usedLetters))
    letterUsed = input("Please enter the letter: ")
    if len(letterUsed) > 1:
        print("Please use one letter!")
        letterUsed = ""
    usedLetters = lettersUsedList(letterUsed)
    return letterUsed

def lettersUsedList(letter):
    if letter in usedLetters:
        print("Letter already tried, please pick another.")
    else:
        usedLetters.append(letter)
        return usedLetters


listOfPhraseBeingGuessed = []
answer = "test"
answerBeingGuessed = list(answer)
lengthOfTheAnswer = len(answer)
listAnswer = hiddenAnswerWriter()
phraseAnswer = createPhrase(listAnswer)
letterUsed = ""
usedLetters = []

#print(answerBeingGuessed)

for i in range(10):
    phraseAnswer = guesser(phraseAnswer)
    if listOfPhraseBeingGuessed == answerBeingGuessed:
        print("Congratulations! You've guessed it!")
        break
    letterUsed = typeLetter(usedLetters)

# if listOfPhraseBeingGuessed == answerBeingGuessed:
#     print("Congratulations! You've guessed it!")

# phraseAnswer = guesser(phraseAnswer)
# letterUsed = typeLetter()
# phraseAnswer = guesser(phraseAnswer)




