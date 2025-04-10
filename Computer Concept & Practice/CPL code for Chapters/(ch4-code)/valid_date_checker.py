def month_LastDate(year, month):            
    # Year와 Month가 주어지면 그 달의 마지막 날짜를 return
    if month in [1, 3, 5, 7 ,8, 10, 12]:
          return 31
    elif month == 2:
        if yeap_year_checker(year):   return 29
        else:                         return 28
    else:
        return 30
        
def valid_date_checker( ):
    Target_Date = input("Type your date in yyyy/mm/dd string format:")

    year, month, date = Target_Date.split("/")
    year, month, date = int(year), int(month), int(date)
    print ("Your typed date is:", "Year", year, "Month", month, "Day", date)

    if (year != 0) and (1 <= month <= 12) and  \
       (1 <= date <= month_LastDate(year, month)) :
              return   "Your typed date is valid!"
    else:    
              return   "Your typed date is invalid!"