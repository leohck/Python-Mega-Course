#  Copyright (c)  7/8/2019
#  Developed by: Leonardo Black | 21 years old | Computer Engineer


def sentence_maker(phrase):
    phrase = str(phrase)
    interrogatives = ("How", "What", "Why", "Should", "Could", "Do")
    capitalized = phrase.capitalize()
    if capitalized.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


words = []
while True:
    word_received = input("Say something: ")
    if word_received == "\\end":
        break
    else:
        words.append(sentence_maker(word_received))

print(" ".join(words))
