class Avto:
    __num_avto = 0
    """Avtomabil klass"""
    
    def __init__(self, make,model, rang, yil, narh, km=100):
        """Avtomabil husuyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        Avto.__num_avto += 1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
    def get_km(self):
        return self.__km
    
    def __str__(self):
        """Obyekt haqida malumot"""
        return f"Avto: {self.make} {self.model} {self.narh}$"
    
    def __repr__(self):
        """Obyekt haqida malumod"""
        return f"Avto: {self.make} {self.model}. {self.narh}$"
     
    def __gt__(self, y):
        return self.narh > y.narh
    
    def __lt__(self, y):
        return self.narh < y.narh
    
    def __le__(self, boshqa_avto):
        return self.narh <= boshqa_avto.narh
    
    def __ge__(self, boshqa_avto):
        return self.narh >= boshqa_avto.narh
    
    def __eq__(self, boshqa_avto):
        return self.narh == boshqa_avto.narh
    def __ne__(self,boshqa_avto):
        return self.narh != boshqa_avto.narh
    def get_info(self):
        return(
            f"{self.rang} {self.make} {self.model}.{self.yil}-yil. Narhi:{self.narh}$"
        )
    
avto = Avto("BMW", "x7", "qora", 2022, 40000)
avto1 = Avto("GM", "malibu", "qora",2020,60000)
avto2 = Avto("GM","lacceti","oq",2022,20000)
avto3 = Avto("GM", "malibu", "qora",2020,30000)
avto4 = Avto("GM", "malibu", "qora",2020,1000000)
avto5 = Avto("GM", "malibu", "qora",2020,60000)
avto6 = Avto("GM", "malibu", "qora",2020,5000)





class AvtoSalon:
    """Avtosalon klass"""
    
    def __init__(self, name):
        self.name = name
        self.avtolar = []
        
    def __reper__(self):
        return f"{self.name} avto salon"
        
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self, index, value):
        if isinstance(value, Avto):
            self.avtolar[index] = value
            
    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyektini kiriting")
                
salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("Avto Lider")
salon3 = AvtoSalon("Sam Avto")


salon1.add_avto(avto1, avto2, avto3)
salon2.add_avto(avto4, avto5, avto6)
salon3.add_avto(avto)


















