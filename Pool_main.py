
print(" ****************")
print(" * UOH POOL POS *")
print(" ****************")

class User:
    def __init__(self,name,userID,account_type):
        self.name = name
        self.userID = userID
        self.account_type = account_type
    def __repr__(self):
        return (f"{self.name} {self.account_type}")

user_dict = {
"903":User("Josh F.","903","Admin"),
"221":User("Rora H.","221", "Admin"),
"697":User("Hayden P.","697","Standard"),
"210":User("Helen H.","210", "Standard"),
"969":User("Ian C.", "696", "Standard"),
"231":User("Rachel H.","231","Standard")
}

choice = str(input("Please enter login: "))

print(user_dict[choice])

#if choice == self.userID:
    #print(self.name)
