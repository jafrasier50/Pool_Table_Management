
print(" ****************")
print(" * UOH POOL POS *")
print(" ****************")


table_dict = {
"1":("status"),
"2":("status"),
"3":("status"),
"4":("status"),
"5":("status"),
"6":("status"),
"7":("status"),
"8":("status"),
"9":("status"),
"10":("status"),
"11":("status"),
"12":("status"),
"13":("status")
}



class User:
    def __init__(self,name,userID):
        self.name = name
        self.userID = userID
        self.account_type = 'standard'
        self.select_action()

    def select_action(self):
        action = int(input("Select User Action: (1,2,3): "))

        if action == 1:
            self.view_tables_status()
        elif action == 2:
            self.assign_table()
        elif action == 3:
            self.pay_close_table()
        else:
            print("Invalid Input")

    def view_tables_status(self):
            print (table_dict)

    # def assign_table():
    #     int(input("Please Enter table #: "))
    #
    #
    # def pay_close_table():
    #     int(input("please enter Table#: "))
    #         print(occupied_tables)

    def __repr__(self):
        return (f"{self.name} {self.account_type}")

class Admin_User(User):
    def __init__(self, name, userID):
        super().__init__(name, userID)
        self.account_type = 'admin'
    #
    # def refund_table():
    #
    # def close_report():



    def __repr__(self):
        return (f"{self.name} {self.account_type}")

class All_Tables:
    def __init__(self,ID, status):
        self.id = ID
        self.status = status
        self.spawn_table = []


    def __repr__(self):
        return (f"{self.ID} {self.status}")



user_dict = {
"903": { 'user_class': Admin_User, 'name': 'joshypooo' },
"102": { 'user_class': User, 'name': 'kendrikl' }
}


#if choice == self.userID:
    #print(self.name)
# start program
user_id = str(input("Please enter user id: "))
the_user = user_dict[user_id] # still just a class

#instantiate user
the_user['user_class'](the_user['name'], user_id)


print("1. View Tables/Status")
print("2. Assign Table")
print("3. Pay/Close Table")
