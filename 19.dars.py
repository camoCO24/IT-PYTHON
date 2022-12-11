# import avto_dars_mod

# avto1 = avto_dars_mod.avto_info("GM","malibu","qora","avtomat",2020,50000)
# avto_dars_mod.info_print(avto1)



# import avto_dars_mod as adm

# avto1 = adm.avto_info("GM","malibu","qora","avto",2022,40000)
# adm.info_print(avto1)




import avto_dars_mod as adm

avto1 = adm.avto_kirit()

for avto in avto1:
    adm.info_print(avto)