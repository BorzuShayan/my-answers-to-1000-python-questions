salary = float(input(">> Enter your salary: "))

insurance = int(salary * 0.07)
tax = int(salary * 0.1)
rsalary = int(salary - (insurance + tax))

print(f">> Insurance: {insurance} \n>> Tax: {tax}\n>> Salary after tax and insurance: {rsalary}")