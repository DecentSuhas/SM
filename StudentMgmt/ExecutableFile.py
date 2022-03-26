from StudentMgmt import Config
from StudentMgmt.AdminLogin import AdminLogin
from StudentMgmt.Excel_Operations import export_students_records, generate_barGraph_StudentsCount, import_by_row
from StudentMgmt.StudentLogin import StudentLogin
from StudentMgmt.StudentSignUp import StudentSignUp

get_feature = Config.FEATURE


def login_as_admin():
    options = {'Option 1': 'Print student records', 'Option 2': 'Print student details',
               'Option 3': 'Add a new student record', 'Option 4': 'Download record',
               'Option 5': 'Upload record', 'Option 6': 'Show graph'}
    tests = AdminLogin()
    if tests.verify_login("admin_credentials", "admin"):
        print("=========== Welcome to admin page ============")
        print("Please select any option from the below")
        for item in options.items():
            print(item)
        option_selected = input("Enter your options: ")
        if option_selected == 'Print student records':
            tests.get_all_records("student_records")
        elif option_selected == 'Print student details':
            tests.get_all_records("student_details")
        elif option_selected == 'Add a new student record':
            tests.add_student_record("admin_credentials", "admin")
        elif option_selected == 'Download record':
            export_students_records("student_records", "admin")
        elif option_selected == 'Show graph':
            generate_barGraph_StudentsCount()
        elif option_selected == 'Upload record':
            import_by_row("student_records")
        else:
            print("Sorry invalid entry, Try again next time")


def login_as_student():
    options = {'Option 1': 'Have an account', 'Option 2': 'New user', }
    sing_in = StudentLogin()
    sing_up = StudentSignUp()
    print("Hello.. please select any option from the below")
    for item in options.items():
        print(item)
    option_selected = input("Type your option: ")
    if option_selected == 'Have an account':
        sing_in.displayDetails()
    elif option_selected == 'New user':
        sing_up.student_signup()
    else:
        print("Invalid entry, please try again later")


def call_to_action(feature):
    if feature == 'Admin':
        login_as_admin()
    elif feature == 'Student':
        login_as_student()


call_to_action(get_feature)
