
def answerWriter():
    for letters in range(lengthOfTheAnswer):
        listOfPhraseBeingGuessed.append("_ ")
    return listOfPhraseBeingGuessed

def createPhrase(listOfPhrase):
    phraseBeingGuessed = ''.join(listOfPhrase)
    return phraseBeingGuessed

listOfPhraseBeingGuessed = []
answer = "test"
lengthOfTheAnswer = len(answer)



letterUsed = "a" #input("Please enter the letter: ")
if len(letterUsed) > 1:
    print("Please use one letter!")

listAnswer = answerWriter()
phraseAnswer = createPhrase(listAnswer)

print("Guess the phrase: " + phraseAnswer)


print(letterUsed)
print("asd")


