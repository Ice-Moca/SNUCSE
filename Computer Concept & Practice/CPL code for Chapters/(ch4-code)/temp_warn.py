# input은  '20.3F'  '-10C'   '32.5C'  같은 방식의 string으로 입력
# output은 
#     물의 끓는 점 (100도) 이상일 경우 메시지:    Watch Out!
#     물이 어는 점 (0도) 이하일 경우 메시지:    Don’t get frozen!
#     섭씨 50도에서 100도 사이일 경우 메시지:  You better be careful!
#     섭씨 0도에서 50도 이하일 경우 메시지:  You will be OK!

def FtoC(F):
    C = (F-32)*5/9
    return C

def TempOK(C):
    if 100 <= C:              print ("Watch Out!")
    if  C <= 0:               print ("Don't get frozen!")
    if  50< C < 100:  	    print ("You better be careful")
    if  0<  C <= 50:  	    print ("You will be OK")

def WeatherMessage():
    temp = input("Type your temperature with 'C' or 'F': ")
    if   temp[-1] == "C":
            Centi = float(temp[:-1])
            TempOK(Centi)
    elif  temp[-1] == "F":
            Fahren = float(temp[:-1])
            TempOK( FtoC(Fahren) )
    else:   
            print("Pardon?")
            