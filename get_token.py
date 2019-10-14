import gkeepapi

email = input('Email: ')
password = input('Password: ')

keep = gkeepapi.Keep()
keep.login(email, password)

print(f'Token: {keep.getMasterToken()}')
