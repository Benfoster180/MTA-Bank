import pickle
loop = 1


while loop == 1:
    task = int(input("1)Add New acount 2)View someones acount 3)Exit"))
    if task == 1:
        Person_name = input("Whats your full name")
        MTA=int(input("How many MTA do you have"))
        MOS=int(input("How many mos do you have"))
        
        File_name = Person_name+".txt" # sets up the file name
        
        f= open(File_name,"w+") #creats the file
        
        if MTA == 0 and MOS == 0: #This is for pepole who have no MTAs or Mos
            none = Person_name+" Has No MTA/Mos"
            f.write(none)
            f.close()
        
        elif MOS == 0 and MTA > 0: # This for people with MTA Only
            MTA_only = Person_name+" has "+str(MTA)+" MTA and no MOS"
            f.write(MTA_only)
            f.close
        
        elif MOS > 0 and MTA ==0: #for people who only have an mos
            MOS_only = Person_name+" has "+str(MOS)+" MOS and no MTAs"
            f.write(MOS_only)
            f.close
        
        elif MTA > 0 and MOS > 0: #For people 
            both = Person_name+" has "+str(MTA)+" MTAS and  "+str(MOS)+" MOS"
            f.write(both)
            f.close()

    if task == 2:
        faf = input("Who do you want to see plese type name") #faf = Find A Friend
        fanf = faf+".txt" #conrets name in to file format so the computer can find it
        f= open(fanf,("r")) # open the file found
        Info = f.read()
        print(Info) 
        hold=input("click enter to countine")

    if task == 3: #Ends the while loop cicule
        loop = loop + 20