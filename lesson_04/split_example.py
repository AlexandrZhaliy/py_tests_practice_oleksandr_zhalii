sent = '"Would you tell me, please, which way I ought to go from here?"'

my_phrases = sent.split(",")
print(my_phrases)

print(f"first phrase =  {my_phrases[0]}")
print(f"second_phrase = {my_phrases[1]}")

print(sent.split(" "))

copy_sent = '"Would you       tell me, please,      which way I ought to     go from here?"'

space_split = copy_sent.split(" ")
default_split = copy_sent.split()

for element in default_split:
    new_element = f"this element is: {element}"
    print(new_element)

correct_sentence = False
for element in space_split:
    if element == "":
        correct_sentence = False
print(f"Sentence correct: {correct_sentence}")

wrong_sentence = False
for element in space_split:
    if element == "":
        wrong_sentence = True
print(f"Sentence correct: {wrong_sentence}")



print(space_split)
print(default_split)