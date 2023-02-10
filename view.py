def main_menu():
  commands = ['Показать все контакты', 
             'Открыть файлы',
             'Сохранить файлы',
             'Новый контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Поиск контакта',
             'Выйти из программы']
  
  print('Выберите пункт меню: ')

  for i in range(len(commands)):
    print(f'\t{i+1}.{commands[i]}')
    

def selected_item_menu():
 valid=False
 while not valid:
     user_input = input('Введите пункт меню:')
     try: 
       user_input = int(user_input)
     except:
         print('Некорректный ввод. Вы уверены, что ввели число?')  
         continue
     if user_input <= 8:
      valid=True
      return user_input
     else:
      print('Введите число от 1 до 8')


def show_contacts(phone_book: list):
  if len(phone_book) > 0:
    for item in phone_book:
      print(*item)
  else:
   print('Телефонная книга пуста')
   
def load_success():
 print('Телефонная книга успешно загружена')

def save_success():
  print('Телефонная книга  успешна сохранена')

def find_contact():
  search=input('Введите искомое значение:')
  return search

def new_and_change_contact():
 new_name = input('Введите Имя и Фамилию контакта: ')
 new_phone = input('Введите  номер телефона контакта: ')
 new_comment = input('Введите  комментарий контакта: ')
 return new_name,new_phone,new_comment

def input_change_delete():
 search=input('Введите номер телефона или полное имя для удаления/именения контакта: ')
 return search