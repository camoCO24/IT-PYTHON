from uuid import uuid4

class Ktob:
    """kitob klass"""
    __num_ktob = 0
    def __init__(self, nomi, avtor, varaq, narx):
        """kitob xususyatlari"""
        self.nomi = nomi
        self.__avtor = avtor
        self.varaq = varaq
        self.narx = narx
        self.isbn = uuid4()
        Ktob.__num_ktob += 1
        
        
    @classmethod
    def get_num_ktob(cls):
        return cls.__num_ktob
    
        
    def get_nomi(self):
        return self.__nomi
    """kitobni nomini krituvchi dastur"""
    
    
    def get_avtor(self):
        return self.__avtor
    """kiobni yozuvchisi yani avtori"""
    
    
    def get_varaq(self):
        return self.varaq
    """ kitobnin nechi vaqligini bildiruvchi funksya"""
    
    def get_narx(self):
        return self.narx
    
    def get_info(self):
        """kitob haqida malumotlar"""
        return f"kitobninig nomi {self.nomi} kitobning yozuvchisi {self.get_avtor()} kitovning narxi {self.narx} kitobning varagi {self.varaq}"
    
    def get_id(self):
        return self.__id

   

   
