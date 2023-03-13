# with open('C:\\Users\\tosha\\Downloads\\hashes\\decrypted.txt') as r:
#     w = open('phones.txt', 'w')
#     for line in r:
#         line = line.split(':')[1]
#         w.write(line)

phones = set()
with open('phones.txt') as f:
    for line in f:
        phones.add(int(line.split(':')[1]))
samples = [89156617519
    #, 89866878664, 89636187893, 89038679411, 89868468991
           ]
for i in range(100000000):
    ok = True
    for num in samples:
        if num + i not in phones:
            ok = False
            break
    if ok:
        print(i)