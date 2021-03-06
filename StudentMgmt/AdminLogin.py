from StudentMgmt.DB_Operations import ConnectToDB


class AdminLogin(ConnectToDB):

    def verify_login(self, tablename, db=ConnectToDB()):
        """
            To verify the sercure login by validating the credentials given
        :param tablename:
        :param u_name:
        :param db:
        :return:
        """
        print("\n")
        print("========== Hello user. Welcome to admin page ==============")
        print("\n")
        u_name = input("Enter the username: ")
        query = "select password from " + tablename + " where username =\'" + u_name + "\'"
        fetch_password = db.display_record(query)
        count = 0
        for i in range(3):
            pwd = input("Enter the password: ")
            if pwd == fetch_password:
                print("Login is successful")
                return True
                break
            else:
                print("Incorrect password please try again")
                count = count + i
                if count > 2:
                    print("You have exceeded the limit. Try again later")
                    return False

    def add_student_record(self,tablename,u_name):
        """
         To create a new record of a student by the admin based on the input provided
        :param tablename:
        :param u_name:
        :return:
        """
        #f self.verify_login(tablename,u_name):
        print("\n")
        print(" ===============  Welcome to \'ADD STUDENT RECORD PAGE\'   =============== ")
        print("\n")
        for i in range(2):
            s_name = input("Enter student name: ")
            s_class = input("Enter class room: ")
            s_section = input("Enter section: ")
            s_id = input("Enter the id: ")
            sql_query = "insert into student_records(name, class, section, id) values (%s, %s, %s, %s)"
            sql_value = (s_name, s_class, s_section, s_id)
            try:
                dbs1 = ConnectToDB.cursors.execute(sql_query, sql_value)
                ConnectToDB.myconnection.commit()
            except Exception as e:
                print(e)
                ConnectToDB.myconnection.rollback()
        #else:
        #    print("Login is unsuccessful")

    def get_all_records(self,tablename,db=ConnectToDB()):
        print("\n")
        print("---------- Displaying all the records ------------")
        print("\n")
        db.display_all_records(tablename)


