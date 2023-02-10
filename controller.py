
import view
import model

def start():
  user_choise=0
  while user_choise !=8:
     view.main_menu()
     user_choise =view.selected_item_menu()
     match user_choise:
           case 1:
              phone_book = model.get_phone_book()  
              view.show_contacts(phone_book)
           case 2:
                model.open_phone_book()
                view.load_success()
           case 3:
               model.save_phone_book()
               view.save_success()
           case 4:
               new=view.new_contact()
               model.update_phone_book(new)
           case 5:
               search=view.input_change_delete()
               input=view.new_and_change_contact()
               model.change_contact(search,input)
           case 6:
              search=view.input_change_delete()
              model.delete_contact(search)
           case 7:
            search = view.find_contact()
            result = model.search_contact(search)
            view.show_contacts(result)
           case 8:
              model.exit_programm()
    

