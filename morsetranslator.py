morseCode = {
    "A":"._",
    "B":"_...",
    "C":"_._.",
    "D":"_..",
    "E":".",
    "F":".._.",
    "G":"__.",
    "H":"....",
    "I":"..",
    "J":".___",
    "K":"_._",
    "L":"._..",
    "M":"__",
    "N":"_.",
    "O":"___",
    "P":".__.",
    "Q":"__._",
    "R":"._.",
    "S":"...",
    "T":"_",
    "U":".._",
    "V":"..._",
    "W":".__",
    "X":"_.._",
    "Y":"_.__",
    "Z":"__.."
}

text = input("Type something\n")
words = text.split() 
morseMessage = []

for word in words:
    morseWord = [morseCode[char.upper()] for char in word if char.upper() in morseCode]
    morseMessage.append(" ".join(morseWord))

finalMessage = " / ".join(morseMessage)
print(finalMessage)
