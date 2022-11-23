name_verification = input('Please type your full name ')
age_verification = float(input('Please enter your age, thx hun '))
if age_verification >= 21:
    print ('Congrats M8, welcome to the club')
elif age_verification < 21 and age_verification >= 18:
    print ("Apologies, Under 21's are not allowed to enter the club")
else:
    print ('Sorry you young mfer, go back to school')