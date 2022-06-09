from struct import *

FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
)


def parse(buf, offs, ty):
    return unpack_from(FMT[ty], buf, offs)[0], offs + calcsize(FMT[ty])


def parse_a(buf, offs):
    a1, offs = parse(buf, offs, 'uint64')
    a2, offs = parse(buf, offs, 'int64')
    a3_size, offs = parse(buf, offs, 'uint32')
    a3_offs, offs = parse(buf, offs, 'uint32')
    a3 = []
    for _ in range(a3_size):
        val, a3_offs = parse_b(buf, a3_offs)
        a3.append(val)
    a4_offs, offs = parse(buf, offs, 'uint16')
    a4, a4_offs = parse_c(buf, a4_offs)
    a5, offs = parse(buf, offs, 'int32')
    a6_offs, offs = parse(buf, offs, 'uint32')
    a6, a6_offs = parse_e(buf, a6_offs)
    a7, offs = parse(buf, offs, 'float')
    a8_offs, offs = parse(buf, offs, 'uint32')
    a8, a8_offs = parse_f(buf, a8_offs)

    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8), offs


def parse_b(buf, offs):
    b1_size, offs = parse(buf, offs, 'uint16')
    b1_offs, offs = parse(buf, offs, 'uint32')
    b1 = []
    for _ in range(b1_size):
        val, b1_offs = parse(buf, b1_offs, 'char')
        b1.append(val.decode())
    b2, offs = parse(buf, offs, 'int8')
    b3, offs = parse(buf, offs, 'int8')
    b4, offs = parse(buf, offs, 'uint32')
    b5, offs = parse(buf, offs, 'float')
    b6, offs = parse(buf, offs, 'int64')
    return dict(B1=''.join(b1), B2=b2, B3=b3, B4=b4, B5=b5, B6=b6), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'uint32')
    c2, offs = parse(buf, offs, 'uint32')
    c3, offs = parse_d(buf, offs)
    c4, offs = parse(buf, offs, 'int8')
    c5, offs = parse(buf, offs, 'uint32')
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'uint64')
    d2_size, offs = parse(buf, offs, 'uint16')
    d2_offs, offs = parse(buf, offs, 'uint16')
    d2 = []
    for _ in range(d2_size):
        val, d2_offs = parse(buf, d2_offs, 'uint8')
        d2.append(val)
    d3, offs = parse(buf, offs, 'float')
    d4, offs = parse(buf, offs, 'int8')
    return dict(D1=d1, D2=d2, D3=d3, D4=d4), offs


def parse_e(buf, offs):
    e1, offs = parse(buf, offs, 'int16')
    e2 = []
    for _ in range(4):
        val, offs = parse(buf, offs, 'int64')
        e2.append(val)
    return dict(E1=e1, E2=e2), offs


def parse_f(buf, offs):
    f1_size, offs = parse(buf, offs, 'uint32')
    f1_offs, offs = parse(buf, offs, 'uint32')
    f1 = []
    for _ in range(f1_size):
        val, f1_offs = parse(buf, f1_offs, 'uint8')
        f1.append(val)
    f2, offs = parse(buf, offs, 'uint16')
    f3, offs = parse(buf, offs, 'int8')
    f4, offs = parse(buf, offs, 'float')
    return dict(F1=f1, F2=f2, F3=f3, F4=f4), offs


def main(buf):
    return parse_a(buf, 5)[0]


print(main(b'RHMN\x9a\xd3\x17\xb1\xbb\x06\x0c@\x07\x9b\xe6\xb7Ro\xdc\xb6[\x02\x00\x00'
 b'\x005\x00\x00\x00h\x00\x06n$\xf3\x86\x00\x00\x00:\xa1$\xbf\xac\x00\x00\x00l'
 b"hijyz\x03\x00/\x00\x00\x00\xc5\xda\xa1p;S\x9b\xb6\x16\xbfD\xe6'"
 b'\xd0\x9d\x01\x9bV\x03\x002\x00\x00\x00ON\xd7%\xb4\xd49\xa2X\xbf\xca\xf3\xd1'
 b'\xd0\x177\x039i\x8e^2\xb2\xfc\xe9\x1fn(\xaaB\xc3}\xd0\xf8\x1c\xc1\x82'
 b'\x03\x00e\x00\xd9\xf8\xc1\xbe;\x130W4\xbb\xfd34\xa61\x9d\xf1Nh\x05%A.\xd5'
 b'jf\xd7\xa2\xec^F\xe3\xf1\xbbY\x9cH\x1fR\x1d<\x87r\xad\xbc\xfe\xea\xe5'
 b'\x04\x00\x00\x00\xa8\x00\x00\x00\xf9\xb1\x05%\t\x1d\xbf'))
