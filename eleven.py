body = [x for x in range(10)]
k = int(input('please enter the index to be removed from the list:')) #index
print(body)


tmp = body[0:k] + body[k+1:len(body)]
body = tmp

print(body)

