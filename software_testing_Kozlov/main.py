import os
import click


@click.command()
def all():
    os.system("behave features\SignUp.feature")
    os.system("behave features\LogIn.feature")
    os.system("behave features\Cars_search.feature")
    os.system("behave features\Subscribe.feature")
    os.system("behave features\ContactUs.feature")


@click.command()
def signup():
    os.system("behave features\SignUp.feature")


@click.command()
def login():
    os.system("behave features\LogIn.feature")


@click.command()
def cars():
    os.system("behave features\Cars_search.feature")


@click.command()
def subscribe():
    os.system("behave features\Subscribe.feature")


@click.command()
def contactus():
    os.system("behave features\ContactUs.feature")


@click.group()
def main():
    pass


main.add_command(all)
main.add_command(signup)
main.add_command(login)
main.add_command(cars)
main.add_command(subscribe)
main.add_command(contactus)

if __name__ == "__main__":
    main()
