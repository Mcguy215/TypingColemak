from random import randint, choice
from operator import itemgetter


row1 = ["q","w","f","p","g","j","l","u","y"]
row2 = ["a","r","s","t","d","h","n","e","i","o"]
row3 = ["z","x","c","v","b","k","m"]

punc = [",",".","/","'","[","]","\\","-","=",]
nums = ["0","1","2","3","4","5","6","7","8","9"]

lett = row1 + row2 + row3
full = lett.copy()

exist = False

for item in lett:
    full.append(item.upper())
ak =[]

wordsa = []
print(
"""
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
    words = open("words.txt", "r")
except:
    try:
        print("words.txt failed to load! Trying Typing Colemak/words.txt")
        words = open("Typing Colemak/words.txt", "r")
    except:
        print("Typing Colemak/words.txt falied to load! Defaulting to small list...")
        words = ["a", "about", "all", "also", "and", "as", "at", "be", "because", "but", "by", "can", "come", "could", "day", "do", "even", "find", "first", "for", "from", "get", "give", "go", "have", "he", "her", "here", "him", "his", "how", "I", "if", "in", "into", "it", "its", "just", "know", "like", "look", "make", "man", "many", "me", "more", "my", "new", "no", "not", "now", "of", "on", "one", "only", "or", "other", "our", "out", "people", "say", "see", "she", "so", "some", "take", "tell", "than", "that", "the", "their", "them", "then", "there", "these", "they", "thing", "think", "this", "those", "time", "to", "two", "up", "use", "very", "want", "way", "we", "well", "what", "when", "which", "who", "will", "with", "would", "year", "you", "your"]

words = words.read().split(",")

conf = input("ENTER to Continue \n \n")
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
    settings1 = input()
    try:
        settings1 = int(settings1)
    except:
        print("\nThat isn't valid! (Not a number)")
        continue
    if settings1 > 9 or settings1 < 1:
        print("\nThat isn't valid! (Not between 1 and 8)")
        continue
    break
if settings1 == 1:
    ak = row2
elif settings1 == 2:
    ak = row1
elif settings1 == 3:
    ak = row3
elif settings1 == 4:
    ak = lett
elif settings1 == 5:
    ak = punc
elif settings1 == 6:
    ak = nums
elif settings1 == 7:
    ak = full
else:
    ak = full + punc + nums


try:
    settings2 = input("\n\nHow many rounds do you want to do? (Default 5) ")
    settings2 = int(settings2)
except:
    print(settings2, "isn't valid! Defaulting to 5.")
    settings2 = 5

print("\nYour active keys are", ak, "\n")

# Find Valid Words
for word in words:
    works = True
    for letter in word:
        if letter not in ak:
            works = False
    if works:
        wordsa.append(word)
        exist = True

correct = 0
wrong = 0
print("Please type the following!")

keysmissed = []

for item in ak:
    keysmissed.append([item, 0])


for x in range(settings2):
    ts = ""
    for y in range(10):
        if randint(0,3) == 1 or not exist:
            for x in range(6):
                ts += ak[randint(0,len(ak)-1)]
                if randint(0,2) == 1:
                    ts += " "
                    break
        else:
            if exist:
                ranword = wordsa[randint(0,len(wordsa)-1)]
                if (settings1 == 7 or settings1 == 8) and randint(0,1) != 0:
                    ts += ranword[0].upper()
                    ts += ranword[1:]
                else:
                    ts += ranword
                ts += " "
    print(ts)
    tt = input()
    correctr = 0
    wrongr = 0
    while 1:
        if len(ts) < len(tt):
            tt = tt[:-1]
        elif len(ts) > len(tt):
            tt += " "
        else:
            break

    lettersmissed = 0
    print("\n")
    for z in range(len(ts)):
        if ts[z] == tt[z]:
            correct += 1
            correctr += 1
        else:
            wrong += 1
            wrongr += 1
            try:
                keysmissed[ak.index(ts[z])][1] += 1
            except:
                pass
            lettersmissed += 1
            if lettersmissed < 5:
                print("On character",z+1,"You should have typed",ts[z],"but typed",tt[z])
    if lettersmissed >= 5:
        print(lettersmissed-5, "more incorrect characters abridged.")

    print("\nAccuracy =",round(correct / (correct + wrong)*100, 2))
    print("Accuracy (this round)=",round(correctr / (correctr + wrongr)*100, 2), "\n\n")
keysmissed.sort(key=(itemgetter(1)))
keysmissed.reverse()

print("==Anaylsis==")
print("- Accuracy",round(correct / (correct + wrong)*100, 2))
if settings2 == 1:
    print("- Round:", settings2)
else:
    print("- Rounds:", settings2)
print("- Frequency of keys missed \n")
for item in keysmissed:
    if item[1] != 0:
        if item[0] == 1:
            print(f"Mistyped: '{item[0]}', {item[1]} time.")
        else:
            print(f"Mistyped: '{item[0]}', {item[1]} times.")


input()
