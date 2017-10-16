import sys

import pickle

print"Welcome to The Great Nautanki Theatre \n "

print "Get ready to witness first of its kind,long running Bollywood Musical.....just book the tickets now...!!! \n "

print "The timings are 7:00 pm to 9:00 pm \n "


def funcc(D):
    
    Data=open("theatre1.dat","rb")
    dictionary={}
    dictionary=pickle.load(Data)
    Seats=dictionary[D]

    while True: #loops back to here and asks question again on line below

        try:
            EntryPeople = int(input("How many people do you wish to book for? MAXIMUM 10 at a time ! \n "))

        except ValueError:
            print("You have to type an Integer \n ")

        else:

            while EntryPeople >10: #Loops back to this point if they enter more than 10

                print("Please Enter a Number below ten!") 
                EntryPeople = int(input("Many people do you wish to book for? MAXIMUM 10 at a time! \n "))

            else:

                EntryRow = raw_input("Which row would you like to book for? \n ")
                Upper = EntryRow.upper()

                if Upper in ['A','B']:
                    print "You will have to pay Rs.",t.prAB*EntryPeople

                elif Upper in ['C','D']:
                    print "You will have to pay Rs.",t.prCD*EntryPeople

                elif Upper in ['E']:
                    print "You will have to pay Rs.",t.prE*EntryPeople 


                while not Upper in ('A','B','C','D','E'):

                    print("That is not a row")
                    EntryRow = input("Which row would you like to book for? ")
                    print '\n'
                    Upper = EntryRow.upper()

                    if Upper in ['A','B']:
                       print "You will have to pay Rs.",t.prAB*EntryPeople

                    elif Upper in ['C','D']:
                        print "you will have to pay Rs.",t.prCD*EntryPeople

                    elif Upper in ['E']:
                        print "you will have to pay Rs.",t.prE*EntryPeople 

                else:
                    Index = ord(EntryRow.upper()) -65

                    if int(Seats[Index])- int(EntryPeople) > -1:
                        Seats[Index]= int(Seats[Index]) - EntryPeople
                        print "for booking "+str(EntryPeople)+" seats in row:"+EntryRow+" on"+D
                        print "\n"
                        ##### Prog For setting the SEAT ID######
                        no=30-int(Seats[Index])
                        a=no-EntryPeople
                        print "Your seat Id is/are: \n "
                        for i in range(a,no):
                            print "S-",i,"R-",EntryRow.upper(),"16"

                        print "\n"
                        print "Thank You for booking in The Great Nautanki Theatre"
                    
                        Data = open('theatre1.dat', 'wb') # Saving the changes made, in the file
                        pickle.dump(dictionary,Data)
                        
                        Data.close()
                        return                                             # Returning to the value of the func
                    
#This segment above forces the input to uppercase because all uppercase have a value. A = 65 if you subtract 65 form 65 you get 0. 0 is the corresponding number to A in the list.
#Therefore B=1; it works for any value entered.

                    else:
                        
                        print "\n"
                        print"I'm Sorry but those seats are currently UNAVAILABLE"
                        print "\n"

                        print "Available seats on row A for: "+D+" are"
                        print (Seats[0])
                        print "\n"

                        print "Available seats on row B for: "+D+"are" 
                        print (Seats[1])
                        print "\n"

                        print"Available seats on row c for: "+D+" are"
                        print(Seats[2])
                        print "\n"

                        print"Available seats on row D for: "+D+" are"
                        print (Seats[3])
                        print "\n"

                        print"Available seats on row E for:"+D+" are"
                        print(Seats[4])#prints free seats

#the below prog is to ask uer wether he wants to book on same day or some other day
                        print "\n"
                        a=raw_input("do u want to book any other seat for same date say YES/NO \n or you want to change date say 'CHANGE DATE'")

                        if a.upper()=="YES":
                               print "the seat available for "+D+" are",dictionary[D]

                               EntryRow = raw_input("Which row would you like to book for?")
                               Index1=ord(EntryRow.upper()) -65
                               Seats[Index1]= int(Seats[Index1]) - EntryPeople

                               print "you have booked "+str(EntryPeople)+" seats in row:"+EntryRow

                               no=30-int(Seats[Index])
                               a=no-EntryPeople 
                               for i in range(a,no):
                                       print "your seat Id is/are: \n ","S-",i,"R-",EntryRow.upper(),"16"

                               print "Thank You for booking in The Great Nautanki Theatre"

                               Data = open('theatre1.dat', 'wb')
                               pickle.dump(dictionary,Data)
                               Data.close()
                               return

                        elif a.upper()=='NO':
                            print "Thank You"
                            Data.close()
                            sys.exit()

                        else:
                            print "the dates are:  ",dictionary.keys()
                            print "\n"
                            cdate=raw_input("enter another date \n ")
                            print "the available seats for this day are:   ",dictionary[cdate]
                            a=funcc(cdate) # again calling the func with changed date.....Applying Nested Function
                            
                            sys.exit()       

