def main(number):
    end_one = number & 0xf
    end_two = number & 0xf0
    end_three = number & 0xf00
    number = number & 0xfffff000 | end_one << 8 | end_two >> 4 | end_three >> 4
    red = number & 0xe0000000
    blue = number & 0x10000000
    green = number & 0x0e000000
    purple = number & 0x01000000
    number = number & 0x00ffffff | red >> 4 | blue << 3
    number = number | green << 3 | purple
    return hex(number)
