# son = 1
# while son < 100:
#     print(son, end='\n')
#     son = son + 1
# print('salom')



# while input:
#     print('siz buni anglamaysiz ')
                          
# while input:
#     from random import randint 
# print('amallardan birini tanlang: ')
# a = ['ayirish', 'bolish', 'qoshish']

# son = 1
# for b in a:
#     print(son, '-', b, end=('\n'))
#     son += 1
    
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
#     print('qoshish')
# from random import randint
# print('amallardan birini tanlang va ozingizni sinab koring')
# a = ('ayru','bolu','qoshu','kopaytru' 


# print('kiritilgan sonni kvadratini qaytaradigan dastur.')
# savol = 'istalgan sonni kriting '
# savol += "(dasturni toxtatish uchun 'exit' deb yozing>>> ):"
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('dastur tugadi')

# print('kiritilgan sonni kvadratini qaytaradigan dastur.')
# savol = 'istalgan sonni kriting '
# savol += "(dasturni toxtatish uchun 'exit' deb yozing):"
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)++2)
# print('dastur to\`xtadi!')

# print('kiritilgan sonni kvadratini qaytaradigan dastur.')
# savol = 'istalgan sonni kriting '
# savol += "(dasturni toxtatish uchun 'exit' deb yozing):"
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break  #toxtatish
#     else:
#         print(float(qiymat)++2)
# print('dastur to\`xtadi!')

#continue otkizib yuboruvchi 
# savolar = list(range(1,11))
# for son in savolar:
#     if son == 5:
#         break
#     print (f'{son} ning kvadrati {son**2} ga teng')
    
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f'{son} ning kvadrati {son**2}ga teng')
    
# from random import random
# print('amallardan birini tanlang: ')
# a = ['ayirish', 'bolish', 'qoshish']
# print('amallardan birini tanlang:')
# savo = "(dasturni toxtatish uchun 'exit' deb yozing):"
# son = 1
# for b in a:
#         print(son, '-', b, end=('\n'))
#         son += 1
        
# savol = input('amal raqamini kriting.>>> ')
# while True:
#     if savol == '1':
#         a = random(1,11)
#         b = random(1,11)
#         print('misollarni javobini kriting:')
#         c = int(input('{} - {} =' .format(a, b)))
#         if c == (a - b):
#             print('togri :)')
#         else:
#             print('xato! :(')
#             a = random(1,11)
#             b = random(1,11)   
#             print('misollarni javobini kriting:')
#         c = int(input('{} % {} =' .format(a, b)))
#         if c == (a % b):
#             print('togri :)')
#         else:
#             print('xato! :(')
#             a = random(1,11)
#             b = random(1,11)   
#             print('misollarni javobini kriting:')
#             c = int(input('{} + {} =' .format(a, b)))
#             if c == (a + b):
#                 print('togri :)')
#             else:
#                 print('xato! :(')
# print('amallardan birini tanlang va ozingizni sinab koring')
# a = ('ayru','bolu','qoshu','kopaytru' )
    
# from random import random
# ism = input('asalomu alaykum foydalanuvchi ismingizni kriting')
# print(f'salom {ism} dasturimizga hush kelibsiz')   
# a = print('ayru,bolu,qoshu')
# input('ozingizni sinab koring')
# print('amallardan birini tanlang')
# while True:
#     a = random(1,11)
#     b = random(1,11)
#     print('misollarni javobini kriting:')
#     c = int(input('{} - {} =' .format(a,b)))
#     if c == (a - b ):
#         print('togri:)')
#     else:
#         print('xato:(')


from random import randint
ism = input('asalomu alaykum fotdalanuvchi ismingizni kriting')
savol = print(f"salom {ism}, dasturimizga hush kelibsiz dastur toxtatish uchun 'exit' deb yozing  ")
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        a = randint(1, 10)
        b = randint(1,10)
        c = int(input('{} + {} = '.format(a,b)))
        if c == (a + b):
            print('togri! :)')
        else:
            print('xato! :(')
print('dastur tugadi tshrif buyurganingiz uchun raxmat')


# son = 0
# while son<10:
#     son += 1
#     if son%2==0:
#         continue
#     else:
#         print(son)
        
    
# infinite loop;
# import math
# print('kiritilgan sonni ildizini qaytaruvchi dastur.')
# savol = 'istalgan sonni kiring'
# savol += "(dasturni toxtatish uchun 'exit' deb yozing): "
# while True:
#     son = input(savol)
#     if son == 'exit':
#         break 
#     else:
#         if  int(son) < 0:
#             print('iltimos musbat son kriting!\n')
#         else:
#             print(math.sqrt(float(son)))
# print('dastur to\`xtaydi')



# son = 0
# while son<10:
#     if son%2 !=0:
#         continue
#     else:
#         print(son)
#         son += 1

# import logging

# from aiogram import Bot, Dispatcher, executor, types

# API_TOKEN = '5612340364:AAH0nW9gic-hNo77UPYu8s_VX9C0wKuCRXM'

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.reply("salom\nmen EchoBot!\nhello world deb yozing")
    
# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)

#     await message.answer(message.text)
    
    
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True) 