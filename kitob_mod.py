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
        return f"kitobninig nomi {self.nomi} kitobning yozuvchisi {self.get_avtor()} kitovning narxi {self.narx} kitobning varagi {self.varaq} varaq"
    
    def get_id(self):
        return self.__id
a = Ktob ("boy.ota kambagal.ota","RoberdKyosaki",100,20000)
a1 = Ktob ("bir guncha oltin","oybek",200,40000)
a2 = Ktob ("ipman","ipshoiri",3000,500)
a3 = Ktob ("lon.sin","lilhonim",100,600)
a4 = Ktob ("sionshin","nilaqio",800,300000)
a5 = Ktob ("jionshin","fioli",900,4000)
a6 = Ktob ("fekshon","lero",400,40900)
 

class KtobXona:
       """ KtobXona klass"""
       
       def __init__(self, name):
           self.name = name
           self.kitoblar = []
           
       def __reper__(self):
           return f"{self.name} KtobXona"
       
       def __len__(self):
           return len(self.Ktob)
       
           
       def __getitem__(self,index):
           return self.Ktob[index]
       
       def __setitem__(self, index, value):
           if isinstance(value, Ktob):
               self.Ktob[index] = value
               
       def add_ktob(self, *qiymat):
           for ktob in qiymat:
               if isinstance(ktob, Ktob):
                   self.kitoblar.append(ktob)
               else:
                   print("ktoblarning obyektini kiriting")
       
       def __add__(self, qiymat):
           if isinstance(qiymat, KtobXona):
               yangi_Xona = KtobXona(f"{self.name} {qiymat.name}")
               yangi_Xona.Xona = self.Ktob + qiymat.Ktob
               return yangi_Xona
           elif isinstance(qiymat, Ktob):
               self.add_Ktob(qiymat)
           else:
               return(f"KtobXonaga ga {type(qiymat)} qoshib bolmaydi")
           
       def __call__(self, *param):
           if param:
               for Ktob in param:
                   self.add_Ktob(Ktob)
           else:
                 return [Ktob for Ktob in self.Ktob]
       def get_list(self):
           return [Ktob for Ktob in self.Ktob]
       
             
Xona1 = KtobXona("elektron.ktob")
Xona2 = KtobXona("ktoblarning.yahshisi")



Xona1.add_ktob(a1, a2)
Xona2.add_ktob(a3, a4)
