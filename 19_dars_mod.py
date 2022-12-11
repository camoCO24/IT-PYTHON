
def avto_info(kompanya, model,rangi,koropka, yil,narhi=None):
    avto = {'kompani':kompanya,
            'model':model,
            'color':rangi,
            'box':koropka,
            'year':yil,
            'price':narhi
}
    return avto
def avto_kirit():
    '''foydalanuvchiga avto info funksyasi yordamida birnechta'''
    avtolar = []
    while True:
        print('quydagi malumotlarni kiriting',end="")
        kompani = input('kompanya nomini kriting')
        model= input('modelini :')
        color = input('rangini :')
        box = input('karopka: ')
        year = input('ishlab chiqarilgan yili yilini:')
        price = input ('narhini :')
        avtolar.append(avto_info(kompani,model,color,box,year,price))
        javob = input('yana avto qoshasizmi? (yes/no): ')
        if javob == 'no':
            break
    return avtolar

def info_print(avto_info):
    '''avtomabillar haqida malumotlar saqlangan lugatni konsolga chiqaruvchi funksya'''
    print(
        f"{avto_info['range'].title()} {avto_info['kompaniya'].upper()}"
        f"{avto_info['model'].upper()}, {avto_info['kompaniya'].upper()}"
        f"{avto_info['yil']}-yil, {avto_info['narhi']}$")
    