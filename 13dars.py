# python_words = {
#     'integer': 'butun son',
#     'float':'onlik son',
#     'bolean':'mantiqiy qiymati',
#     'for':'biror amalni qayta qayta bajarish tartibi',
#     'if':'shartlarni bajarish operatori',
#     'else':'akis holda tushunchasi',
#     'f(string)' : "matinlar bilan ishlash",
#     'not in' : 'shunda bolmasa'}


# davlatlar = {
#     'ozbekiston':'toshkent',
#     'aqish':'washington d.c',
#     'rossia':'moskova',
#     'tojikiston':'dushanbe',
#     'qirgiziston':'bishkek',
#     'qozoqiston':'nursulton',
#     'molazya':'kuolla-limpor',
#     'singapur':'singapur',
#     'italya':'rim'
# }



# country = input('qaysi davlatni bilishni istaysiz?: ').lower()
# capital = davlatlar.get(country)
# if capital == None:
#     print('kechirasiz, bizda haqida malumot yoq')
# else:
#     print(f'{country.upper()} ning poytahti {capital.title()}')
    
menu = {
    'osh':20000,
    'lagmon':20000,
    'non':4000,
    'choy':5000,
    'shoshlik':12000,
    'somsa':6000,
    'tabaka':15000}
narx = 0  
print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f'{n+1}-taom:').lower())
    
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        narx = narx + menu[buyurtma]
        print(f'{buyurtma.title()} {menu[buyurtma]} som')
    else:
        print(f'kechirasiz, bizda {buyurtma} yoq.')
print(f'jami: {narx}')

    
    
    