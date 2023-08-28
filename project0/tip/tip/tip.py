def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d_no_dollar_sign = d.replace("$", "")
    return float(d_no_dollar_sign)

def percent_to_float(p):
    p_no_percent = p.replace("%", "")
    p_converted = float(p_no_percent) / 100

    return p_converted

if __name__ == "__main__":
    main()