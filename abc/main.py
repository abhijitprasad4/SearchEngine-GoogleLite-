# first storing all the words that have to be ignored
f = open("english.txt",encoding="utf8")
read = f.readlines()
list = []
for line in read:
    list.append(line.strip())
f.close()

ignoreWordDict = {}
for x in list:
    ignoreWordDict[x] = 1

# keyword indexing starts from here
# creating dictionary for each articles
k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20,k21,k22,k23,k24,k25,k26,k27,k28,k29,k30,k31,k32,k33,k34,k35,k36,k37,k38,k39,k40,k41,k42,k43,k44,k45,k46,k47,k48,k49,k50 = {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}
list = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20,k21,k22,k23,k24,k25,k26,k27,k28,k29,k30,k31,k32,k33,k34,k35,k36,k37,k38,k39,k40,k41,k42,k43,k44,k45,k46,k47,k48,k49,k50]
AllWordDict = {}
# traversing all words of all articles
for x,kdict in zip((range(1,51)),list):
    x = str(x)
    f = open("news_k50/k"+x+".txt",encoding="utf8")
    read = f.readlines()
    for line in read:
        for word in line.split():
            #removing "", from word
            if word and not word[0].isalnum():
                word = word[1:]
            if word and not word[-1].isalnum():
                word = word[:-1]
            if word and not word[-1].isalnum():
                word = word[:-1]
            word = word.lower()
            # storing all word of individual article in their individual dictionary
            if word not in ignoreWordDict:
                if word in kdict:
                    kdict[word] += 1
                else:
                    kdict[word] = 1
                # storing all words of all article in AllWordDict word as key and list of article(in which the word is present) as value
                if word in AllWordDict:
                    if  "k"+x not in AllWordDict[word]:
                        AllWordDict[word] = AllWordDict[word] + ["k"+x]
                else:
                    AllWordDict[word] = ["k"+x]
    f.close()
# Retrival starts here
# taking inputs
while 1:
    #creating another individual dict for each article
    k1_2,k2_2,k3_2,k4_2,k5_2,k6_2,k7_2,k8_2,k9_2,k10_2,k11_2,k12_2,k13_2,k14_2,k15_2,k16_2,k17_2,k18_2,k19_2,k20_2,k21_2,k22_2,k23_2,k24_2,k25_2,k26_2,k27_2,k28_2,k29_2,k30_2,k31_2,k32_2,k33_2,k34_2,k35_2,k36_2,k37_2,k38_2,k39_2,k40_2,k41_2,k42_2,k43_2,k44_2,k45_2,k46_2,k47_2,k48_2,k49_2,k50_2={},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}
    arr = ["k1_2","k2_2","k3_2","k4_2","k5_2","k6_2","k7_2","k8_2","k9_2","k10_2","k11_2","k12_2","k13_2","k14_2","k15_2","k16_2","k17_2","k18_2","k19_2","k20_2","k21_2","k22_2","k23_2","k24_2","k25_2","k26_2","k27_2","k28_2","k29_2","k30_2","k31_2","k32_2","k33_2","k34_2","k35_2","k36_2","k37_2","k38_2","k39_2","k40_2","k41_2","k42_2","k43_2","k44_2","k45_2","k46_2","k47_2","k48_2","k49_2","k50_2"]
    word = input("Input your word:- ")
    word = word.lower()
    word = word.split()
    dictOfAllWord = {"k1_2": [],"k2_2": [],"k3_2": [],"k4_2": [],"k5_2": [],"k6_2": [],"k7_2": [],"k8_2": [],"k9_2": [],"k10_2": [],"k11_2": [],"k12_2": [],"k13_2": [],"k14_2": [],"k15_2": [],"k16_2": [],"k17_2": [],"k18_2": [],"k19_2": [],"k20_2": [],"k21_2": [],"k22_2": [],"k23_2": [],"k24_2": [],"k25_2": [],"k26_2": [],"k27_2": [],"k28_2": [],"k29_2": [],"k30_2": [],"k31_2": [],"k32_2": [],"k33_2": [],"k34_2": [],"k35_2": [],"k36_2": [],"k37_2": [],"k38_2": [],"k39_2": [],"k40_2": [],"k41_2": [],"k42_2": [],"k43_2": [],"k44_2": [],"k45_2": [],"k46_2": [],"k47_2": [],"k48_2": [],"k49_2": [],"k50_2": []}
    n = len(word)
    dictOfAllWord2 = {}
    list3 = []
    for individual_word in word:
        listOfword = {}
        #check if the word exists in any of the articles or not
        if individual_word in AllWordDict:
            for x in AllWordDict[individual_word]:
                #traversing through the list of all articles in which the word exists and storing article name as key and no. of times the word appear in the article as value in local dictionary listOfword
                listOfword[x] = list[int(x[1:]) - 1][individual_word]
                #storing all the entered(from user) word that exists in individual articles in dictOfAllWord dictionary
                if individual_word not in dictOfAllWord[arr[int(x[1:]) - 1]]:
                    dictOfAllWord[arr[int(x[1:]) - 1]] = dictOfAllWord[arr[int(x[1:]) - 1]] + [individual_word]
            #creating a array by sorting listOfword dictionary (which contain the individual word as key and frequecy as value)
            list2 = sorted(listOfword.keys(), key=lambda x:listOfword[x],reverse=True)
            # print(individual_word,list2)
        # else:
            # print(individual_word,"No result found")

    #creating a dictionary that contains name of individual article as key and available word in that article as list of values
    for x,y in dictOfAllWord.items():
        if len(y) != 0:
            dictOfAllWord2[x] = y
    # print(dictOfAllWord2)

    #now ranking the article first by more number of inputed words matched and second by frequecy of that words
    while n and len(list3) < 5:
        dict4 = {}
        for x,y in dictOfAllWord2.items():
            if len(y) == n:
                ab = 0
                for i in y:
                    ab += list[int(x[1:-2]) - 1][i]
                dict4[x] = ab
        list4 = []
        list4 = sorted(dict4.keys(), key=lambda x:dict4[x],reverse=True)
        #storing it in the list3 array
        list3 += list4
        n -= 1

    FinalList = []
    #removing the k part and printing only the no. of article
    for x in list3[:5]:
        FinalList.append(x[1:-2])
    print("Articles related to your query are:- ")
    print(FinalList)
    print()
    # ranking rules that this program follows is
    # more query word matches in the article and after that it follows second rule which is the sum of all frequecy query words