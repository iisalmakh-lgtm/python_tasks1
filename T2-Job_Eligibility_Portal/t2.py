#version1
print("#"*55)
print(" Welcome to our Job Eligibility Portal ".center(49,'#'))
print("#"*55)

python_skill=input("does the student know Python? (yes/no): ").strip().lower()

if python_skill=="no" :
    print("You are not eligible because Python knowledge is required.")
else:
    experience=int(input("How many years of experience or projects do you have? "))
    degree=input("does the student have a degree in Computer Science or a bootcamp certificate? (yes/no): ").strip().lower()
    if experience >= 2 or degree=="yes" :
        print("Congratulations! You have been accepted for the next interview stage.")
    else:
        print("Sorry, you are not eligible for the job now.")
#========================================================================
#version2


python_skill=input("does the student know Python? (yes/no): ").strip().lower()
experience=int(input("How many years of experience or projects do you have? "))
degree=input("does the student have a degree in Computer Science or a bootcamp certificate? (yes/no): ").strip().lower()

if python_skill=="no" :
    print("You are not eligible because Python knowledge is required.")
else:
    if experience >= 2 or degree=="yes" :
        print("Congratulations! You have been accepted for the next interview stage.")
    else:
        print("Sorry, you are not eligible for the job now.")
