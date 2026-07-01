brandname = {}
def brand_name ():
        brandname["city"] = input("Enter your favorite city: ")
        brandname["pet"] = input("Enter your pet name: ")
        brandName = (brandname["city"] + brandname["pet"])
        print(f"Here is your brand name {brandName}")
        
def dictionary ():
    print(brandname)        
        
def Brandname():
   while True:
     print("Generate your brand name")
     print("1. Generate brand name ")
     print("2. Print out dictionary")
     print("3. Exit")
     
     option = input ("enter the next action: ")
     if option == "1":
         brand_name ()
     elif option == "2":
          dictionary()
     elif option == "3":
          print("you have exited the page")
          break
     else:
          print("Enter the option given above")
        
Brandname ()