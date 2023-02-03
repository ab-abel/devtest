from passlib.context import CryptContext

pwt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#static method help calling an instance of a class without having to instaintiate the class before the call
class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwt_context.verify(plain_passworf, hashed_password)
    
    @staticmethod
    def get_password_hash(plain_password):
        return pwt_context.hash(plain_password)
