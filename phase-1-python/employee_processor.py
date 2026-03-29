with open("employees.txt", "w") as file:
    file.write("Ankit,30000,Delhi\n")
    file.write("Priya,55000,Mumbai\n")
    file.write("Rahul,22000,Patna\n")
    file.write("Sneha,70000,Bangalore\n")
    file.write("VK,45000,Patna\n")

def get_level(salary):
    if salary > 50000:
        return "Senior"
    elif salary > 25000:
        return "Mid level"
    else:
        return "Junior"

with open("employees.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        name = parts[0]
        salary = int(parts[1])
        city = parts[2]
        print(f"{name:<10} | City: {city:<10} | Salary: {salary:<8} | Bonus: {salary*0.1:<8.1f} | Level: {get_level(salary):<10}")
