with open('salted.txt', 'w') as w:
    with open('source.txt') as f:
        for line in f:
            w.write(str(int(line.rstrip()) + 87893892) + '\n')
