def convert_login(login):
    login = login[:10]
    for i in range(len(login)):
        if login[i] < 'A':
            return "Неверный логин"
        if login[i] >= 'Z':
            login = login[:i] + chr(ord(login[i]) - 32) + login[i + 1:]
    return login

def sumlog(login):
    sumlog = 0x0
    for i in range(len(login)):
        sumlog += ord(login[i])
    sumlog = sumlog ^ 0x5678
    return sumlog

def create_passwords(sumlog):
    xor = str(sumlog ^ 0x1234)
    passwords = [xor]
    for i in range(1, len(xor)):
        passwords.append(str(int(xor[:i]) - 1) + chr(int(xor[i]) + 10 + ord('0')) + xor[i + 1:])
    return passwords

def check_password(password, sumlog):
    dec_pass = 0x0
    for i in range(len(password)):
        dec_pass *= 10
        dec_pass += (ord(password[i]) - ord('0'))
    dec_pass = dec_pass ^ 0x1234
    if dec_pass == sumlog:
        return True
    else:
        return False


login = str(input())
new_login = convert_login(login)
if new_login != "Неверный логин":
    sumlog = sumlog(new_login)
    passwords = create_passwords(sumlog)
    for i in range(len(passwords)):
        if check_password(passwords[i], sumlog):
            print(passwords[i])
else:
    print(new_login)