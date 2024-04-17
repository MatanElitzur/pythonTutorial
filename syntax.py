users: dict[int, str] = {1: 'matan', 2: 'david', 3: 'sharon'}

#user: str | None = users.get(4)

def is_user_exists(user: str | None) -> None:
    if user:
        print(f'{user} exists!')
    else:    
        print(f'no user found!')

def is_user_exists() -> None:
    user: str | None = users.get(4)
    if user:
        print(f'{user} exists!')
    else:    
        print(f'no user found!')

def is_user_exists_1() -> None:
    if user := users.get(4):
        print(f'{user} exists!')
    else:    
        print(f'no user found!')

def get_info(text: str) -> dict:
    return {'words': (words := text.split),
            'word_count': len(words),
            'char_count': len(''.join(words))}

if __name__ == '__main__':
    is_user_exists(users.get(1))
    is_user_exists(users.get(4))
    is_user_exists()
    is_user_exists_1()
    print(users)
    print(users[1])
 
    get_info('Bob')
    get_info('Hello Bob')
    get_info('My name is Bob!')
