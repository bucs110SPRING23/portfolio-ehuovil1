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
    def fixStart(self):
            if len(self.string) < 2:
                return(self.string)
            first = self.string[0]
            repl = self.string.replace(first, "*")
            repl = repl.replace("*", first, 1)
            return repl
    def asciiSum(self):
        asciisum = 0
        for i in self.string:
            asciisum += ord(i)
        return asciisum
    
    def cipher(self):
        length = len(self.string)
        cipher = ""
        for i in self.string:
            if i.islower():
                new = (ord(i) - ord('a') + length) % 26 + ord('a')
            elif i.isupper():
                new = (ord(i) - ord('A') + length) % 26 + ord('A')
            else:
                new = ord(i)
            new2 = chr(new)
            cipher += new2
        return cipher
            