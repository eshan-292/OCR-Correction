# from difflib import SequenceMatcher

# def accuracy(file1,file2):
#     text1 = open(file1).read()
#     text2 = open(file2).read()
#     m = SequenceMatcher(None, text1, text2)
#     return m.ratio()

# def main():
#     match = 100*accuracy("data/output.txt","data/pred.txt")    
#     print(match)

# if __name__ == "__main__":
#     main()    

file1 = "data/output.txt"
file2 = "data/pred.txt"
f1 = open(file1,"r")
f2 = open(file2,"r")
lista = f1.readlines()
listb = f2.readlines()
def words_different(list1,list2):
    answer = 0
    for i in range(len(list1)):
        if(list1[i]!=list2[i]):
            print(list1[i],list2[i])
            answer+=1
    return answer
total_words = 0
words_diff = 0
for i in range(len(lista)):
    total_words += len(lista[i].split(' '))
    words_diff += words_different(lista[i].split(' '),listb[i].split(' '))
print((total_words-words_diff)*100/total_words)