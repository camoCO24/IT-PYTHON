
# file = open("pi.txt")
# PI = file.read()
# print(PI)
# file.close()





# with open("pi.txt") as file:
#     pi = file.read()
    
# # print(pi)

# pi = pi.rstrip()
# pi = pi.replace("\n", "")
# pi = float(pi)
# print(pi)


# filename = "data/talabaw.txt"
# with open(filename) as file:
#     for line in file:
#         print(line)
        
        
# with open(filename) as file:
#     talabalar = file.readlines()
    
# print(talabalar)
# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)




faylnomi = "new_file.txt"
ism = "Umar Usmonov"
tyil = 1999
with open(faylnomi, "w") as fayl:
    fayl.write(ism + '\n')
    fayl.write(str(tyil) + '\n')




import pickle

talaba1 = {"ism": "hasan", "familya": "husanov", "tyili": "2000"}
talaba2 = {"ism": "hasan", "familya": "husanov", "tyili": "2000"}
with open("info1", "wb") as file:
    pickle.dump(talaba1, file)
    
with open("info1", "rb") as file:
    talaba_1 = pickle.load(file)
    # talaba_2 = pickle.load(file)
print(talaba_1)
#print(talaba_2)












