class CodePreprocessor:
    def __init__(self, code):
        self.code = code

    def clean_code(self):
        cleaned = self.code.lower()
        cleaned = " ".join(cleaned.split())
        return cleaned


def tokenize(code):
    return code.split()


def jaccard_similarity(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union


with open("file1.py") as f:
    code1 = f.read()

with open("file2.py") as f:
    code2 = f.read()

p1 = CodePreprocessor(code1)
p2 = CodePreprocessor(code2)

clean1 = p1.clean_code()
clean2 = p2.clean_code()

tokens1 = tokenize(clean1)
tokens2 = tokenize(clean2)

set1 = set(tokens1)
set2 = set(tokens2)

score = jaccard_similarity(set1, set2)

print("Similarity:", score * 100, "%")