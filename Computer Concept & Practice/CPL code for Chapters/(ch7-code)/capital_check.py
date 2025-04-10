stateMap = { 'pittsburgh': 'PA', 'chicago':'IL', 'seattle':'WA', 'boston':'MA' }
city = input( "Enter a city name --> " ).lower( )
if (city in stateMap):
    print( city.title( ), "is in", stateMap[city] )
else:
    print( "Sorry, never heard of it " )
