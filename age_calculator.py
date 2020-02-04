import datetime

def check_birthdate(year, month, day):
	today_date = datetime.date.today()
	birthday_date = datetime.date(year, month, day)
	if (today_date - birthday_date).days < 0:
		return False
	else: return True


def calculate_age(year, month, day):
	today_date = datetime.date.today()
	birthday_date = datetime.date(year, month, day)
	age = (today_date - birthday_date).days // 365
	print('You are '+str(age)+' years old.')


def main():
	year = int(input('Enter year of birth: '))
	month = int(input('Enter month of birth: '))
	day = int(input('Enter day of birth: '))
	if check_birthdate(year, month, day):
		calculate_age(year, month, day)
	else:
		print('Birthdate is invalid.')


if __name__ == '__main__':
	main()

