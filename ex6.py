def zero(arr, word):
    if word == 'SMALI':
        if arr[0] == 'XPROC':
            return 7
        elif arr[0] == 'OPAL':
            return 8
    elif word == 'HTTP':
        if arr[0] == 'XPROC':
            return two(arr, arr[0])
        elif arr[0] == 'OPAL':
            return 12


def one(arr, word):
    if arr[1] == 'ALLOY':
        return two(arr, arr[1])
    elif arr[1] == 'SMALI' or 'HTTP':
        return zero(arr, arr[1])


def two(arr, word):
    if word == 'XPROC':
        if arr[2] == 1994:
            return 9
        elif arr[2] == 1982:
            return 10
        elif arr[2] == 2003:
            return 11
    elif word == 'ALLOY':
        if arr[2] == 1994:
            return three(arr, arr[2])
        elif arr[2] == 1982:
            return 3
        elif arr[2] == 2003:
            return three(arr, arr[2])


def three(arr, word):
    if word == 1994:
        if arr[3] == 'TEXT':
            return 0
        elif arr[3] == 'BLADE':
            return 1
        elif arr[3] == 'PAN':
            return 2
    elif word == 2003:
        if arr[3] == 'TEXT':
            return 4
        elif arr[3] == 'BLADE':
            return 5
        elif arr[3] == 'PAN':
            return 6


def main(arr):
    word = ''
    return one(arr, word)


print(main(['OPAL', 'HTTP', 1982, 'PAN']))
