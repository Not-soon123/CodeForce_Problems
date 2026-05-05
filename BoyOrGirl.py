# Recognizing user gender by username
def recognize_by_username(username):
    if len(set(username))%2 == 0:
        return "CHAT WITH HER!"
    else:      
        return "IGNORE HIM!"
username = input()
result = recognize_by_username(username)
print(result)
