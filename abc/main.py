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
# title dictionary for individual articles
T_k1,T_k2,T_k3,T_k4,T_k5,T_k6,T_k7,T_k8,T_k9,T_k10,T_k11,T_k12,T_k13,T_k14,T_k15,T_k16,T_k17,T_k18,T_k19,T_k20,T_k21,T_k22,T_k23,T_k24,T_k25,T_k26,T_k27,T_k28,T_k29,T_k30,T_k31,T_k32,T_k33,T_k34,T_k35,T_k36,T_k37,T_k38,T_k39,T_k40,T_k41,T_k42,T_k43,T_k44,T_k45,T_k46,T_k47,T_k48,T_k49,T_k50 = {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}
#list of all title dictionarys
T_List = [T_k1,T_k2,T_k3,T_k4,T_k5,T_k6,T_k7,T_k8,T_k9,T_k10,T_k11,T_k12,T_k13,T_k14,T_k15,T_k16,T_k17,T_k18,T_k19,T_k20,T_k21,T_k22,T_k23,T_k24,T_k25,T_k26,T_k27,T_k28,T_k29,T_k30,T_k31,T_k32,T_k33,T_k34,T_k35,T_k36,T_k37,T_k38,T_k39,T_k40,T_k41,T_k42,T_k43,T_k44,T_k45,T_k46,T_k47,T_k48,T_k49,T_k50]

#creating another dict for the final rule i.e perfer word that occur in starting of the document(article)
first_occ_dict_k1, first_occ_dict_k2, first_occ_dict_k3, first_occ_dict_k4, first_occ_dict_k5, first_occ_dict_k6, first_occ_dict_k7, first_occ_dict_k8, first_occ_dict_k9, first_occ_dict_k10, first_occ_dict_k11, first_occ_dict_k12, first_occ_dict_k13, first_occ_dict_k14, first_occ_dict_k15, first_occ_dict_k16, first_occ_dict_k17, first_occ_dict_k18, first_occ_dict_k19, first_occ_dict_k20, first_occ_dict_k21, first_occ_dict_k22, first_occ_dict_k23, first_occ_dict_k24, first_occ_dict_k25, first_occ_dict_k26, first_occ_dict_k27, first_occ_dict_k28, first_occ_dict_k29, first_occ_dict_k30, first_occ_dict_k31, first_occ_dict_k32, first_occ_dict_k33, first_occ_dict_k34, first_occ_dict_k35, first_occ_dict_k36, first_occ_dict_k37, first_occ_dict_k38, first_occ_dict_k39, first_occ_dict_k40, first_occ_dict_k41, first_occ_dict_k42, first_occ_dict_k43, first_occ_dict_k44, first_occ_dict_k45, first_occ_dict_k46, first_occ_dict_k47, first_occ_dict_k48, first_occ_dict_k49, first_occ_dict_k50 = {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}
first_occ_dict_list = [first_occ_dict_k1, first_occ_dict_k2, first_occ_dict_k3, first_occ_dict_k4, first_occ_dict_k5, first_occ_dict_k6, first_occ_dict_k7, first_occ_dict_k8, first_occ_dict_k9, first_occ_dict_k10, first_occ_dict_k11, first_occ_dict_k12, first_occ_dict_k13, first_occ_dict_k14, first_occ_dict_k15, first_occ_dict_k16, first_occ_dict_k17, first_occ_dict_k18, first_occ_dict_k19, first_occ_dict_k20, first_occ_dict_k21, first_occ_dict_k22, first_occ_dict_k23, first_occ_dict_k24, first_occ_dict_k25, first_occ_dict_k26, first_occ_dict_k27, first_occ_dict_k28, first_occ_dict_k29, first_occ_dict_k30, first_occ_dict_k31, first_occ_dict_k32, first_occ_dict_k33, first_occ_dict_k34, first_occ_dict_k35, first_occ_dict_k36, first_occ_dict_k37, first_occ_dict_k38, first_occ_dict_k39, first_occ_dict_k40, first_occ_dict_k41, first_occ_dict_k42, first_occ_dict_k43, first_occ_dict_k44, first_occ_dict_k45, first_occ_dict_k46, first_occ_dict_k47, first_occ_dict_k48, first_occ_dict_k49, first_occ_dict_k50]


# traversing all words of all articles
for x,kdict,title_dict,first_occ_dict in zip((range(1,51)),list,T_List,first_occ_dict_list):
    x = str(x)
    f = open("news_k50/k"+x+".txt",encoding="utf8")
    # i use for indicating the title
    i = 0
    word_no = 1
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
            # storing all word of individual article in their individual dictionary and titles in their title dict
            if word not in ignoreWordDict:
                # title dictionary
                if i == 0:
                    if word not in title_dict:
                        title_dict[word] = 1
                    else:
                        title_dict[word] += 1
                # individual dictionary
                if word in kdict:
                    kdict[word] += 1
                else:
                    kdict[word] = 1
                # first occur dict for the final rule
                if word not in first_occ_dict:
                    first_occ_dict[word] = word_no
                # storing all words of all article in AllWordDict word as key and list of article(in which the word is present) as value
                if word in AllWordDict:
                    if  "k"+x not in AllWordDict[word]:
                        AllWordDict[word] = AllWordDict[word] + ["k"+x]
                else:
                    AllWordDict[word] = ["k"+x]
            word_no += 1
        i += 1
    f.close()
# for x in T_List:
#     print(x)
#     print()

