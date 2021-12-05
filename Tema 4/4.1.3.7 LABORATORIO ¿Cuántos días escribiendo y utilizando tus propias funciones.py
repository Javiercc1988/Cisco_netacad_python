def isYearLeap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def daysInMonth(year, month):
    d28 = [2]
    d30 = [4,6,9,11]
    d31 = [1,3,5,7,8,10,12]
    if month in d30:
        return 30
    elif month in d31:
        return 31
    elif isYearLeap(year) == True:
        return 29
    else:
        return 28
        
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")