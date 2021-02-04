#BLL
class Customer:
    listcus=[]
    def __init__(self):
        self.id=0
        self.age=0
        self.name=""
    def addCustomer(self):
        Customer.listcus.append(self)
    def searchCustomer(self):
        for e in Customer.listcus:
            if(e.id==self.id):
                self.age=e.age
                self.name=e.name
                return
    def deleteCustomer(self):
        for e in Customer.listcus:
            if(e.id==self.id):
                Customer.listcus.pop(e)
                return
    @staticmethod
    def deleteCust(id):
        for e in Customer.listcus:
            if(e.id==id):
                Customer.listcus.remove(e)
                return
    def modifyCustomer(self):
        for e in Customer.listcus:
            if (e.id == self.id):
                e.name=self.name
                e.age=self.age


#PL
def showCust(ob):
    print("Customer ID:",ob.id,"Customer Age:",ob.age,"Customer Name:",ob.name)
while(1):

    ch=input("Enter Choice 1 to add Customer \n 2 to search Customer \n 3 to Delete Customer \n 4 to modify Customer \n 5 to display all \n 6 to Exit: ")
    if(ch=="1"): #Add Customer
        cus=Customer()
        cus.id=input("Enter Customer ID:")
        cus.age=input("Enter Customer Age:")
        cus.name=input("Enter Customer Name:")
        cus.addCustomer()
        print("Customer Added Successfully")
    elif(ch=="2"): #Search Cust
        cus=Customer()
        cus.id=input("Enter Customer ID:")
        cus.searchCustomer()
        showCust(cus)
    elif(ch=="3"): # Delete Cust
        id=input("Enter Customer Id:")
        Customer.deleteCust(id)
        # cus=Customer()
        # cus.id=input("Enter Cust ID:")
        # cus.deleteCustomer()
        print("Cust Deleted Successfully")
    elif(ch=="4"): #Modify
        cus=Customer()
        cus.id=input("Enter Customer ID:")
        cus.age=input("Enter Customer Updated Age:")
        cus.name=input("Enter Customer Updated Name:")
        cus.modifyCustomer()
    elif(ch=="5"): #Display All
        for e in Customer.listcus:
            showCust(e)
    elif(ch=="6"):#Exit
        break






