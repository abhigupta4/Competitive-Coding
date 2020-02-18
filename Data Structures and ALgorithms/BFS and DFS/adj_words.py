def check_adj(word1, word2):
    count = 0
    for i in xrange(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    if count == 1:
        return 1
    else:
        return 0


visi = {'toon':1}
ans = 100

def count_steps(cur_word, end_word, steps, dict1):
    print cur_word
    for ele in dict1.keys():
        if ele not in visi and check_adj(cur_word,ele):
            if ele == end_word:
                global ans
                ans = min(ans, steps+1)
                return
            else:
                visi[ele]=1
                count_steps(ele,end_word,steps+1,dict1)

    return

dict1 = {'poon':1,'plee':1,'same':1,'poie':1,'plie':1,'poin':1,'plea':1}
print dict1.keys()
count_steps('toon','plea',0, dict1)
print ans




