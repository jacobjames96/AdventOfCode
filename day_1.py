# Day 1: Calculate fuel required to launch a rocket which is based on the mass of its modules
# Fuel also requires fuel to launch, so we keep calculating additional fuel fuel cost

def calc_fuel(mass):
    """
    Take a mass of a module, calculate the fuel required for that module
    Formula is mass divided by three, rounded down, minus two.
    """
    fuel = (mass // 3) - 2
    return fuel


def main():
    # Open the input data and extract it into a list of modules
    with open('Data/day1.txt', 'r') as f:
        data = f.read().splitlines()

    module_fuel = 0
    # Loop through the modules and calculate fuel for each one
    for module in data:
        fuel = calc_fuel(int(module))
        # Calculate whether the fuel required for a module also needs fuel itself, recursively until additional
        # fuel requirements are negative
        additional_fuel = calc_fuel(fuel)
        while additional_fuel > 0:
            fuel += additional_fuel
            print(additional_fuel, fuel)
            additional_fuel = calc_fuel(additional_fuel)
        module_fuel += fuel

    print(module_fuel)


if __name__ == '__main__':
    main()