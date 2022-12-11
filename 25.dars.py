#INCASULATSYA


from uuid import uuid4

class Avto:
    """Avto klass"""
    __num_avto = 0
    
    def __init__(self, make, model, rang, yil, narx, km=0):
        """Avtomobilning xususyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.__narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
        
    def get_narx(self):
        return self.__narx
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def set_narx(self, narx):
        """mashinaga narx ga yana narx qoshish"""
        self.__narx = narx
        
       
        
        
    def add_km(self, km):
        """MAshinaning km ga yana km qoshish"""
        if km >= 0:
            self.__km += km
        else:
            return "mashina km kamaytirib bolmaydi"
            
avto1 = Avto("GM","Malibu","Qora",2022,40000,100)
