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
            return (self.string[0] + self.string[1] + self.string[-1] + self.string[-2])
           

        




