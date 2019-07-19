#Connection
from pymongo import MongoClient
client = MongoClient(host="localhost", port=27017)
mydb = client["TesGO"]
Stock = mydb["Item"]
People = mydb["People"]

#Store function
class Store():
    #Search for a single item
    def SearchOneItem():
        itemName = input("Enter the name of the product here").lower()
        myquery = {"Name": itemName}
        doc = Stock.collection.find_one(myquery)
        if doc is not None:
            print(doc)
        else:
            print("Product not found: " + itemName)

    #Search for lots of Items
    def SearchAllItems():
        search = Stock.collection.find()
        count = 0
        for itemName in search:
            print(itemName)
            count = count + 1
        print(str(count) + " total products")

    #Add an item
    def AddCopy():
        itemName = input("Enter the name of the product here").lower()
        myquery = {"Name": itemName}
        doc = Stock.collection.find_one(myquery)
        if doc is not None:
            print(itemName + " is already exist in stock")
        else:
            itemPrice = int(input("Enter the price of the product here"))
            itemCopy = int(input("Enter the number of products here"))
            item = {"Name": itemName, "Price": itemPrice, "Copy": itemCopy}
            new_id = Stock.collection.insert_one(item)
            print("Inserted item with id %s" % new_id.inserted_id)

    #Remove an item
    def DelCopy():
        itemName = input("Enter the name of the product here").lower()
        item = {"Name": itemName}
        results = Stock.collection.delete_many(item)
        if results.deleted_count != 0:
            print("\nDeleted %d item" %(results.deleted_count))
        else:
            print("There is no product named " + itemName)

    #Update item Count
    def UpCopy():
        itemName = input("Enter the name of the product here").lower()
        myquery = {"Name": itemName}
        doc = Stock.collection.find_one(myquery)
        if doc is not None:
            newCount = int(input("Enter the new amount here"))
            myquery = {"Name": itemName}
            newvalues = {"$set": {"Copy": newCount}}

            result = Stock.collection.update_many(myquery, newvalues)
            print("%d documents matched, %d documents updated" % (result.matched_count, result.modified_count))

        else:
            print(itemName + " does not exist in stock")

    #Update item Price
    def UpCost():
        itemName = input("Enter the name of the product here").lower()
        myquery = {"Name": itemName}
        doc = Stock.collection.find_one(myquery)
        if doc is not None:
            newPrice = int(input("Enter the new cost here"))
            myquery = {"Name": itemName}
            newvalues = {"$set": {"Price": newPrice}}

            result = Stock.collection.update_many(myquery, newvalues)
            print("%d documents matched, %d documents updated" % (result.matched_count, result.modified_count))
        else:
            print(itemName + " does not exist in stock")

#Employee function
class Employee():
    #Find all staff detail
    def FindAllStaff():
        search = People.collection.find()
        count = 0
        for staffName in search:
            print(staffName)
            count = count + 1
        print(str(count) + " total Employees")

    #Add staff record
    def AddStaff():
        staffName = input("Enter the name of the employee here").lower()
        myquery = {"Name": staffName}
        doc = People.collection.find_one(myquery)
        if doc is not None:
            print(staffName + " already exist in the records")
        else:
            staffRole = input("Enter the role of the employee here").lower()
            staffSalary = int(input("Enter the salary of employee here"))
            ppl = {"Name": staffName, "Role": staffRole, "Salary": staffSalary}
            new_id = People.collection.insert_one(ppl)
            print("Inserted Employee with id %s" % new_id.inserted_id)

    #Delete staff record
    def RemoveStaff():
        staffName = input("Enter the name of the employee here").lower()
        ppl = {"Name": staffName}
        results = People.collection.delete_many(ppl)
        if results.deleted_count != 0:
            print("\nRemoved %d employee" % (results.deleted_count))
        else:
            print("There is no employee named " + staffName)

    #Update staff record
    def UpdateStaff():

    #Update role of staff
    def UpdateRole():

    #Update staff salary
    def UpdateSalary():

#Program Start
user = input("Please enter your Username").lower()
while user != "exit":
    role = input("Enter Role here").lower()#needs to change
    if role == "tilloperator":
        action = input("How can I help you? (FindItem, LogOut)").lower()
        while action != "log out":
            if action == "finditem":
                search = input("Would you like to find a item or all items?(one, all)").lower()
                if search == "one":
                    Store.SearchOneitem()
                elif search == "all":
                    Store.SearchAllitems()
                else:
                    print("Please enter a valid action")
            else:
                print("Please enter a valid action")
    elif role == "storemanager":
        action = input("How can I help you? (AddItem, RemoveItem, LogOut)").lower()
        while action != "log out":
            if action == "additem":
                Store.AddCopy()
            elif action == "removeitem":
                Store.DelCopy()
            else :
                print("Please enter a valid action")
    elif role == "stockcontroller":
        action = input("How can I help you? (UpdateStock, LogOut)").lower()
        while action != "log out":
            if action == "updatestock":
                Store.UpCopy()
            else:
                print("Please enter a valid action")
    elif role == "financialconsultant":
        action = input("How can I help you? (UpdatePrice, LogOut)").lower()
        while action != "log out":
            if action == "updateprice":
                Store.UpCost()
            else:
                print("Please enter a valid action")
    else:
        print("You do not have permission to access this program")
    role = input("Enter Role here").lower()#needs to change
