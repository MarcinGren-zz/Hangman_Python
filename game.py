
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
    print("Guess the phrase: " + phraseAnswer)
    phraseAnswer = checkIfTheLetterIsInTheAnswer(letterUsed)
    return phraseAnswer

listOfPhraseBeingGuessed = []
answer = "test"
answerBeingGuessed = list(answer)
lengthOfTheAnswer = len(answer)
listAnswer = hiddenAnswerWriter()
phraseAnswer = createPhrase(listAnswer)

print(answerBeingGuessed)



letterUsed = "e" #input("Please enter the letter: ")
if len(letterUsed) > 1:
    print("Please use one letter!")


phraseAnswer = guesser(phraseAnswer)

phraseAnswer = guesser(phraseAnswer)



print("**************")
print(letterUsed)
print("asd")


