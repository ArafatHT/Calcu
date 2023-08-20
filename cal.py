logo = ("""

\033[1;91m────────────────────────────────────────────────────────────
\033[1;91m ███████████████████    \033[1;92m████████  ████████    \033[1;91m██████████████
\033[1;91m ██░░░░░░░░░░░░░░░██    \033[1;92m██░░░░██  ██░░░░██    \033[1;91m██░░░░░░░░░░██
\033[1;91m ██░░███████████████    \033[1;92m████░░██  ██░░████    \033[1;91m██░░██████████
\033[1;91m ██░░██                   \033[1;92m██░░░░██░░░░██      \033[1;91m██░░██
\033[1;91m ██░░██████████           \033[1;92m████░░░░░░████      \033[1;91m██░░██        
\033[1;91m ██░░░░░░░░░░██             \033[1;92m██░░░░░░██        \033[1;91m██░░██  ██████
\033[1;91m ██░░██████████           \033[1;92m████░░░░░░████      \033[1;91m██░░██  ██░░██
\033[1;91m ██░░██                   \033[1;92m██░░░░██░░░░██      \033[1;91m██░░██  ██░░██
\033[1;91m ██░░██                 \033[1;92m████░░██  ██░░████    \033[1;91m██░░██████░░██
\033[1;91m ██░░██                 \033[1;92m██░░░░██  ██░░░░██    \033[1;91m██░░░░░░░░░░██
\033[1;91m ██████                 \033[1;92m████████  ████████    \033[1;91m██████████████
\033[1;92m────────────────────────────────────────────────────────────""")


print(logo)


print("\033[0;34mHello Dear,\nMy Name Is \"_____________\"\nWhat's Yours name?" )
print()
name = input("\033[0;34mEnter Your Name: ")
age = input("Enter your Age: ")
gpa = input("Enter Your GPA: ")


print("\033[1;32mI Collected Your Information")
print("..................................")
print("Name : "+name)
print("Age : "+age)
print("GPA : "+gpa)
print("..................................")



def display_menu():
    green = '\033[92m'
    reset = '\033[0m'

    print(f"{green}[1]{green} + {green} Addition")
    print(f"{green}[2]{green} - {green} Subtraction")
    print(f"{green}[3]{green} * {green} Multiplication")
    print(f"{green}[4]{green} / {green} Division")


while True:
    display_menu()

    choice = input("Enter an Option: ")

    if choice == '1':
        name = "+"
    elif choice == '2':
        name = "-"
    elif choice == '3':
        name = "*"
    elif choice == '4':
        name = "/"


    if name == "+":
        print("\033[0;34mLet's Solve Your Problem")
        num1 = int(input("\033[0;34mEnter Your First Number : "))
        num2 = int(input("\033[0;34mEnter Your Second Number : "))
        sum = num1 + num2
        print("\033[0;32mThe Result is : " f"{num1} + {num2} = {num1 + num2}")

    elif name == "-":
        print("\033[0;34mLet's Solve Your Problem")
        num1 = int(input("\033[0;34mEnter Your First Number : "))
        num2 = int(input("\033[0;34mEnter Your Second Number : "))
        sum = num1 - num2
        print("\033[0;32mThe Result is : " f"{num1} - {num2} = {num1 - num2}")
    elif name == "*":
        print("\033[0;34mLet's Solve Your Problem")
        num1 = int(input("\033[0;34mEnter Your First Number : "))
        num2 = int(input("\033[0;34mEnter Your Second Number : "))
        sum = num1 * num2
        print("\033[0;32mThe Result is : " f"{num1} * {num2} = {num1 * num2}")
    elif name == "/":
        print("\033[0;34mLet's Solve Your Problem")
        num1 = int(input("\033[0;34mEnter Your First Number : "))
        num2 = int(input("\033[0;34mEnter Your Second Number : "))
        sum = num1 / num2
        print("\033[0;32mThe Result is : " f"{num1} / {num2} = {num1 / num2}")
