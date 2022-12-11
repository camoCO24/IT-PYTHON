# def orqali(min,max,qadam=1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# print(orqali(1,21, 2))




# def avto_info(kompanya, model,rangi,koropka, yil,narhi=None):
#     avto = {'kompani':kompanya,
#             'model':model,
#             'color':rangi,
#             'box':koropka,
#             'year':yil,
#             'price':narhi
# }
#     return avto
# print('quydagi malumotlarni kriting\n')
# avtolar = []
# while True:
#     kompani = input('kompanya nomini kriting')
#     model= input('modelini kriting')
#     color = input('rangini kriting')
#     box = input('karopkalimi yoki karopkasiz ')
#     year = input('yilini kriting')
#     price = ('narhini kriting')
#     avtolar.append(avto_info(kompani,model,color,box,year,price))
#     chiqarish = input('dasturni tohtatasizmi yes/no')
#     if chiqarish == 'yes':
#         break
#     elif chiqarish != 'yes' or 'no':
#         print('Tanlov noto\'g\'ri.')
#         break
# for avto in avtolar:
#     if avto['price']:
#         price = f"{avto['price']}$"
#     else:
#         price = 'nomalum'
#     q = (f"{avto['kompani']} {avto['model']} {avto['color']} {avto['box']} {avto['year']} {avto['price']}")
#     print(q.title())
    
    
# def talabani_bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"talaba {ism.title()} ning bahosini kriting: ")
#         baholar[ism] = int(baho)
#     return baholar


# baho  = talabani_bahola(['ali','vali','hasan','husan'])
# print(baho)    

#: kopya qilib olinuvchi degani"

# talabalar = (['ali','vali','hasan','husan'])

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"talaba {ism.title()} ning bahosini kriting: ")
#         baholar[ism] = (baho)
#     return baholar



# baholar = bahola(talabalar[:])   
# for baho  in baholar.values():
#     print(f"{talabalar.pop().title()} ning bahosi: {baho}")
    
    
# def summa(*sonlar):
#     '''kiritilgan sonni yigindisini hisoblaydigan funksya'''
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# # print(summa(1,2,3,4,5,6,7,8,9,10))
    

# def summa(x,y, *sonlar):
#     '''kiritilgan sonni yigindisini hisoblovchi dastur'''
#     return x + y + sum(sonlar)

# print(summa(5,2))
# print(summa(1,2,3,4,5))
# print(summa(9,11))

# def avto_info(kompaniya,model, **malumotlar):
#     '''avto haqidagi malumotlar lugat korinishdia qaytaradigan funksya'''
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar

# avto1 = avto_info("GM","MALIBU",rang='qora', yil =2018)
# avto2 = avto_info("kia", "k5", rang='qizil',narh=35000,yil=2000)
# print(avto1)
# print(avto2    )

# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)
#             # print(sonlar)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#             # print(sonlar[1], sonlar[2])
#     return sonlar 
# print((fibonacci(10000)))



# def avto_info(kompanya, model,rangi,koropka, yil,narhi=None):
#     avto = {'kompani':kompanya,
#             'model':model,
#             'color':rangi,
#             'box':koropka,
#             'year':yil,
#             'price':narhi
# }
#     return avto
# def avto_kirit():
#     '''foydalanuvchiga avto info funksyasi yordamida birnechta'''
#     avtolar = []
#     while True:
#         print('quydagi malumotlarni kiriting',end="")
#         kompani = input('kompanya nomini kriting')
#         model= input('modelini :')
#         color = input('rangini :')
#         box = input('karopka: ')
#         year = input('ishlab chiqarilgan yili yilini:')
#         price = input ('narhini :')
#         avtolar.append(avto_info(kompani,model,color,box,year,price))
#         javob = input('yana avto qoshasizmi? (yes/no): ')
#         if javob == 'no':
#             break
#     return avtolar

# def info_print(avto_info):
#     '''avtomabillar haqida malumotlar saqlangan lugatni konsolga chiqaruvchi funksya'''
#     print(
#         f"{avto_info['range'].title()} {avto_info['kompaniya'].upper()}"
#         f"{avto_info['model'].upper()}, {avto_info['kompaniya'].upper()}"
#         f"{avto_info['yil']}-yil, {avto_info['narhi']}$")
    
# print(avto_kirit())

    



