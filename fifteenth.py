inp = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]
outp = list(map(lambda x: x[-1], inp))
res = [price + 10 for price in outp if price < 100]

print(list(outp))
print(res)
