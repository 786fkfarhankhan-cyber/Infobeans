
ch = input("enter a character= ")
match ch:
    case "A" : 
        print("A")
        for i in range(1,9):
            for j in range(1,19):
                if (i+j==11) or (j-i==9) or (j>5 and i==5 )and (j<15 and i==5) :
                    print("*",end="")
                else:
                    print(" ",end="") 
            print() 

    case "B" :
        print("B")
        for i in range(1,12):
            for j in range(1,8):
                if (i==1 and j<6 )or (i==11 and j<6 )or j==1 or (j==7 and (i>2 and i<10) and i != 6 ) or (i==6 and j<6 ) or (j==6 and (i==2 or i==6 or i==10)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print() 

    case "C" :
        print("C")
        for i in range(1,11):
            for j in range(1,9):
                if (j==1 and (i<9 and i>2)) or (i==1 and (j<9 and j>2))  or (i== 10 and j>2) or (i==2 and j==2) or (i==9 and j==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()  

    case "D" :
        print("D")
        for i in range(1,12):
            for j in range(1,8):
                if (i==1 and j<6) or (i==11 and j<6) or j==1 or (j==7 and (i>2 and i<10)) or (j==6 and (i==2 or i==10)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")  
            print()    

    case "E" :
        print("E")
        for i in range(1,11):
            for j in range(1,6):
                if j==1 or  i ==1 or  i ==5 or i==10  :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    case "F" :
        print("F")
        for i in range(1,11):
            for j in range(1,6):
                if j == 1 or i==1 or i == 5:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    case "G" :
        print("G")
        for i in range(1,11):
            for j in range(1,9):
                if (j==1 and i>2 and i<9) or (i==1 and j>2) or (i==10 and j>2 and j<7) or (j==8 and i>6 and i<9) or (i==6 and j>3 and j<7) or (i==2 and j==2 ) or (j==7 and (i==9 or i==6 )) or (i==9 and j==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()      

    case "H" :
        print("H")
        for i in range(1,8):
            for j in range(1,6):
                if j==1 or j==5 or i==4 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    case "I" :
        print("I")
        for i in range(1,10):
            for j in range(1,10):
                if(j==1) and (i<5) or (i==1) and (j>5) or (i==9) and j<5 or (i==9) and (j>5) or (i==5) or (j==5):
                    print("*",end=" ")
                else:
                    print(" ", end=" ")
    
            print()

    case "J" :
        print("J")
        for i in range(1,7):
            for j in range(1,6):
                if i==1 or j==3 or (i==6 and j<3) or  (i==5 and j<2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


    case "K" :
        print("K")
        for i in range(1,10):
            for j in range(1,6):
                if j==1 or i+j==6 or i-j==4 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    case "L" :
        print("L")
        for i in range(1,11):
            for j in range(1,6):
                if j==1 or i==10 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


    case "M" :
        print("M")
        for i in range(1,7):
            for j in range(1,6):
                if j==1 or j==5 or (i<4 and i==j) or (i==2 and j==4) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


    case "N" :
        print("N") 
        for i in range(1,6):
            for j in range(1,6):
                if j==5 or j==1 or i == j:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    case "O" :
        print("O")
        for i in range(1,11):
            for j in range(1,11):
                if (i==1 and (j>4 and j<6) ) or (i==10 and (j>4 and j<7)) or (j==1 and (i>4 and i<7)) or (j==10 and (i>4 and i<7)) or (i==2 and (j==3 or j==8)) or (i==3 and (j==2 or j==9)) or (i==8 and (j==2 or j==9)) or (i==9 and (j==3 or j==8))  :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()      

    case "P" :
        print("P")
        for i in range(1,12):
            for j in range(1,7):
                if j==1 or (i==1 and j<5) or (j==6 and (i<5 and i>2)) or (i==6 and j<5 ) or (j==5 and (i==5 or i==2)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print() 


    case "Q" :
        print("Q")
        for i in range(1,11):
            for j in range(1,11):
                if (i==1 and (j>4 and j<7) ) or (i==10 and (j>3 and j<8)) or (j==1 and (i>3 and i<8)) or (j==10 and (i>4 and i<7)) or (i==2 and (j==3 or j==8)) or (i==3 and (j==2 or j==9)) or (i==8 and (j==2 or j==9)) or (i==9 and (j==3 or j==8)) or (i>7 and i==j) :
                    print("*",end="")
                else:
                    print(" ",end=" ")
            print()   


    case "R" :
        print("R")
        for i in range(1,12):
            for j in range(1,7):
                if j==1 or (i>6 and i-j==5) or (i==1 and j<5) or (j==6 and (i<5 and i>2)) or (i==6 and j<5 ) or (j==5 and (i==5 or i==2)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print() 


    case "S" :
        print("S")
        for i in range(1,8):
            for j in range(1,6):
                if i==1 or i == 7 or i ==4 or (j==1 and i<5) or ( j==5 and i>4) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


    case "T" :
        print("T")
        for i in range(1,8):
            for j in range(1,6):
                if i==1 or j == 3 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


    case "U" :
        print("U")
        for i in range(1,7):
            for j in range(1,6):
                if (j==1 or j==5 ) and i<5 or i+j==9:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print() 


    case "V" :
        print("V")
        for i in range(1,8):
            for j in range(1,15):
                if i==j or j+i==14:
                    print("*",end="")
                else:
                    print(" ",end="")
            print() 


    case "W" :
        print("W")
        for i in range(1,7):
            for j in range(1,6):
                if j==1 or j==5 or (i==5 and (j==2 or j==4)) or (i==4 and j==3) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


    case "X" :
        print("X")
        for i in range(1,6):
            for j in range(1,6):
                if i==j or i+j==6 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    case "Y" :
        print("Y")
        for i in range(1,6):
            for j in range(1,6):
                if (i<4 and i==j) or i+j==6 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    case "Z" :
        print("Z")
        for i in range(1,6):
            for j in range(1,6):
                if i==1   or i == 5 or i + j == 6:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    case _: print("Invalid choice...")
















