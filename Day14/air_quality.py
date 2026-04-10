## Air Quality Analyzer Program

aqi_data = []


# Load data
def load_data():
    aqi_data.clear()
    try:
        with open("aqi_data.txt", "r") as file:
            for line in file:
                city, aqi = line.strip().split(",")
                aqi_data.append({"city": city, "aqi": int(aqi)})
    except FileNotFoundError:
        pass


# Save data
def save_data():
    with open("aqi_data.txt", "w") as file:
        for entry in aqi_data:
            file.write(f"{entry['city']},{entry['aqi']}\n")
    print("Data saved successfully!")


# AQI category
def get_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 200:
        return "Unhealthy"
    else:
        return "Very Unhealthy"


# Add data
def add_data():
    city = input("Enter city name: ").strip()

    try:
        aqi = int(input("Enter AQI value: "))
    except ValueError:
        print("AQI must be a number!")
        return

    aqi_data.append({"city": city, "aqi": aqi})
    print("Data added!")


# View data
def view_data():
    if not aqi_data:
        print("No data available.")
        return

    print("\n===== AQI Records =====")
    for entry in aqi_data:
        print("-" * 30)
        print(f"City     : {entry['city']}")
        print(f"AQI      : {entry['aqi']}")
        print(f"Category : {get_category(entry['aqi'])}")
    print("-" * 30)


# Find most polluted city
def most_polluted():
    if not aqi_data:
        print("No data available.")
        return

    worst = max(aqi_data, key=lambda x: x["aqi"])
    print("\nMost Polluted City:")
    print("-" * 30)
    print(f"City     : {worst['city']}")
    print(f"AQI      : {worst['aqi']}")
    print(f"Category : {get_category(worst['aqi'])}")
    print("-" * 30)


# Main menu
def main():
    load_data()

    while True:
        print("\n===== Air Quality Analyzer =====")
        print("1. Add AQI Data")
        print("2. View All Data")
        print("3. Show Most Polluted City")
        print("4. Save Data")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_data()
        elif choice == "2":
            view_data()
        elif choice == "3":
            most_polluted()
        elif choice == "4":
            save_data()
        elif choice == "5":
            save_data()
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
