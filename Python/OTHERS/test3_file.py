liste=[1,4,2,8,3,5,7,9]

for i in range(8):
    print(max(liste))
    liste.remove(max(liste))