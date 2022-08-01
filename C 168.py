from tkinter import *
root=Tk()
root.geometry("700x700")
root.configure(background="light blue")
root.title("My Citizenship Card")
class Citizen:
    def __init__(self,name,age,dob,id_number):
        self.citizen_name = name
        self.citizen_age = age
        self.citizen_dob = dob
        self.citizen_id = id_number
        
    def add_citizen(self):
        print("Name: "+self.citizen_name)
        print("Age: "+str(self.citizen_age))
        print("Date of birth: "+self.citizen_dob)
        print("Citizen Id: "+self.citizen_id)
        print("Citizen Added")
        
        
citizen1 = Citizen("Jake",22,"17/4/2000","053198")
citizen1.add_citizen()

citizen2 = Citizen("Jennie",26,"16/1/1996","0199367")
citizen2.add_citizen()
root.mainloop()