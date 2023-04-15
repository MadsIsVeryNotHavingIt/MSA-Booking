class menu():
    '''Class for interpreting user inputs.'''
    def __init__(self):
        ()
    
    def boot(self):
        '''Prompts the user to log in using their staff details. Launches main menu subroutine'''

        print("Hello.\n")

        valid = None
        while valid is not True:
            option = input("Select; \n 1. Login \n 2. Create Login \nEnter:")
            try:
                option = int(option)
                if option is int and (option == 1 or option == 2):
                    valid = True
            except ValueError:
                print("\nError; please enter an integer choice.\n")
            except:
                print("\nError; please enter a value corresponding to your choice.")

            if option == 1:
                print("Launching login...")
                menu.login()
            if option == 2:
                print("Launching new login...")
                menu.create_login()

    def login(self):
        