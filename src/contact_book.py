from collections import defaultdict

class ContactBook:
    def __init__(self):
        self.contacts = defaultdict(dict)

    def add_contact(self, name, phone, email=None):
        if name in self.contacts:
            print('contact already exist')
        else:
            self.contacts[name]['phone'] = phone 
            self.contacts[name]['email'] = email  
        
    def view_contact(self):
        for name , info in self.contacts.items():
            # print(f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}")
             print(f"Name: {name}")
             print(f"Phone: {info['phone']}")
             print(f"Email: {info['email']}")
             print('_' *50)

    def  delete_contact(self , name):
        if name in self.contacts:
            del self.contacts[name]
            print('contact has been deleted successfully!')    
        else:
            print('contact not found!')

    def update_contact(self , name , phone = None , email = None) :
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email    
            print('contact updated successfully')    
        else:
            print('contact not found!')


if __name__ == "__main__":
    book = ContactBook() 
      
