name = input('Enter name\n')
surname = input('Enter surname\n')
year = input('Enter year\n')
city = input('Enter city\n')
email = input('Input email\n')
telephone = input('Input telepfone\n')


def my_func (name, surname, year, city, email, telephone):
     return ' '.join([
         "name: ", name,
         ". surname: ", surname,
         ". year: ", year,
         ". city: ", city,
         ". email: ", email,
         ". telephone: ", telephone, "."])
print(my_func(name, surname, year, city, email, telephone))