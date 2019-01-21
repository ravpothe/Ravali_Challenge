# Please use python 2.
import re

def creditCardNumValid(cardNum):
    pattern = '^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'
    prog = re.compile(pattern)
    result = prog.match(cardNum)
    if result is None:
        return 'Invalid'
    cardNum = cardNum.replace('-', '')
    prev = cardNum[0]
    count = 1
    for digit in cardNum[1:]:
        if digit == prev:
            count += 1
        else:
            count = 1
        prev = digit
        if count == 4:
            return 'Invalid'
    return 'Valid'

if __name__ == '__main__':
    numCards = int(raw_input())
    cards = []
    for i in range(numCards):
        cards.append(raw_input())
    for card in cards:
        print creditCardNumValid(card)
