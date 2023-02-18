stri = 'natus natus error sit error error error sit voluptatem accusantium voluptatem accusantium voluptatem accusantium '
text = stri.split()
res = dict()

for word in text:
    res[word] = text.count(word)

print(res)
