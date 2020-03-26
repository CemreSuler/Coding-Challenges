orig_necklace = input("What is the name on the original necklace: ").lower()
rotated_necklace = orig_necklace
repeats = 0
for i in range(len(orig_necklace)):
    rotated_necklace = rotated_necklace[-1:] + rotated_necklace[:-1]
    if(rotated_necklace == orig_necklace):
        repeats += 1
print("When rotating the letters on the necklace, the necklace will be the same as the original " + str(repeats) + " times")