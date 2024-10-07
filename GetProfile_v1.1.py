import csv
from faker import Faker

# Create a Faker instance
fake = Faker()

# Function to generate a fake profile
def generate_profile():
    return {
        "Name": fake.name(),
        "Address": fake.address(),
        "Email": fake.email(),
        "Phone Number": fake.phone_number(),
        "Job": fake.job(),
        "Company": fake.company(),
        "DOB": fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=80),
    }

# Function to save profiles to a CSV file
def save_profiles_to_csv(profiles, filename):
    # Get the profile keys (header for CSV)
    fieldnames = profiles[0].keys()

    # Write to the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(profiles)
    print(f"Profiles saved to {filename} successfully!")

# Main function to run the script
if __name__ == "__main__":
    try:
        count = int(input("How many profiles would you like to generate? "))
        profiles = [generate_profile() for _ in range(count)]
        filename = input("Enter the filename to save profiles (e.g., profiles.cs>")
        save_profiles_to_csv(profiles, filename)
    except ValueError:
        print("Please enter a valid number.")
