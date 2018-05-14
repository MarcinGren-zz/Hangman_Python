
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

def typeLetter():
    letterUsed = input("Please enter the letter: ")
    if len(letterUsed) > 1:
        print("Please use one letter!")
        letterUsed = ""
    return letterUsed



listOfPhraseBeingGuessed = []
answer = "test"
answerBeingGuessed = list(answer)
lengthOfTheAnswer = len(answer)
listAnswer = hiddenAnswerWriter()
phraseAnswer = createPhrase(listAnswer)
letterUsed = ""

print(answerBeingGuessed)

for i in range(10):
    phraseAnswer = guesser(phraseAnswer)
    if listOfPhraseBeingGuessed == answerBeingGuessed:
        print("Congratulations! You've guessed it!")
        break
    letterUsed = typeLetter()


# phraseAnswer = guesser(phraseAnswer)
# letterUsed = typeLetter()
# phraseAnswer = guesser(phraseAnswer)




