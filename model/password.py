from datetime import datetime
from pathlib import Path
# vamos "Recriar" um ORM

class BaseModel:
    BASE_DIR = Path(__file__).resolve().parent.parent
    DB_DIR = BASE_DIR / 'db'
    
    
    
    def save(self):
        table_path = Path(self.DB_DIR / f'{self.__class__.__name__}.txt')
        if not table_path.exists():
            table_path.touch()
        
        string = ""
        
        for i in self.__dict__.values():
            string += f'{i}|'
            print(string)
            
        with open(table_path, 'a') as arq:
            arq.write(string)
            arq.write('\n')
            
    @classmethod
    def get(cls):
        # se algum dia o nome do arquivo for alterado, será alterado automaticamente 
        table_path = Path(cls.DB_DIR / f'{cls.__name__}.txt')
        
        
        if not table_path.exists():
            table_path.touch()
        
        
        
        with open(table_path, 'r') as arq:
            x = arq.readlines()
        
        
        results = []
        
        atributos = vars(cls())
        
        
        for i in x:
            split_v = i.split('|')
            tmp_dict = dict(zip(atributos, split_v))
            results.append(tmp_dict)
            #print(tmp_dict)
            #print(split_v[0])
            
        return results
            
                
                
          
            
            

class Password(BaseModel):
    def __init__(self, domain=None, password=None, expire=False):
        self.domain = domain
        self.password = password
        self.create_at = datetime.now().isoformat()
       
#p1 = Password(domain='youtube', password='abcd')
#p1.save() 
#Password.get()


        
'''           
    
print("|".join(list(map(str, self.__dict__.values()))))



print(self.__dict__.values())


w -> escreve
a -> escreve + o que ja tinha
r -> lê o que a gente cria





'''

        
#pythonando = Password(domain='Pythonando.com.br', password='1234')
#pythonando.save()