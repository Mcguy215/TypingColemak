from random import randint, choice
from string import digits
from collections import Counter


row1 = "qwfpgjluy"
row2 = "arstdhneio"
row3 = "zxcvbkm"

punc = ",./'[]\\-="

lett = row1 + row2 + row3
full = lett

for item in lett:
    full += item.upper()

print(r"""
 ▄████▄   ▒█████   ██▓    ▓█████  ███▄ ▄███▓ ▄▄▄       ██ ▄█▀
▒██▀ ▀█  ▒██▒  ██▒▓██▒    ▓█   ▀ ▓██▒▀█▀ ██▒▒████▄     ██▄█▒
▒▓█    ▄ ▒██░  ██▒▒██░    ▒███   ▓██    ▓██░▒██  ▀█▄  ▓███▄░
▒▓▓▄ ▄██▒▒██   ██░▒██░    ▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ▓██ █▄
▒ ▓███▀ ░░ ████▓▒░░██████▒░▒████▒▒██▒   ░██▒ ▓█   ▓██▒▒██▒ █▄
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░▓  ░░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒
  ░  ▒     ░ ▒ ▒░ ░ ░ ▒  ░ ░ ░  ░░  ░      ░  ▒   ▒▒ ░░ ░▒ ▒░
░        ░ ░ ░ ▒    ░ ░      ░   ░      ░     ░   ▒   ░ ░░ ░
░ ░          ░ ░      ░  ░   ░  ░       ░         ░  ░░  ░
░

  _____                 _                   _                                            _
 |_   _|  _  _   _ __  (_)  _ _    __ _    | |     ___   ___  ___  ___   _ _    ___    _| |_
   | |   | || | | '_ \ | | | ' \  / _` |   | |__  / -_) (_-< (_-< / _ \ | ' \  (_-<   |_   _|
   |_|    \_, | | .__/ |_| |_||_| \__, |   |____| \___| /__/ /__/ \___/ |_||_| /__/     |_|
          |__/  |_|               |___/
  ___                     _     _
 | _ \  _ _   __ _   __  | |_  (_)  __   ___
 |  _/ | '_| / _` | / _| |  _| | | / _| / -_)
 |_|   |_|   \__,_| \__|  \__| |_| \__| \___|



""")
try:
    words = open("words.txt").read().split(",")
except:
    try:
        print("words.txt failed to load! Trying Typing Colemak/words.txt")
        words = open("Typing Colemak/words.txt").read().split(",")
    except:
        print("Typing Colemak/words.txt failed to load! Defaulting to small list...")
        words = ["a", "about", "all", "also", "and", "as", "at", "be", "because", "but", "by", "can", "come", "could", "day", "do", "even", "find", "first", "for", "from", "get", "give", "go", "have", "he", "her", "here", "him", "his", "how", "I", "if", "in", "into", "it", "its", "just", "know", "like", "look", "make", "man", "many", "me", "more", "my", "new", "no", "not", "now", "of", "on", "one", "only", "or", "other", "our", "out", "people", "say", "see", "she", "so", "some", "take", "tell", "than", "that", "the", "their", "them", "then", "there", "these", "they", "thing", "think", "this", "those", "time", "to", "two", "up", "use", "very", "want", "way", "we", "well", "what", "when", "which", "who", "will", "with", "would", "year", "you", "your"]

input("ENTER to Continue \n \n")
while True:
    print("""
What would you like to practice?
   (1) - Home Row [arst]
   (2) - Top row (qwfp)
   (3) - Bottom row (zxcv)
   (4) - All letters
   (5) - Punctuation (,./')
   (6) - Numbers (1234)
   (7) - Letters + Shift (QWFP)
   (8) - Full""")
    inp = input()
    try:
        inp = int(inp)
        if inp >= 1 and inp <= 8:
            break
        print("\nThat isn't valid! (Not between 1 and 8)")
    except:
        print("\nThat isn't valid! (Not a number)")

# choose active keys
ak = (row2, row1, row3, lett, punc, digits, full, full + punc + digits)[inp - 1]

try:
    rounds = input("\n\nHow many rounds do you want to do? (Default 5) ")
    rounds = int(rounds)
except:
    print(rounds, "isn't valid! Defaulting to 5.")
    rounds = 5

print(f"\nYour active keys are {ak} \n")  # {list(ak)} for old formatting

valid_words = [word for word in words if all(letter in ak for letter in word)]

print("Please type the following!")

correct = 0
wrong = 0
missed_keys = Counter()

for round_ in range(rounds):
    word = ""
    for _ in range(10):
        # no valid_words or 1/4
        if not valid_words or not randint(0, 3):
            for _ in range(6):
                word += choice(ak)
                if not randint(0, 2):  # 1/3
                    word += " "
                    break
        else:
            ranword = choice(valid_words)
            # capitalization on and 1/2
            if full in ak and randint(0, 1):
                word += ranword[0].upper()
                word += ranword[1:]
            else:
                word += ranword
            word += " "
    print(word)
    inp = input()

    # make same length
    if len(inp) > len(word):
        inp = inp[:len(word)]
    else:
        inp = inp.ljust(len(word))

    correctr = 0
    wrongr = 0
    missed_letters = 0
    print("\n")
    for index, (w, i) in enumerate(zip(word, inp)):
        if w == i:
            correct += 1
            correctr += 1
        else:
            wrong += 1
            wrongr += 1
            missed_keys.update(w)
            missed_letters += 1
            if missed_letters <= 5:
                print(f"On character {index+1} you should have typed {w} but typed {i}")
    if missed_letters > 5:
        print(f"{missed_letters-5} more incorrect characters abridged.")

    print(f"\nAccuracy = {round(correct / (correct + wrong)*100, 2)}%")
    print(f"Accuracy (this round) = {round(correctr / (correctr + wrongr)*100, 2)}%\n\n")

print("==Analysis==")
print(f"- Accuracy {round(correct / (correct + wrong)*100, 2)}%")

print(f"- Round{'s' if round_ != 1 else ''}: {round_}")
print("- Frequency of keys missed \n")
for k, v in missed_keys.most_common(len(missed_keys)):
    if k == 1:
        print(f"Mistyped: '{k}', {v} time.")
    else:
        print(f"Mistyped: '{k}', {v} times.")

input()
