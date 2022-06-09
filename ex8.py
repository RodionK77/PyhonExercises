import re


def main(str):
    str = re.split('[<>@"(;)./#\n ]+', str)
    d = {}
    one = ''
    two = []
    b = False
    for i in range(len(str)):
        if str[i] == 'end':
            break
        if str[i] == 'block' and str[i - 1] != 'begin' \
                and str[i - 1] != 'block':
            b = False
            d[one] = two
            one = ''
            two = []
        if str[i - 1] == 'block' and str[i] != 'block':
            one = str[i]
        if b:
            two.append(int(str[i]))
        if str[i - 1] == 'is':
            b = True
            two.append(int(str[i]))

    return d

print(main("""begin <block> @"atedin_911" is #( 4915 ; -5601 ). </block>. <block>
@"titiin" is#(4655 ; -5055 ; -2988 ; -4635).
</block>.<block>@"leso_581" is #( 1681 ; 8393 ; -7454 ). </block>. end"""))
