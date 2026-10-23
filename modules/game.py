import random

class WordEntry:
    def __init__(self, word: str, description: str):
        self.word = word
        self.description = description


def initUserProgress(word: str):
    userWordProgress = []
    for i in range(len(word)):
        userWordProgress.append(False)
    return userWordProgress


def isWord(word):
    return len(word) > 1


def isWordsMatch(word: str, userWord: str):
    return word == userWord


def isAlive(lives: int) -> bool:
    return lives > 0


def isCharExists(word: str, char: str):
    for i in range(len(word)):
        if word[i] == char:
            return True
    return False


def openChar(userWordProgress: list, word: str, char: str):
    result = userWordProgress
    for i in range(len(word)):
        if word[i] == char:
            result[i] = char
    return result


def isUserWordDone(userWordProgress: list, word: str):
    for i in range(len(word)):
        if userWordProgress[i] != word[i]:
            return False
    return True


def openAllChars(word: str):
    result = []
    for i in range(len(word)):
        result.append(word[i])
    return result

def askWord(minLenWord: int = 2, maxLenWord: int = 20) -> str:
    isAdditionalSen = False
    additionalSen = ""
    while True:
        ask = "Введите букву или слово целиком"
        if isAdditionalSen is True:
            ask += " "
            ask += f"({additionalSen})"
        ask += ": "
        word = input(ask)
        if len(word) > 1:
            if (len(word) > minLenWord and len(word) < maxLenWord):
                return word
            else:
                print(f"Длина слова должна быть в диапазоне от {minLenWord} до {maxLenWord} букв")
                if isAdditionalSen is False:
                    isAdditionalSen = True
                    additionalSen = "повторите попытку"
        else:
            return word


def printGuess(userWordProgress: list, livesLeft: int):
    result = ""
    for i in range(len(userWordProgress)):
        if userWordProgress[i] is False:
            if i == len(userWordProgress) - 1:
                result += "⬛"
            else:
                result += "⬛ "
        else:
            if i == len(userWordProgress) - 1:
                result += userWordProgress[i]
            else:
                result += f"{userWordProgress[i]} "
    print(f"{result} | ❤️  x{livesLeft}")


def readRandomEntry(filepath: str) -> WordEntry:
    separator = " - "
    entries = []
    
    with open(filepath, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            
            if separator not in line:
                raise ValueError(
                    f"Строка {line_number}: отсутствует разделитель ' - ': {line!r}"
                )
            
            word, description = line.split(separator, maxsplit=1)
            word = word.strip()
            description = description.strip()
            
            if not word or not description:
                raise ValueError(
                    f"Строка {line_number}: пустое слово или описание: {line!r}"
                )
            
            entries.append(WordEntry(word, description))
    
    if not entries:
        raise ValueError(f"Файл пуст или не содержит корректных строк: {filepath!r}")
    
    return random.choice(entries)


def printDescription(description):
    print(f"подсказка: {description}")


def printFinalGuess():
    print("Ваши жизни закончились")


def printWinGuess(message):
    print(message)


def readFile(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def printPart(part):
    print(part)