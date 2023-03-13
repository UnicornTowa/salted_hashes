salt = 87893892

dict = {}
with open('phones.txt') as f:
    for line in f:
        line = line.rstrip().split(':')
        dict[line[0]] = int(line[1])
with open('hashes.txt') as f:
    with open('source.txt', 'w') as w:
        for line in f:
            w.write(str(dict[line.rstrip()] - salt) + '\n')