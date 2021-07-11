class Dog:

    def __init__(self):
        self.name = input('What is the name of your dog? ')
        self.age = int(input('How old is your dog? '))
    
    def sit(self):
        print(f'{self.name}, sit, please.')

    def roll_over(self):
        print(f'{self.name}, roll_over!')


my_dog = Dog()
your_dog = Dog()
my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()

# print(f"My dog's name is {my_dog.name} and his age is {my_dog.age}")
