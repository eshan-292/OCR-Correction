from difflib import SequenceMatcher

def accuracy(file1,file2):
    text1 = open(file1).read()
    text2 = open(file2).read()
    m = SequenceMatcher(None, text1, text2)
    return m.ratio()

def main():
    match = 100*accuracy("data/output.txt","data/pred.txt")    
    print(match)

if __name__ == "__main__":
    main()    