def calculate_bonus (base_salary ,performance_rating):
    if performance_rating == 5 :
        bonus_percentage = 0.20
        return base_salary * bonus_percentage
    elif performance_rating >=3 :
        bonus_percentage = 0.10
        return base_salary * bonus_percentage
    else:
        bonus_percentage = 0.0
        return  base_salary * bonus_percentage


def calculate_tax(gross_salary):
    if gross_salary > 7000:
        tax_percentage = 0.15
    elif gross_salary >= 3000:
        tax_percentage = 0.10
    else:
        tax_percentage = 0.0

    return gross_salary * tax_percentage
    

    
def main_hr_app ():
    print("-" *60)
    print ("Welcome To Our Corporate Payroll System ".center(50 ,"-"))
    print("-" *60)

    emp_name=input(" Enter Employee Name: ")
    dept=input(" Enter Your Department : ")
    base_salary = float(input(" Enter Base Salary (EGP): "))
    rating = int(input(" Enter Performance Rating (1-5): "))

    if base_salary < 0 or rating < 1 or rating > 5:
        print("Invalid Information")
        return

    bonus = calculate_bonus(base_salary, rating)
    gross_salary = base_salary + bonus
    tax = calculate_tax(gross_salary)
    net_salary = gross_salary - tax


    print("\n" + "=" * 50)
    print("PAYROLL STATEMENT".center(50))
    print("=" * 50)
    print(f"Employee Name : {emp_name}")
    print(f"Department    : {dept}")
    print("-" * 50)
    print(f"Base Salary   : {base_salary:.2f} EGP")
    print(f"Bonus         : {bonus:.2f} EGP")
    print(f"Gross Salary  : {gross_salary:.2f} EGP")
    print(f"Tax           : {tax:.2f} EGP")
    print("-" * 50)
    print(f"Net Salary    : {net_salary:.2f} EGP")
    print("=" * 50)

main_hr_app()