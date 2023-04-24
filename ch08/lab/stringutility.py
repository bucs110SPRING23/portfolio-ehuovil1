class StringUtility:
    def __init__(self, string):
        self.string = string
    def __str__(self):
        return self.string
    def vowels(self):
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        vowelcount = 0
        for i in self.string:
            for x in vowels:
                if i == x:
                    vowelcount +=1
        if vowelcount < 5:
            return str(vowelcount)
        else:
            return "many"
    def bothEnds(self):
            if len(self.string) < 3:
                return ""
            return (self.string[0] + self.string[1] + self.string[-2] + self.string[-1])
           
    class StringManipulator:
        def bothEnds(self, s):
            if len(s) <= 2:
                return ""
            else:
                return s[:2] + s[-2:]

    def fixStart(self, s):
        if len(s) <= 1:
            return s
        else:
            first_char = s[0]
            return first_char + s[1:].replace(first_char, '*')

    def asciiSum(self, s):
        return sum(ord(c) for c in s)

    def cipher(self, s):
        shifted = ""
        for c in s:
            if c.isalpha():
                ascii_offset = 65 if c.isupper() else 97
                shifted_char = chr((ord(c) - ascii_offset + len(s)) % 26 + ascii_offset)
                shifted += shifted_char
            else:
                shifted += c
        return shifted

        




