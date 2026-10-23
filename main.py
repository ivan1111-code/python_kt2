from modules.game import *

def start():

    entry = readRandomEntry("./modules/words.txt")
    word = entry.word
    description = entry.description

    lives = 3
    part = 1
    userLives = 3

    userWordProgress = initUserProgress(word)

    printGuess(userWordProgress, userLives)
    printDescription(description)

    while True:
        if isAlive(userLives) is False:
            return printFinalGuess()

        userWord = askWord()

        if isWord(userWord) is True:
            if isWordsMatch(word, userWord) is True:
                userWordProgress = openAllChars(word)
                printGuess(userWordProgress, userLives)
                return printWinGuess("Вы отгадали слово целиком")
            else:
                userLives = userLives - 1
                printGuess(userWordProgress, userLives)
                printPart(readFile(f"./modules/part{part}.txt"))
                part = part + 1

        else:
            if isCharExists(word, userWord) is True:
                userWordProgress = openChar(userWordProgress, word, userWord)
                if isUserWordDone(userWordProgress, word) is True:
                    printGuess(userWordProgress, userLives)
                    return printWinGuess("Вы отгадали слово по буквам")
                else:
                    printGuess(userWordProgress, userLives)
            else:
                userLives = userLives - 1
                printGuess(userWordProgress, userLives)
                printPart(readFile(f"./modules/part{part}.txt"))
                part = part + 1

start()

