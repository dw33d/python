import bcrypt

print("Welcome to XYZ platform! Sign up to get creating!")

# empty dictionary we are going to update user_id:private_key to
user_db = {}

user_id = input('Username: ')
private_key = input('Password: ').encode()
# Adding salt
salt = bcrypt.gensalt()
hashbrown_key = bcrypt.hashpw(private_key, salt)
user_db.update({user_id:hashbrown_key})
print(user_db)