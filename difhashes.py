from hashlib import sha1, sha3_512, sha256
import whirlpool

with open('source.txt') as f:
    with open('sha256.txt', 'w') as w:
        for line in f:
            w.write(str(sha256(line.rstrip().encode('utf-8')).hexdigest()) + '\n')

# with open('source.txt') as f:
#     with open('whirlpool.txt', 'w') as w:
#         for line in f:
#             w.write(str(whirlpool.new(line.rstrip().encode('utf-8')).hexdigest()) + '\n')