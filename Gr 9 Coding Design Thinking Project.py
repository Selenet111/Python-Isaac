principal = float(input("Enter the principal amount (number only): "))
rate = float(input("Enter the percent that the principal is compoundng by (number only): ")) / 100
time = float(input("Enter how many years you are investing or loaning for (number only): "))
periods = float(input("Enter the amount of times your money is compounded each year (number only): "))

total = round((principal * (1 + (rate / periods))**(periods * time)), 2)

print(f"\nYour final amount will be ${total}.\n")