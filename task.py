# Basic Data Processing Script for Average Temperature

def calculate_average(temperatures):
    """Calculate the average of a list of temperatures."""
    if len(temperatures) == 0:
        return None
    return sum(temperatures) / len(temperatures)


# --- Option 1: Read from a text file ---
# Each temperature should be on a new line in temperatures.txt
def read_temperatures_from_file(filename):
    temps = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    temps.append(float(line.strip()))
                except ValueError:
                    pass  # ignore lines that are not numbers
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return temps


# --- Option 2: Manual Input ---
def read_temperatures_from_input():
    temps = []
    n = int(input("How many temperature values? "))
    for i in range(n):
        value = float(input(f"Enter temperature {i+1}: "))
        temps.append(value)
    return temps


# --- Main Program ---
print("🌡️ Average Temperature Calculator")
choice = input("Read temperatures from (1) File or (2) Manual input? ")

if choice == "1":
    filename = "temperatures.txt"
    temperatures = read_temperatures_from_file(filename)
elif choice == "2":
    temperatures = read_temperatures_from_input()
else:
    print("Invalid choice.")
    temperatures = []

if temperatures:
    avg_temp = calculate_average(temperatures)
    print(f"\nTemperatures: {temperatures}")
    print(f"Average Temperature = {avg_temp:.2f} °C")
else:
    print("No temperature data available.")