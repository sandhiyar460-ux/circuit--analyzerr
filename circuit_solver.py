# Circuit Analysis Solver for ECE Students
# Calculates series, parallel circuits and Thevenin/Norton equivalents

def series_resistance(resistors):
    return sum(resistors)

def parallel_resistance(resistors):
    reciprocal = sum(1/r for r in resistors)
    return 1 / reciprocal

def thevenin_voltage(v_source, r1, r2):
    """Simple voltage divider: Vth = V * R2 / (R1 + R2)"""
    return v_source * r2 / (r1 + r2)

def thevenin_resistance(r1, r2):
    """Rth = R1 parallel R2"""
    return parallel_resistance([r1, r2])

def norton_current(vth, rth):
    """In = Vth / Rth"""
    return vth / rth

def main():
    while True:
        print("\n=== CIRCUIT ANALYSIS SOLVER ===")
        print("1. Series Circuit")
        print("2. Parallel Circuit")
        print("3. Thevenin & Norton Equivalent")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of resistors: "))
            resistors = [float(input(f"Enter resistor {i+1} value (ohms): ")) for i in range(n)]
            r_total = series_resistance(resistors)
            print(f"Total series resistance: {r_total:.2f} Ω")

        elif choice == 2:
            n = int(input("Enter number of resistors: "))
            resistors = [float(input(f"Enter resistor {i+1} value (ohms): ")) for i in range(n)]
            r_total = parallel_resistance(resistors)
            print(f"Total parallel resistance: {r_total:.2f} Ω")

        elif choice == 3:
            v_source = float(input("Enter voltage source V (volts): "))
            r1 = float(input("Enter series resistor R1 (ohms): "))
            r2 = float(input("Enter load resistor R2 (ohms): "))

            vth = thevenin_voltage(v_source, r1, r2)
            rth = thevenin_resistance(r1, r2)
            inorton = norton_current(vth, rth)

            print(f"\nThevenin Voltage Vth: {vth:.2f} V")
            print(f"Thevenin Resistance Rth: {rth:.2f} Ω")
            print(f"Norton Current In: {inorton:.2f} A")

        elif choice == 4:
            print("Exiting Circuit Solver.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
