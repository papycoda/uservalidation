import random #imports the random module
import string #imports the string module

company_database = {}


#def randomString(stringLength=5):  # function to create the random string to be added
    #ending = string.ascii_lowercase
    #return ''.join(random.choice(ending) for i in range(stringLength))


def checker():
    if confirm == "Y":
        pass
    elif confirm == "N":
        userinp = input("please enter your preferred secret password:")
        if len(userinp) < 7:
            print("length must not be shorter than 7 characters please retry")
            userinp = input("please enter your preferred secret password:")
        else :
            company_database.update({'password': userinp})
    else:
        pass

not_last_user = True

while not_last_user:
    firstname = input("please enter your first name: ")
    lastname = input("please enter your last name: ")
    ending = string.ascii_lowercase
    combo = (firstname[:2] + lastname[:1:-1])+''.join(random.choice(ending) for i in range(5))
    #random = randomString()
    print("your auto-generated password is: ", combo) #+ random)
    password = combo #+ random)
    confirm = input("are you satisfied with the password or you would like to create yours?, please press Y for yes ,N for no(to create yours): ")
    confirm = confirm.upper()
    checker()
    company_database[firstname] = lastname
    company_database[lastname] = password
    print ("Thank You, \nAre you the final user though??")
    redo = input("please press Y for yes ,N for no: ")
    redo = redo.upper()
    if redo == "Y":
        not_last_user =False

    print(company_database\
