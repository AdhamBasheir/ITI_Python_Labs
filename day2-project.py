from re import match, sub
from datetime import datetime

class User:
    def __init__(self, first_name, last_name, email, mobile, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile = mobile
        self.password = password


class Project:
    def __init__(self, title, details, target_amount, start_date, end_date, user_email, user_number):
        self.title = title
        self.details = details
        self.target_amount = target_amount
        self.current_amount = 0
        self.start_date = start_date
        self.end_date = end_date
        self.user_email = user_email
        self.user_number = user_number


class CrowdfundingApp:
    def __init__(self):
        self.users = []
        self.projects = []

    # helper functions
    def validate_name(self, name):
        return match(r'^[a-zA-Z]+', name) is not None
    
    def validate_email(self, email):
        return match(r'^[\w\.-]+@[\w-]+\.[\w-]+$', email) is not None

    def validate_mobile(self, mobile):
        return match(r'^01[0-25][0-9]{8}$', mobile) is not None

    def find_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None
    
    def find_user_by_mobile(self, mobile):
        for user in self.users:
            if user.mobile == mobile:
                return user
        return None
    
    def find_project_by_title(self, title):
        for project in self.projects:
            if project.title == title:
                return project
        return None
    
    def check_email(self, email):
        for user in self.users:
            if user.email == email:
                return True
        return False
    
    def check_mobile(self, mobile):
        for user in self.users:
            if user.mobile == mobile:
                return True
        return False
    
    def check_title(self, title):
        for project in self.projects:
            if project.title == title:
                return True
        return False

    # main functions
    def register(self):
        print('Register:')
        print('Type "Exit" to return to the main menu')
        print('_'*38,'\n')

        first_name = input('Enter your First Name: ').strip().capitalize()
        while (first_name != 'Exit'):
            if self.validate_name(first_name):
                break
            first_name = input('Name must contain Alphabets only, Please Enter again: ').strip().capitalize()
        if first_name == 'Exit':
            return None

        last_name = input('Enter your Last Name: ').strip().capitalize()
        while (last_name != 'Exit'):
            if self.validate_name(last_name):
                break
            last_name = input('Name must contain Alphabets only, Please Enter again: ').strip().capitalize()
        if last_name == 'Exit':
            return None

        email = input('Enter your Email: ').strip().lower()
        while (email != 'exit'):
            if self.validate_email(email):
                if self.check_email(email):
                    email = input('Email already Exists, Please Enter an unregistered Email:').strip().lower()
                    continue
                break
            email = input('Enter a valid Email: ').strip().lower()
        if email == 'exit':
            return None

        mobile = input('Mobile Number (Egyptian format): ').strip().lower()
        while (mobile != 'exit'):
            if self.validate_mobile(mobile):
                if self.check_mobile(mobile):
                    mobile = input('Mobile Number already Exists, Please Enter an unregistered Mobile Number (Egyptian format):').strip().lower()
                    continue
                break
            mobile = input('Enter a valid Mobile Number (Egyptian format): ').strip().lower()
        if mobile == 'exit':
            return None

        while (True):
            password = input('Enter Password: ')
            if password.lower() == 'exit':
                return None
            confirm_password = input('Confirm Password: ')
            if (password == confirm_password):
                break
            print('Passwords do not match')
        
        new_user = User(first_name, last_name, email, mobile, password)
        self.users.append(new_user)
        print(f'User {first_name} {last_name} registered successfully!\n')
        return new_user
    
    def login(self):
        print('Login:')
        print('Type "Exit" to return to the main menu')
        print('_'*38,'\n')

        while (True):
            email_mobile = input('Enter your Email or Mobile Number: ').strip().lower()
            if email_mobile == 'exit':
                return None
            password = input('Enter your Password: ')

            if match(r'^\d{11}$',email_mobile):
                user = self.find_user_by_mobile(email_mobile)
            else:
                user = self.find_user_by_email(email_mobile)

            if user and user.password == password:
                print(f'Welcome back, {user.first_name} {user.last_name}!')
                return user
            else:
                print('Invalid email/mobile or password, Please try again\n')
    
    def create_project(self, user):
        print('Create Project:')
        print('Type "Exit" to return to the main menu')
        print('_'*38,'\n')
        
        title = input('Title: ')
        title = sub(r'\s+', ' ', title).strip().title()
        while (title != 'Exit'):
            if not self.check_title(title):
                break
            title = input('Title already exists, Please Enter an unregistered Title: ')
            title = sub(r'\s+', ' ', title).strip().title()
        if title == 'Exit':
            return None

        details = input('Details: ')
        if details.strip().lower() == 'exit':
            return None

        while True:
            try:
                target_amount = float(input('Target Amount (EGP): '))
                if target_amount <= 0:
                    print('Target amount must be greater than zero, Please try again')
                else:
                    break
            except ValueError:
                print('Invalid input, Please enter a valid number for the target amount')

        while True:
            start_date_input = input('Enter Start Date (DD-MM-YYYY): ')
            if start_date_input.lower() == 'exit':
                return None
            
            try:
                start_date = datetime.strptime(start_date_input, '%d-%m-%Y')
            except ValueError:
                print('Invalid date format. Please enter the date in DD-MM-YYYY format.')
                continue
            
            while True:
                end_date_input = input('Enter End Date (DD-MM-YYYY) or "none" if it is flexible: ')
                if end_date_input.lower() == 'exit':
                    return None
                
                if end_date_input.lower() == 'none':
                    end_date = None
                    break
                
                try:
                    end_date = datetime.strptime(end_date_input, '%d-%m-%Y')
                    if end_date < start_date:
                        print('End date cannot be before start date. Please try again.')
                    else:
                        break
                except ValueError:
                    print('Invalid date format. Please enter the date in DD-MM-YYYY format.')
            
            break
        
        new_project = Project(title, details, target_amount, start_date, end_date, user.email, user.mobile)
        self.projects.append(new_project)
        print('Project created successfully!\n')
    
    def view_projects(self):
        print('All Projects:')
        for project in self.projects:
            print(f'Title: {project.title}, Current: {project.current_amount} EGP, Target: {project.target_amount} EGP')
        
    def edit_project(self, user):
        print('Edit Project:')
        print('Type "Exit" to return to the main menu')
        print('_' * 38, '\n')

        title = input('Enter the project title to edit: ').strip().title()
        title = sub(r'\s+', ' ', title).strip().title()

        project = self.find_project_by_title(title)

        if project:
            if project.user_email == user.email:
                new_title = input('New Title (Leave empty to keep the current one or type "Exit" to cancel): ').strip().title()
                if new_title == 'Exit':
                    return None
                if new_title and not self.check_title(new_title):
                    project.title = new_title

                new_details = input(f'New Details (Leave empty to keep the current one or type "Exit" to cancel): ').strip()
                if new_details == 'Exit':
                    return None
                if new_details:
                    project.details = new_details

                while True:
                    try:
                        new_target_amount_input = input(f'New Target Amount (EGP) (Leave empty to keep the current one or type "Exit" to cancel): ').strip()
                        if new_target_amount_input == 'Exit':
                            return None
                        if new_target_amount_input:
                            new_target_amount = float(new_target_amount_input)
                            if new_target_amount <= 0:
                                print('Target amount must be greater than zero, Please try again')
                            else:
                                project.target_amount = new_target_amount
                                break
                        else:
                            break
                    except ValueError:
                        print('Invalid input, Please enter a valid number for the target amount')

                new_start_date_input = input(f'New Start Date (DD-MM-YYYY) (Leave empty to keep the current one or "none" to skip, "exit" to cancel): ').strip()
                if new_start_date_input.lower() == 'exit':
                    return None
                if new_start_date_input.lower() != 'none' and new_start_date_input:
                    try:
                        project.start_date = datetime.strptime(new_start_date_input, '%d-%m-%Y')
                    except ValueError:
                        print('Invalid date format. Please enter the date in DD-MM-YYYY format.')
                        return None

                new_end_date_input = input(f'New End Date (DD-MM-YYYY) (Leave empty to keep the current one or "none" to skip, "exit" to cancel): ').strip()
                if new_end_date_input.lower() == 'exit':
                    return None
                if new_end_date_input.lower() != 'none' and new_end_date_input:
                    try:
                        project.end_date = datetime.strptime(new_end_date_input, '%d-%m-%Y')
                        if project.end_date < project.start_date:
                            print('End date cannot be before start date. Please try again.')
                            return None
                    except ValueError:
                        print('Invalid date format. Please enter the date in DD-MM-YYYY format.')

                print('Project updated successfully!\n')
            else:
                print('You cannot edit this project as You are not the owner.')
        else:
            print(f'No project found with the title "{title}"\n')


    def delete_project(self, user):
        print('Delete Project:')
        print('Type "Exit" to return to the main menu')
        print('_' * 38, '\n')

        title = input('Enter the project title to delete: ').strip().title()
        project = self.find_project_by_title(title)
        
        if project:
            if project.user_email == user.email:
                self.projects.remove(project)
                print('Project deleted successfully!\n')
            else:
                print('You cannot delete this project as You are not the owner.')
        else:
            print(f'No project found with the title "{title}"')


app = CrowdfundingApp()

while True:
    print('\nCrowd-Funding console app')
    print('_'*24)
    print('1. Register')
    print('2. Login')
    print('3. Create Project')
    print('4. View Projects')
    print('5. Edit Project')
    print('6. Delete Project')
    print('7. Logout')
    print('8. Exit')

    choice = input('\nEnter your choice: ').strip().lower()
    user = None

    match choice:
        case '1':
            user = app.register()
        case '2':
            user = app.login()
        case '3':
            if user in app.users:
                app.create_project(user)
            else:
                print('Please log in first')
        case '4':
            app.view_projects()
        case '5':
            if user in app.users:
                app.edit_project(user)
            else:
                print('Please log in first')
        case '6':
            if user in app.users:
                app.delete_project(user)
            else:
                print('Please log in first')
        case '7':
            if user:
                print(f'Goodbye, {user.first_name} {user.last_name}!')
                user = None
        case '8':
            if user:
                print(f'Goodbye, {user.first_name} {user.last_name}!')
            else:
                print('Goodbye!')
            break
        case _:
            print('Invalid choice')


