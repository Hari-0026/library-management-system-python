print("*======= LIBRARY MANAGEMENT SYSTEM =======*\n")
print("_____Welcome to library ______\n")
options=["1)view books","2)Return books","3)Borrow books","4)Exit","___________________________________________"]
books=["* PYTHON","* C++","* JAVA","* C PROGRAMMING"]
for i in options:
    print(i,end="\n")
op=int(input("Enter your optinos here :"))
if(op==1):
    for k in books:
        print(k,end="\n")
elif(op==2):
    print("======Select book to return======")
    list_book=["1)PYTHON","2)C++","3)JAVA","4)C PROGRAMMING"]
    for m in list_book:
        print(m,end="\n")
    book_op=int(input("Enter a book number to return:"))    
    if(book_op in range(1,5)):
      print("the book was returned successfully")
    else:
        print("Invalid book number")
elif(op==3):
   print("======Select book Borrow======")
   list_book=["1)PYTHON","2)C++","3)JAVA","4)C PROGRAMMING"]
   for m in list_book:
        print(m,end="\n")
   book_br=int(input("Enter a book number to borrow:"))    
   if(book_br in range(1,5)):
           print("the book was borrowed successfully")
           print("=======================")
           print("Your payment amount=5$")
           print("THANK YOU FOR PURCHASE")
           print("=======================")

   else:
           print("Invalid book number")
    
elif(op==4):
    print("========================")
    print("THANK YOU FOR VISITING!")
    print("========================")
    
    
        
    

    
        
