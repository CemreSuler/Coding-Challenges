import collections
word_list = []
rotated_word_list = []
file = open ("enable1.txt", "r")
for item in file:
    word_list.append(item)
for z in range(len(word_list)):
    word_list[z] = word_list[z].replace('\n', '')
for i in range(len(word_list)):
    orig_necklace = word_list[i]
    for x in range(len(orig_necklace)):
        orig_necklace = orig_necklace[-1:] + orig_necklace[:-1]
        rotated_word_list.append(orig_necklace)
match_list = [item for item, count in collections.Counter(rotated_word_list).items() if count == 4]
for g in range(len(match_list)):
    if(match_list[g] in word_list):
        print(match_list[g])