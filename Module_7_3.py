class WordsFinder:
    file_names = []

    def __init__(self, *args: str):
        self.args = args
        for i in args:
            self.file_names.append(i)

    def get_all_words(self):
        all_words: dict = {}

        replace_list = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            lines = []
            with open(i, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for symb in line:
                        if replace_list.__contains__(symb):
                            line = line.replace(symb, '')
                        else:
                            continue
                    line = line.split()
                    lines += line
            all_words.update({i: lines})
        return all_words

    def find(self, word: str):
        result: dict = {}
        self.get_all_words()
        for keys, values in self.get_all_words().items():
            for i in range(0, len(values)):
                if values[i] == word.lower():
                    result.update({keys: i+1})
                    break
        return result

    def count(self, word: str):
        result: dict = {}
        self.get_all_words()
        counter = 0
        for keys, values in self.get_all_words().items():
            for i in values:
                if i == word.lower():
                    counter += 1
            result.update({keys: counter})
            counter = 0
        return result


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

