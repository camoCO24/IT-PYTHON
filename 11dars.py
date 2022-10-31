# son = int(input('juft son kriting: '));print('rahmat') if son % 2 == 0 else print ('xato')
 #bita listga kritish kodlarni

# son = int(input('istalgan butun son kriting: '))
# for n in range(2,11):
      # if not (son % n):
#         print(f'{son} soni {n} ga qoldiqsiz bolinadi')
        
# yosh = '18'
# print(yosh.isdigit())
# yosh =  input('yoshingiz nechida? ')
# if yosh.istigit():
#     yosh = float(yosh)
# else:
#     print('matinli raqam  ')


# # while True          #tohtamaydi dastur
# from random import randint
# a = randint(1, 10)
# b = randint(1,10)
# c = int(input('{} + {} = '.format(a,b)))
# if c == (a + b):
#     print('togri! :)')
# else:
#     print('xato! :(')


# # print()

# from random import randint
# son =input(f'ozingizni sinab koring: 1.kopaytru  2.bolu  3.qoshu  4.ayru  ? ')
# if son == '1':
#     a = randint(1, 11)
#     b = randint(1,11)
#     c = int(input('{} * {} = '.format(a,b))) 
# elif c == (a * b):
#     print('togri! :)')
# else:
#     print('xato! :(')
# if son == '2':
#     a = randint(1, 11)
#     b = randint(1,11)
#     c = int(input('{} % {} = '.format(a,b)))
# if c == (a % b):
#     print('togri! :)')
# else:
#     print('xato! :(')
# if son == '3':
#     a = randint(1, 11)
#     b = randint(1,11)
#     c = int(input('{} + {} = '.format(a,b)))
# if c == (a + b):
#     print('togri! :)')
# else:
#     print('xato! :(')
# if son == '4':
#     a = randint(1, 11)
#     b = randint(1,11)
#     c = int(input('{} - {} = '.format(a,b)))
# if c == (a - b):
#     print('togri! :)')
# else:
#     print('xato! :(')

# #     print()

from random import randint 
print('amallardan birini tanlang: ')
a = ['ayirish', 'bolish', 'qoshish']

son = 1
for b in a:
    print(son, '-', b, end=('\n'))
    son += 1
    
# savol = input('amal raqamini kriting.>>> ')
# if savol == '1':
#     a = randint(1,11)
#     b = randint(1,11)
#     print('misollarni javobini kriting:')
#     c = int(input('{} - {} =' .format(a, b)))
#     if c == (a - b):
#         print('togri :)')
#     else:
#         print('xato! :(')
# elif savol == '2':
#     print('bolish')
# elif savol == '3':
# #     print('qoshish')
# from random import randint
# print('amallardan birini tanlang va ozingizni sinab koring')
# a = ('ayru','bolu','qoshu','kopaytru' )

# son = 1
# for b in a:    
#     print(son, '-', b, end=('\n'))
#     son += a 
    
# savol = input('amal raqamini kritin.>>> ')
# if savol == '1': 
#     a = randint(1,11)
#     b = randint(1,11)
#     print('misollarni javobini kriting:')
#     c = int(input('{} - {} =' .format(a, b)))
#     if c == (a - b):
#         print('togri :)')
#     else:
#         print('xato! :(')
# elif savol == '2':
#     print('bolu')
# elif savol == '3':
#     print('qoshu')
# elif savol == '4':
#     print('kopaytru')

# car = {'model': 'ferari', 'rang': 'qizil'}
# print(car['model'])
# print(car['rang'])

# talaba_0 = {
#      'ism': 'kamron yusupov',
#      'yosh': 22,
#      't_yil': 2008
# }
# print(f"{talaba_0['ism'].title()}, {talaba_0['t_yil']}-yilda tugilgan, {talaba_0['yosh']}yoshda")

# talaba_1 = {}
# talaba_1['ism'] = 'kamron'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# print(talaba_1)
# printq

sonlar = {}
a_1 = int(input("a>>>  "))
b_1 = int(input("b>>>  "))
sonlar["a"] = a_1
sonlar['b'] = b_1
print(sonlar)

print(f"a = {sonlar['a']}")