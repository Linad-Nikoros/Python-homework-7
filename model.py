import sys

phone_book = []
path = 'phone_book.txt'

def get_phone_book():
     global phone_book
     return phone_book

def open_phone_book():
    global phone_book
    global path
    with open(path, 'r', encoding = 'UTF-8') as file:
        data = file.readlines()
        for line in data:
           phone_book.append(line.strip().split(';'))

def update_phone_book(contact: list):
   global phone_book
   phone_book.append(contact)

def save_phone_book():
    global phone_book
    global path
    data = []
    for line in phone_book:
           data.append(';'.join(line))
    with open(path, 'w', encoding = 'UTF-8') as file:
        data = file.write('\n'.join(data))
        
def search_contact(search: str):
    global phone_book
    search_results = []
    for line in phone_book:
        for field in line:
             if search in field:
                 search_results.append(line)
                            
    return search_results

def delete_contact(search):
    valid=False
    global phone_book
    for line in phone_book:
      for field in line:
        if field==search:
            phone_book.remove(line)
            print('Контакт успешно удален')
            valid=True
    if not valid:  
     print('Контакта с такими данными не существует')   

def change_contact(search : str, contact: list):
  valid=False
  global phone_book
  for line in range(len(phone_book)):
    for field in range(3):
        if phone_book[line][field]==search:
           phone_book[line]=contact
           print('Контакт успешно изменен')
           valid=True
  if not valid: 
    print('Контакта с такими данными не существует')         
           
def exit_programm():
    sys.exit()