######################################################################################


class Theatre: # creating a class for the programmer to set the values for a particular show

    from datetime import date

    def __init__setvalues(self):

        self.prAB=0
        self.prCD=0
        selfprE=0
        self.date1=date(2016,0,0)
        self.date2=date(2016,0,0)
        self.date3=date(2016,0,0)
        self.date4=date(2016,0,0)


    def inputprice(self):
        
        self.prAB=input("enter the price you want to set for rows A & B for this show: \n ")
        self.prCD=input("enter the price you want to set for rows C & D for this show: \n ")
        self.prE=input("enter the price you want to set for row E for this show:\n ")


    def showprice(self):
        
        print "The fare for rows A,B are   Rs.",self.prAB
      
        print "The fares for rows C,D are  Rs.",self.prCD
        
        print "The fares for row E are   Rs.", self.prE
        print '\n'
   
        
    def inputdates(self):

        a=input("Enter the year of show as 20XX \n ")
        b=input ("Enter the month of show:{eg. 1 for January} \n ")
        d1=input("Enter the first date of show:  ")
        d2=input("enter the second day of show:  ")
        d3=input("Enter the third date of show:  ")
        d4=input("Enter the fourth date of show:  ")

        from datetime import date

        self.date1=date(a,b,d1)
        self.date2=date(a,b,d2)
        self.date3=date(a,b,d3)
        self.date4=date(a,b,d4)


    def showdate(self):
        
        print "The show is on:\n ",self.date1.strftime('%d,%b %y'),'\n',self.date2.strftime('%d,%b %y'), '\n' ,self.date3.strftime('%d,%b %y'), '\n', self.date4.strftime('%d,%b %y'),'\n'

    
"""from datetime import date

t=Theatre() # creating the object of the class

t.inputprice()

t.inputdates()


import pickle

fw=open("theatresettings.dat",'wb')#dumping the class object in file for further use
pickle.dump(t,fw)
print "\n"
print "The object is saved in the file name theatresettings.dat \n "
fw.close()

t.showdate()

t.showprice()

d={}#creating an empty dictionary for initialising the values for the show

key=t.date1.strftime('%d')
d[key]=[30,30,30,30,30]

key=t.date2.strftime('%d')
d[key]=[30,30,30,30,30]

key=t.date3.strftime('%d')
d[key]=[30,30,30,30,30]

key=t.date4.strftime('%d')
d[key]=[30,30,30,30,30]

#above the dates on which show is to be held are made the keys of the dictionary so as to access the dict datewise


fw=open("theatre.dat","wb")
pickle.dump(d,fw)
fw.close()

f=open("theatre.dat","rb")
d1={}
d1=pickle.load(f)

fr=open("theatre1.dat",'wb')
pickle.dump(d1,fr)
f.close()
fr.close()"""


choice=raw_input("Do you want to book a ticket?,say Y\N ")
choice=choice.upper()

if choice=='N':
    sys.exit()                                                                                    #exits the program

elif choice=='Y':
    t=Theatre()                                                                                #an empty class object for loading the contnts of file
    from datetime import date
    fille=open("theatresettings.dat",'rb')

    try:
        while True:
            t=pickle.load(fille)
            t.showdate()
            t.showprice()

    except EOFError:                                                                    # checking the End Of Line error
        fille.close()



    fe=open("theatre1.dat","rb")
    d1={}
    d1=pickle.load(fe)
  

    for i in d1:
        print "the seat available for",i,"is",d1[i]

    l=[]
    l=d1.keys()                                                                                # creating a list of all the keys i.e dates of show

    print "\n"
    print "enter",t.date1.strftime('%d'),"for ",t.date1.strftime('%d,%b %y')         # strftime is an inbuit func of datetime.date module
    print "enter",t.date2.strftime('%d'),"for ",t.date2.strftime('%d,%b %y')        # %d gives the date
    print "enter",t.date3.strftime('%d'),"for ",t.date3.strftime('%d,%b %y')        #%b gives month name,
    print "enter",t.date4.strftime('%d'),"for ",t.date4.strftime('%d,%b %y')        #%y gives last two digits of the year
    print "\n"
    fe.close()
    

    Date=raw_input("enter your choice ")
    print '\n'

    Seats = []
    
    
            
    a=funcc(Date)                                                                  #calling the function with argument and is of retrn type
        
        
            
        
        


#####################################################

             
                                        
                                    
                        
                        

