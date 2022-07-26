#Write a program to return a boolean value as a print statement if one number is greater than another.
#       E.g. If X is greater than Y return True otherwise return False

x, y = 5, 9

if x > y:
    print("true")
else:
    print("false")

#2) Modify the previous program to return a string value as a print statement like:
#	"10 is greater than 5" Or opposed "2 is less than 4"

x1, y1 = 1, 9

if x1 > y1:
    print(x1, " is greater than ", y1)
else:
    print(x1, "is less than", y1)

#    3) Modify the previous program to cover the case to compare only positive numbers, zero is not included!
#	in case one of the variables is zero return a string value as a print statement like:
#	"One or both numbers are not positive, can't proceed with the comparison!"

x2, y2 = 2, -2

if x2 > 0 and y2 > 0:
    if x2 > y2:
        print(x2, " is greater than ", y2)
    else:
        print(x2, "is less than", y2)
else:
    print("One or both numbers are not positive, can't proceed with the comparison!")
