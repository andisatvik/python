class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print(self.last_name)
        print(self.eye_color)

sajid_khan = Parent("Khan","brown")
sajid_khan.show_info()

#print(sajid_khan.last_name)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

salman_khan = Child("Khan","brown","3")
#print(salman_khan.last_name)
#print(salman_khan.number_of_toys)
salman_khan.show_info()

