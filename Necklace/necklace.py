# Made by: Cemre Süler
# https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/
import collections

def same_necklace(orig, new):
    orig_necklace = orig.lower()
    new_necklace = new.lower()
    is_same_necklace = False
    for i in range(len(orig_necklace)):
        orig_necklace = orig_necklace[-1:] + orig_necklace[:-1]
        if(orig_necklace == new_necklace):
            is_same_necklace = True
    print("Are they the same necklace: " + str(is_same_necklace))

def rotate_necklace(necklace):
    orig_necklace = necklace.lower()
    rotated_necklace = orig_necklace
    repeats = 0
    for i in range(len(orig_necklace)):
        rotated_necklace = rotated_necklace[-1:] + rotated_necklace[:-1]
        if(rotated_necklace == orig_necklace):
            repeats += 1
    print("When rotating the letters on the necklace, the necklace will be the same as the original " + str(repeats) + " times")

def check_word_list():
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