import string, secrets
import hashlib
import base64
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

class FernetHasher:
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase
    # Path(__file__) pega a raiz do meu projeto
    BASE_DIR = Path(__file__).resolve().parent.parent
    KEY_DIR = BASE_DIR / 'keys'
    
    
    # cls é para instancia de classe, self é para metodos de instancia 
    def __init__(self, key):
        
        if not isinstance(key, bytes):
            key = key.encode()
        
        self.fernet = Fernet(key)
        
        
    # a biblioteca pathlib trabalha com diretórios em Python
    # a biblioteca secrets trabalha com criptografia
    @classmethod
    def _get_random_string(cls, length = 25):
        string = ''
        for i in range(length):
            string = string + secrets.choice(cls.RANDOM_STRING_CHARS)
        return string
    
    
    # mudar uma string para um byte
    @classmethod
    def create_key(cls, archive = False):
        value = cls._get_random_string()
        value = value.encode('utf-8')
        
        hasher = hashlib.sha256(value).digest()
        
        key = base64.b64encode(hasher)
        if archive:
            return key, cls.archive_key(key)
        return key, None
        
    @classmethod    
    def archive_key(cls, key):
        file = 'key.key'
        while Path(cls.KEY_DIR / file).exists():
            file = f'key_{cls._get_random_string(length = 5)}.key'
        # with é contexto wb = write binary
        with open(cls.KEY_DIR / file, 'wb') as arq:
            arq.write(key)
        return cls.KEY_DIR / file
    
    def encrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()
        return self.fernet.encrypt(value)
    
    def decrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()
            
        try:
            return self.fernet.decrypt(value).decode()
        except InvalidToken as e:
            return 'Token inválido'
    
    
fernet_caio = FernetHasher('vpat/3ybd/MPc3S+S6cNlJqZdptooPv8X85JhhGRWkE=')
print(fernet_caio.decrypt('gAAAAABnJCJ4hNH4XWdg_uIOwvSL2k6RpCQxbSomkjvo9JB80StXzfTVy0cSv5MZle1pqb0lu3MU4g8-50UPSAY7coS7zh4GnA=='))
            
#fernetHasher = FernetHasher()

# joao e marcos vão ter criptografias diferentes porque as chaves são diferentes
#fernet_joao = FernetHasher('1234')
#fernet_marcos = Fernet('abcd')

#FernetHasher.create_key(archive = True)

        
#FernetHasher.create_key(archive = True)
'''    
FernetHasher.create_key()
print(FernetHasher.KEY_DIR)

string = ''
for i in range(25):
    string = string + secrets.choice(cls.RANDOM_STRING_CHARS)
return string
        
chave = FernetHasher._get_random_string()

print(chave)'''