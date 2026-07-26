#with txt file
def login(username, password):
 with open ("student.txt", "w") as f:
    f.write("dua,123\n")
    f.write("ali,456\n")
    f.write("sara,789\n")
 with open ("student.txt","r") as f:
   for x in f :
     un,pwd =x.strip().split(",")
     if username == un and password == pwd:
        return "Login Successful"

 return "Login Failed"
print(login("dua","123"))


#with csv file
import csv
def login(username, password):

     with open ("student.csv", "w") as f:
      f.write("dua,123\n")
      f.write("ali,456\n")
      f.write("sara,789\n")

     with open("student.csv", "r") as f:
        reader = csv.reader(f)

        next(reader)   # Header skip karega

        for row in reader:
            user, pwd = row

            if username == user and password == pwd:
                return "Login Successful"

     return "Login Failed"

# User Input
username = input("Enter Username: ")
password = input("Enter Password: ")

print(login(username, password))
