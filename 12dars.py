
# talaba_1 = {}
# talaba_1['ism'] = 'kamron'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# print(talaba_1)
# printq

# sonlar = {}
# a_1 = int(input("a>>>  "))
# b_1 = int(input("b>>>  "))
# sonlar["a"] = a_1
# sonlar['b'] = b_1
# print(sonlar)

# print(f"a = {sonlar['a']}")





# talaba_0 = {
#     'ism':'alijon',
#     'familya':'shamshiyov',
#     'yosh':20,
#     'fakultet':'matimatika',
#     'kurs':4}
# # key = input('kalit soz kriting: ')
# # if key.lower() in talaba_0:
    
    
#     print(talaba_0[key])
# else:
#     key = input('bunday kalit suz mavjut emas iltimos kalit soz va qiymat kriting.\nkey>>>  ')
    
#     value = input('value>>>  ')
#     talaba_0[key] = value
#     print(f"{key} -- {talaba_0[key]}")
    
# telefonlar = {
#         'ali':'iphone x',
#         'vali':'galihi s9',
#         'olim':'mi 10 pro',
#         'orif':'nokia 3310'}

# for kalit, qiymat in talaba_0.items():
#     print(f"kalit: {kalit}")
#     print(f"qiymat: {qiymat} \n")
    
# for key, value in telefonlar.items():
#     print(f"{key.title()}ning telifoni {value}")
    
mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000}
# print(mahsulotlar.keys())
print('do\'kondagi mahsulotlar: ')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())
bozorlik = ['anor','uzum','not','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} som ")

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"iltimos, dokoningizga {buyum} ham olib keling")
        