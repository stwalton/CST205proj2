print("Welcome to money well saved!")
print( " " )
print("Let's get started. ")
print("would you like to save for an item, or save up an amount?")
print(" ")

ITS = raw_input('Please enter either item or amount:   ')
print " "
print "you chose: ",ITS

if ITS in ['item', 'ITEM', 'item']:
    answer1 = raw_input(("Is this correct? Enter Y for yes or N for no     "))
    
    if answer1 in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print("Awesome, Now lets see")
    
    print(" ")
    
    amountSave = raw_input(("How much do you need to save?  "))
    
    print(" ")
    print ("So, you need to save " + amountSave + " dollars")
    print (" ")
    
    answer3 = raw_input(("Is this correct? Enter Y for yes or N for no     "))
    
    if answer3 in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print("okay...")

    print (" ")
    
    days = input(("How many days would you like to take to save up your funds? "))
    print(" ")

    print "Your input was" 
    
    print days 
    print ("Days")
    answer5 = raw_input(("Is this correct? Enter Y for yes or N for no     "))
    
    if answer5 in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print("alrighty, awesome")
        
    print (" ")
    amountSave2 = int(amountSave)
    perDay = float(amountSave2)/float(days)
    print ( "So you want to save up " + amountSave + " in " + str(days)+ " days--wtf is this: " + str(amountSave2))
    
    print (" ")
    days2 = str(days) 
   
    print ("In order to have the funds in " + days2 + " days " + " It will take $" + str(perDay) + " per day.")
    
    
    
    print (" ")
    print "Happy Saving!"
    
    
    
    
    
    
    
elif ITS in ['amount', 'AMOUNT', 'Amount']:
    answer1 = raw_input(("Is this correct? Enter Y for yes or N for no     "))
    
    if answer1 in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print("Awesome, Now lets see")
    
    print(" ")
    
    amountSave = raw_input(("How much do you need to save?  "))
    
    print(" ")
    print ("So, you need to save " + amountSave + " dollars")
    print (" ")
    
    answer3 = raw_input(("Is this correct? Enter Y for yes or N for no     "))
    
    if answer3 in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print("okay...")

    print (" ")
    
    days = input(("How many days would you like to take to save up your funds? "))
    print(" ")

    print "Your input was" 
    
    print days 
    print ("Days")
    answer5 = raw_input(("Is this correct? Enter Y for yes or N for no     "))
    
    if answer5 in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print("alrighty, awesome")
        
    print (" ")
    amountSave2 = int(amountSave)
    perDay = amountSave2/days
    print ( "So you want to save up " + amountSave + " in " + str(days)+ " days")
    
    print (" ")
    days2 = str(days) 
   
    print ("In order to have the funds in " + days2 + " days " + " It will take $" + str(perDay) + " per day.")
    
    
    
    print (" ")
    print "Happy Saving!"
    
    

