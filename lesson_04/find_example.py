sent = "My first name is Alex"

print(sent.find("Alex")) # will return symbol number on which the value appears
print(sent.find("Vasya")) # will return -1 if value is not found

is_index = sent.find("is")
result_sent = sent[:is_index]
print(result_sent)              # returns all before the value

if sent.find("Alex") > 0:
    print(True)

if "Alex" in sent:
    print("Alex in the sentence")

sent = "Alex My name is Alex"
search_word = "is"

search_word_index = sent.find(search_word)
len_of_search_word = len(search_word)
end_index = search_word_index + len_of_search_word
result_sent = sent[end_index:]
print(result_sent)
