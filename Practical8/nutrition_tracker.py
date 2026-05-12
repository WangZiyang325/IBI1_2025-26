# Practical 8: Nutrition Data Tracker
# Class and function to track daily calorie and nutrient intake.

class food_item:
    """
    A class to represent a food item with nutritional values.
    Attributes:
        name (str): Name of the food
        calories (float/int): Calories per serving
        protein (float/int): Protein in grams
        carbs (float/int): Carbohydrates in grams
        fat (float/int): Fat in grams
    """
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def calculate_daily_nutrition(food_list):
    """
    Calculate and display total nutrition from a list of food_item objects.
    Shows warnings if calories > 2500 or fat > 90g.
    """
    total_cal = 0
    total_prot = 0
    total_carb = 0
    total_fat = 0

    # Sum all nutrients
    for food in food_list:
        total_cal += food.calories
        total_prot += food.protein
        total_carb += food.carbs
        total_fat += food.fat

    # Display results
    print("\n=== 24-Hour Nutrition Summary ===")
    print(f"Total Calories:   {total_cal} kcal")
    print(f"Total Protein:    {total_prot} g")
    print(f"Total Carbohydrates: {total_carb} g")
    print(f"Total Fat:        {total_fat} g")

    # Warning conditions
    if total_cal > 2500:
        print("Warning: Calories exceed 2500 kcal!")
    if total_fat > 90:
        print("Warning: Fat exceeds 90 grams!")

# Example usage
if __name__ == "__main__":
    # Create food objects
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    chicken = food_item("Grilled Chicken", 250, 30, 0, 10)
    rice = food_item("White Rice", 200, 4, 45, 0.5)

    # Daily meal list
    daily_meals = [apple, chicken, rice]

    # Calculate and show results
    calculate_daily_nutrition(daily_meals)