user_data = {}

# Loop exactly 10 times to get data for 10 users
for i in range(1, 11):
    print(f"\n--- Data for User {i} ---")

    # Optional: Get a name for the user to use as a dictionary key,
    # or just use "User 1", "User 2", etc.
    user_key = input(f"Enter name for User {i} (or press Enter to use 'User {i}'): ").strip()
    if not user_key:
        user_key = f"User {i}"

    # Inner while loop for input validation and exception handling
    while True:
        try:
            weight = float(input("Enter the weight in kgs: "))
            height = float(input("Enter the height in metres: "))

            if weight > 0 and height > 0:
                break
            else:
                print("Value of weight/height must be positive.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter numeric values.")
# Calculate BMI
    bmi = weight / (height ** 2)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
        feedback = "Eat well"
    elif 18.5 <= bmi <= 24.9:
        category = "Healthy"
        feedback = "Keep consistent"
    elif 25.0 <= bmi <= 29.9:
        category = "Overweight"
        feedback = "Exercise regularly"
    else:
        category = "Obese"
        feedback = "Consult a health expert"
        print(f"BMI is {bmi:.2f} and you are {category} --> {feedback}")
# Store the results in the dictionary
    user_data[user_key] = {
        "Weight (kg)": weight,
        "Height (m)": height,
        "BMI": round(bmi, 2),
        "Category": category
    }
# Display the final collected data
print("\n================ Final Collected Data ================")
