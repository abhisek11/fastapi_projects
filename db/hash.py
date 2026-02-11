import bcrypt

class Hash():
    @staticmethod
    def bcrypt(password: str):
        # Convert password to bytes and hash it
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password_bytes, salt).decode('utf-8')
    
    @staticmethod
    def verify(hashed_password, plain_password):
        # Convert both to bytes for verification
        plain_password_bytes = plain_password.encode('utf-8')
        hashed_password_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(plain_password_bytes, hashed_password_bytes) 