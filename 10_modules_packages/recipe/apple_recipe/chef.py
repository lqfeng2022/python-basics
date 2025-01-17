# 7)Reference an intro-package (customer)
from ..customer import contact

contact.contact_customer()


def create_recipe():
    print("Create recipes")


def improve_recipe():
    print("Improve recipes")


# 9)Execute chef.py as a script
if __name__ == "__main__":
    print("Chef initialized")
    create_recipe()
