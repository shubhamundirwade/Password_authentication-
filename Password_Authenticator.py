import getpass

database = {"shubham.undirwade": "123456", "undirwade.shubham": "6543218"}
username = input("Enter your Username: ")
password = getpass.getpass("Enter Your Password: ")

for i in database.keys():
    if username == i:
            while password != database.get(i):
                password = getpass.getpass("Enter your Password Again:")
            break
print("Verified")