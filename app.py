class Employee:
    raise_amount: float = 1.04

    def __init__(self, first_name, last_name, pay) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.pay: int = pay
        self.email: str = f"{first_name}.{last_name}@company.com"

    def get_fullname(self) -> str:
        return f"Employee: {self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay: float = int(self.pay * self.raise_amount)


employee_1: Employee = Employee("John", "Doe", 45000)
employee_2: Employee = Employee("Andrew", "Price", 69000)

# Preview namespaces
print(f"\nClass namespace: {Employee.__dict__}")
print(f"Object namespace: {employee_1.__dict__}")
print(f"Object namespace: {employee_2 .__dict__}\n")


def test() -> None:
    print(f"Employee email: {employee_1.email}")
    print(Employee.get_fullname(employee_1))
    print(f"Previous salary:{employee_1.pay}")
    employee_1.apply_raise()
    print(f"Current salary:{employee_1.pay}\n")

    print(f"Employee email: {employee_2.email}")
    print(Employee.get_fullname(employee_2))
    print(f"Previous salary:{employee_2.pay}")
    employee_2.apply_raise()
    print(f"Current salary:{employee_2.pay}\n")


if __name__ == '__main__':
    test()
