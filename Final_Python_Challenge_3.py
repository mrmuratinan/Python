birthYear = input("Enter your birth YEAR (YYYY): ")
birthMonth = input("Enter your birth MONTH (MM): ")
birthDay = input("Enter your birth DAY (DD): ")

todayYear = input("Enter TODAYS' YEAR (YYYY): ")
todayMonth = input("Enter TODAYS' MONTH (MM): ")
todayDay = input("Enter TODAYS' DAY (DD): ")

tYear=int(todayYear)-int(birthYear)     # calculating number of years
tMonth=int(todayMonth)-int(birthMonth)  # calculating number of months
tDay=int(todayDay)-int(birthDay)   # calculating number of days
# converting calculated years months and days to days
totalDays=int(tYear*365+tMonth*30.42+tDay) 
print("You are alive approximately " + str(totalDays) +" days.")
# calculating the alive days as month and days
totalMonths=totalDays/30.42
remDays=int((totalMonths-int(totalMonths))*30.42)
print("OR approximately "+str(int(totalMonths))+" months and "+ str(remDays)+" days.")
