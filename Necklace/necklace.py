orig_necklace = input("What is the name on the original necklace: ").lower()
new_necklace = input("What is the name on the necklace with rotated letters: ").lower()
same_necklace = False
for i in range(len(orig_necklace)):
    orig_necklace = orig_necklace[-1:] + orig_necklace[:-1]
    if(orig_necklace == new_necklace):
        same_necklace = True
print("Are they the same necklace: " + str(same_necklace))