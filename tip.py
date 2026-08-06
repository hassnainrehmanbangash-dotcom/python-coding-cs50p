def main():
    dollars = dollars_to_float(input("how much was the meal? "))
    percent = percent_to_float(input("what percentage would you like to tip? "))
    tip = dollars * percent
    print(f"leave ${tip:.2f}")


# replacing dollars to float numbers...
def dollars_to_float(d):
    # $30
    # 30.0
    d = d.replace("$", " ")
    return float(d)


# replacing percentage to float....
def percent_to_float(p):
    # 20%
    # 0.2
    p = p.replace("%", " ")
    p = float(p) / 100
    return float(p)


main()
