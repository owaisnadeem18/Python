# Railways Form details 

class railway_form:
    form_type = 'Railway Form'
    def show_data(self):
        print(f"Name of passenger is {self.name}")
        print(f"Name of train is {self.train}")

owais_appplication = railway_form()
owais_appplication.name = 'Owais'
owais_appplication.train = 'Shalimar Express' 
owais_appplication.show_data()