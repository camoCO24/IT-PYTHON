# def talaba_ism_yasa(ism,familya ):
#     '''talaba haqida funksyalar'''
#     talaba_haqida = f"{ism} {familya}"
#     return talaba_haqida.title()

# talaba1 = talaba_ism_yasa('olim','hakimov')
# talaba2 = talaba_ism_yasa('hakim','olimov')
# print(f"darsga kelmagan talabalar : {talaba1} va {talaba2} ")
# print(f"{talaba1} darsga kechikib keldi")


# def toliq_ism(ism,familya,otasini_ismi="" ):
#     '''talaba haqida funksyalar'''
#     if otasini_ismi:
#         toliq_ism(f"{ism},{familya}, {otasini_ismi}")
#     else:
#         talaba_haqida = f"{ism} {familya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism('olim','hakimov')
# talaba2 = toliq_ism('hakim','olimov')
# print(f"darsga kelmagan talabalar : {talaba1} va {talaba2}, 'kamoliddin' ")
# print(f"darsga kelmagan oquvchilar")

# def avto_info(kompanya, model,rangi,koropka, yil,narhi=None):
#     avto = {'kompani':'kompanya',
#             'model':model,
#             'color':rangi,
#             'box':koropka,
#             'year':yil,
#             'price':narhi
# }
#     return avto

# avto1 = avto_info('GM', 'molibu','qora','aftomat',2018)
# avto2 = avto_info('GM', 'gentra','oq','mexanika',2016,15000)
# avtolar = [avto1,avto2]
# print('onlayn bozordagi mavjut avtomoshinalar:')
# for avto in avtolar:
#     if avto['price']:
#         narh = f'{avto["price"]}$'
#     else:
#         narh = 'nomalum'
#     print(f"{avto['color']} {avto['model']}, narh: {narh}")
    
    
# def oraliq(min,max):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# print(oraliq(1,10))
# print(oraliq(10,21))
    
    
    
    
    
    
    
    
    