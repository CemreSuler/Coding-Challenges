# Made by: Cemre Süler
# https://www.reddit.com/r/dailyprogrammer/comments/dv0231/20191111_challenge_381_easy_yahtzee_upper_section/

#O(N^2) (slower)
def yahtzee_upper(throw):
    results = []
    for i in range(1,len(throw)+1):
        current_result = 0
        for x in range(len(throw)):
            if(i == throw[x]):
                current_result += i
        results.append(current_result)
    print("The maximum score possible for the throw " + str(throw) + " is " + str(max(results)))

#O(N) (faster)
def yahtzee_upper_efficient(throw):
    results = []
    for i in range(0,1000000000):
        results.append(0)
    for i in range(len(throw)):
        results[throw[i]] += throw[i]
    print("The maximum efficient score possible for the throw " + str(throw) + " is " + str(max(results)))

throw_list = []
file = open ("list.txt", "r")
for item in file:
    throw_list.append(item)
for z in range(len(throw_list)):
    throw_list[z] = throw_list[z].replace('\n', '')
for f in range(len(throw_list)):
    throw_list[f] = int(throw_list[f])
yahtzee_upper_efficient(throw_list)