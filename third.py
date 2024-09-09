from datetime import datetime

def main():
    name=str(input("enter your name:"))
    print("Hello",name)

    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

    try:
        dob = datetime.strptime(dob_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    today = datetime.today()

    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    print(f"Your age is: {age}")

if __name__ == "__main__":
    main()


