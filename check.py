from difflib import SequenceMatcher

with open ("file1.py") as one_file, open("file2.py") as two_file:
    data_file1=one_file.read()
    data_file2=two_file.read()
    matches=SequenceMatcher(None,data_file1,data_file2).ratio()
    print(f" The Plagirized {matches}%")