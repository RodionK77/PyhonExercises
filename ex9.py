class Mili:
    i = 1

    def slur(self):
        if self.i == 1:
            self.i = 1
            return self.i
        elif self.i == 0 or self.i == 8:
            self.i = 2
            return self.i
        elif self.i == 4:
            self.i = 7
            return self.i
        else:
            raise KeyError

    def spawn(self):
        if self.i == 1:
            self.i = 0
            return self.i
        elif self.i == 2 or self.i == 7:
            self.i = 3
            return self.i
        elif self.i == 3 or self.i == 5:
            self.i = 5
            return self.i
        elif self.i == 4:
            self.i = 6
            return self.i
        else:
            raise KeyError

    def group(self):
        if self.i == 4:
            self.i = 8
            return self.i
        elif self.i == 3 or self.i == 5:
            self.i = 4
            return self.i
        else:
            raise KeyError


def main():
    o = Mili()
    return o


o = main()
o.group() # KeyError
print(o.slur()) # 1
o.group() # KeyError
print(o.spawn()) # 0
print(o.slur()) # 2
print(o.spawn()) # 3
print(o.group()) # 4
print(o.slur()) # 7
print(o.spawn()) # 3
print(o.spawn()) # 5
print(o.group()) # 4
print(o.spawn()) # 6
