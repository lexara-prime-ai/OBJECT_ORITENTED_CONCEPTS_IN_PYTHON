# 1 kg -> 2.20462262 lbs

def read_user_input():
    weight: float = float(input("Please provide you weight e.g 69, 420 >"))
    unit: str = input("Please provide a unit of measurement e.g k -> kgs, l -> lbs >")

    if unit.lower() == "k" or unit.lower() == "kgs":
        print(f"Weight: {weight} kg")
        print(f"Weight in kgs: {weight * 2.2} lbs")
    elif unit.lower() == "l" or unit.lower() == "lbs":
        print(f"Weight: {weight} lbs")
        print(f"Weight in pounds: {weight // 2.2} kgs")
