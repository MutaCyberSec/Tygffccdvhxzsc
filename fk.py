from faker import Faker

# Create a Faker instance
fake = Faker('en_US')


# Generate a random USA first name

def sec():
        trS = set()
        for x in range(500):
                usa_first_name = fake.last_name()
                trS.add(usa_first_name)
        trx = list(trS)
        with open('secondtUs.txt', 'w') as file:
                dem = ",".join(trx)
                file.write(dem)

def fir():
        trS = set()
        for x in range(500):
                usa_first_name = fake.first_name()
                trS.add(usa_first_name)
        trx = list(trS)
        with open('firstUs.txt', 'w') as file:
                dem = ",".join(trx)
                file.write(dem)
#print("Random USA First Name:", usa_first_name)

sec()

fir()
