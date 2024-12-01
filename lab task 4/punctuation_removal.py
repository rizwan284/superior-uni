class Remove_Punctuation:
    def __init__(self, input_str):
        self.input_str = input_str
        self.cleaned_str = ""

    def remove_punc(self):
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in self.input_str:
            if char not in punc:
                self.cleaned_str += char
        print(f"The text without punctuation is: {self.cleaned_str}")


usage = input("Enter your Text: ")
obj = Remove_Punctuation(usage)
obj.remove_punc()
