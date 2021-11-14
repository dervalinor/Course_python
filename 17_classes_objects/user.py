#login - create a class where have the attributes and methods

#class - is like an object constructor, all classes have a __init__()
#function

#__init__() is executed automatically, whenever (cuando quiera que) we 
#create the object from this class

class User:
    #Attributes

    #create function __init__

    #"self" parameter - is a reference to the current instance of the class
    #is used to access variables that belong to the class 
    def __init__ (self, email, name, password, current_job_title): #constructor

        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title 

    #Methods
    def change_password(self, change_password): #use "self" as parameter for all the methods and create a new variable
        #function for change password
        self.password = new_password

    def  change_job_title(self, new_job):
        self.current_job_title = new_job

#create an object
user_github = User("melkor@gmail.com", "Melkor", "python3.9", "Programmer Linux")