# for x in first_occ_dict_list:
    # print(x)
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

    #creating a new ranking method
    # 1st by query word all over article
    # 2nd by query word in the title
    # 3rd by freq of query word 
    # 4th by word that occur in starting of the document(article)
    list3 = []
    dict4 = {}
    for article,y in dictOfAllWord2.items():
        queryWord, titleWord, freq, first_occ = 0,0,0,float("inf")
        queryWord = len(y)
        for i in y:
            if i in T_List[int(article[1:-2]) -1]:
                titleWord += T_List[int(article[1:-2]) -1][i]
            freq += list[int(article[1:-2]) - 1][i]
            if first_occ == float("inf"):
                first_occ = first_occ_dict_list[int(article[1:-2]) -1][i]
            else:
                first_occ += first_occ_dict_list[int(article[1:-2]) -1][i]
        dict4[article] = [queryWord,titleWord,freq,first_occ]
    # print()
    # print(dict4)

    #sorting query word, freq in decreasing order and first_occ by increasing order
    list3 = sorted(dict4.keys(),key=lambda x: (dict4[x][0],dict4[x][1],dict4[x][2],-dict4[x][3]), reverse=True)

    #removing the k part and printing only the no. of articles
    FinalList = []
    for x in list3[:5]:
        FinalList.append(x[1:-2])
    
    print("Articles related to your query are:- ")
    print(FinalList)
    print()

    # ranking rules that this program follows is
    # more query word matches in the article and after that it follows second rule the more queryword matched in the title
    # and third rule which is the sum of all frequecy query words
    # fourth rule is word that occur in starting of the document(article)
    
    
    
    
 -------------------------------------------------------------------------- or -------------------------------------------------------------------------------------

# Storing all word that have to be ignored in a set
def IgnoreWord():
    f = open("english.txt",encoding="utf8")
    read = f.readlines()
    temp_list = []
    for line in read:
        temp_list.append(line.strip())
    f.close()

    ignored_word_set = set()

    for x in temp_list:
        if x not in ignored_word_set:
            ignored_word_set.add(x)
    return ignored_word_set

# removepuc will remove all the punctuation from the word and also lower case it
def RemovePunc(word):
    new_word = ""
    word = word.lower()
    for letter in word:
        if letter.isalnum():
            new_word += letter
    return new_word

# now we will loop through all article and it will store article name as key and a dict as value 
# in that inside dict individual word will be stored as key and a list of its all indexes as value
# like main_dict = {"k1" : {"katrina" : [1,3,4],"salmon":[2]}}
# in the nested dict there is a "article-title" key which will store all the title word of that particular article
# like main_dict = {"k1" : {"katrina" : [1,3,4],"salmon":[2],"article-title":["katrina","kaif"]}}
def PreProcessing():
    main_dict = {}
    for x in range(1,51):
        current_article = "k" + str(x)
        f = open("news_k50/"+current_article+".txt",encoding="utf-8")
        i = 0
        word_index = 1
        read = f.readlines()
        for line in read:
            for word in line.split():
                word = RemovePunc(word)
                if word not in ignored_word_set: 
                    if current_article not in main_dict:
                        main_dict[current_article] = {word : [word_index]}
                    else:
                        if word in main_dict[current_article]:
                            main_dict[current_article][word] += [word_index]
                        else:
                            main_dict[current_article][word] = [word_index]
                    # i is use to check if the word is in title or not
                    if i == 0:
                        if "article-title" not in main_dict[current_article]:
                            main_dict[current_article]["article-title"] = [word]
                        else:
                            main_dict[current_article]["article-title"] += [word]
                word_index += 1
            i += 1
        f.close()
    return main_dict
    # ranking rules that this program follows is
    # more query word matches in the article and after that it follows
    # second rule the more queryword matched in the title
    # and third rule which is the sum of all frequecy of query words
    # fourth rule is word that occur in starting of the document(article)
def main():
    main_dict = PreProcessing()
    while True:
        user_input = input("Enter your word:- ")
        user_input = user_input.split()
        inputed_word_list = []
        # removing all the word that has to be ignored and also punctuations
        for word in user_input:
            if word not in ignored_word_set:
                inputed_word_list.append(RemovePunc(word))
        temp_dict = {}
        # queryword means the no. of words that matches with inputed words and words in a particular article
        # title means the no. of inputed words thats in the title of an article
        # freq means the frequecy of all inputed words in a particular article
        # first_occ means the sum of all indexes of all inputed words in a particular article

        for current_article in main_dict:
            temp_dict[current_article] = [0,0,0,float("inf")]
                                       # [queryword,title,freq,first_occ]
            for word in inputed_word_list:
                if word in main_dict[current_article]:
                    # queryword
                    temp_dict[current_article][0] += 1
                    # title
                    if word in main_dict[current_article]["article-title"]:
                        temp_dict[current_article][1] += 1
                    # freq
                    temp_dict[current_article][2] += len(main_dict[current_article][word])
                    # occurr
                    if temp_dict[current_article][3] == float("inf"):
                        temp_dict[current_article][3] = main_dict[current_article][word][0]
                    else:
                        temp_dict[current_article][3] += main_dict[current_article][word][0]
            if temp_dict[current_article] == [0,0,0,float("inf")]:
                del temp_dict[current_article]

        #sorting queryword,title, freq in decreasing order and first_occ by increasing order
        temp_list = sorted(temp_dict.keys(),key=lambda x: (temp_dict[x][0],temp_dict[x][1],temp_dict[x][2],-temp_dict[x][3]), reverse=True)

        #removing the k part and printing only the no. of articles
        final_list = []
        for x in temp_list[:5]:
            final_list.append(x[1:])
    
        print("Articles related to your query are:- ")
        print(final_list)
        print()
        
ignored_word_set = IgnoreWord()
main()
