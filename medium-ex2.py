paragraph = "This course is not nice it is amazing course "
paragraph = paragraph.lower()
words = paragraph.split()
unique_words = list(set(words))
list={}
#print(unique_words )
for w in unique_words:
    count=len(w)
    list[w]  = count
print(list)

#word=input("Type a  word : ")
#count=len(word)
#print(count)