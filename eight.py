s = input("Введіть рядок:")
ch = input("Введіть символ:")
start = 0
while start < len(s):
    poi = s.find(ch, start)
    if poi == -1:
        break
    print('index of symbol: ', poi)
    start = poi + 1
