from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    return user if user and password==user.password else None
    
