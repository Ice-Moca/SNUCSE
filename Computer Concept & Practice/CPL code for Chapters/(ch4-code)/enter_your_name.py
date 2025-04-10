def enter_your_name():
    # get user’s first and last names
      first = input("Please enter your first name (all lowercase): ")
      last  = input("Please enter your last name (all lowercase): ")
      print() 
	  # concatenate first initial with the last name
      print( "Then your_name is : ", first[0] + "." + last )
