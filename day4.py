from hashlib import md5


if __name__ == '__main__':

    with open('./inputs/day4.txt') as f:
        hashkey = f.readline()

    f5 = f6 = False
    for x in range(10000000):
        value = hashkey + str(x)
        hash_obj = md5(value.encode())
        hex = hash_obj.hexdigest()
        if hex[0:5] == '00000':
            print(f'{hashkey}, {x}')
            f5 = True
        if hex[0:6] == '000000':
            print(f'{hashkey}, {x}')
            f6 = True

        if f5 and f6:
            break