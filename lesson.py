class Human:
	def __init__(self, name, surname, age, town):
		self.name = name
		self.surname = surname
		self.age = age
		self.town = town
	def display(self):
		print(f'Имя - {self._name}\nфамилия - {self._surname}\nвозраст - {self._age}\nгород - {self._town}')
class Student(Human):
	def __init__(self, name, surname, age, town, NumClass, rating):
		self.NumClass = NumClass
		self.rating = rating

		Human.__init__(self, name, surname, age, town)
	def display(self):
		Human.display(self)
		print(f'Номер класса - {self.NumClass}\nОценки - {self.rating}\n')
	def math(self, FirstNumber, SecondNumber, mark):
		try:
			if mark == '+':
				a = FirstNumber+SecondNumber
			if mark == '-':
				a = FirstNumber-SecondNumber
			if mark == '*':
				a = FirstNumber*SecondNumber
			if mark == '/':
				a = FirstNumber/SecondNumber
		except ZeroDivisionError:
			print('На ноль делить нельзя')
			while SecondNumber == 0:
				SecondNumber = int(input('Напиши 2 число заново '))
			if mark == '+':
				a = FirstNumber+SecondNumber
			if mark == '-':
				a = FirstNumber-SecondNumber
			if mark == '*':
				a = FirstNumber*SecondNumber
			if mark == '/':
				a = FirstNumber/SecondNumber
		finally:
			print(a)
FirstNumber = int(input('Первое число '))
SecondNumber = int(input('Второе число '))
Mark = input('Знак ')
Man1 = Student('Алексей', 'Чебыкин', '17', 'Москва', '10', {'Алгебра':4, 'Русский язык':5, 'Литература':4, 'Биология':3})
Man1.math(FirstNumber, SecondNumber, Mark)