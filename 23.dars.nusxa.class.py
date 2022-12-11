class Shaxs:
    
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
        
    def get_info(self):
        info = f"{self.ism} {self.familiya}."
        info += f"PASSPORT raqami: {self.passport}, {self.tyil} yilda tug'ilgan. "
        return info
    
    def get_age(self):
        return (2022 - self.tyil)
    
class Manzil:
    """Manzil saqlash uchun klass"""

    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
    
class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam,):
        super().__init__(ism, familiya, passport, tyil)
        
        self.idraqam = idraqam
        self.bosqich = 1
        
    
        
    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich
 
    def get_info(self):
        info = f"{self.ism} {self.familiya}."
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}."
        return info
talaba1 = Talaba('Ali', "Valiyev", "AB12345678", 2000, 'ID87643456')
talaba_m = Manzil("5/3", "Jayxun", "Yangiyer", "Sirdaryo")
print(talaba1.get_info(), talaba_m.get_manzil())