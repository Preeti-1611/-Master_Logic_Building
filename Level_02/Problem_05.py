h = int(input("enter hour(0-23)"))
if h<0 or h>23:
    print("invalid hour.enter 0-23")
elif 5<=h <=11:
    print("good morning")
elif 12<=h<=16:
    print("good afternoon")
elif 17<=h<=20:
    print("good evening")
else:
    print("good night")