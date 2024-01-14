spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """
    Retrieves names from the list of foods.
    """
    # Extracting names using a list comprehension
    names = [food['name'] for food in spicy_foods]

    return names

def get_spiciest_foods(spicy_foods):
    """
    Returns foods with a heat_level over 5.
    """
    # Using a list comprehension to filter foods with heat_level over 5
    spiciest_foods = [food for food in spicy_foods if food.get('heat_level', 0) > 5]

    return spiciest_foods

def print_spicy_foods(spicy_foods):
    """
    Prints all foods formatted with 🌶 emojis.
    """
    for food in spicy_foods:
        name = food.get('name', 'Unknown Food')
        cuisine = food.get('cuisine', 'Unknown Cuisine')
        heat_level = food.get('heat_level', 0)

        # Creating a string with 🌶 emojis based on heat_level
        emoji_str = '🌶' * heat_level

        # Printing the formatted output
        print(f"{name} ({cuisine}) | Heat Level: {emoji_str}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Returns the food that matches a cuisine.
    """
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food

    return None

def print_spiciest_foods(spicy_foods):
    """
    Prints foods with heat_level over 5 formatted with 🌶 emojis.
    """
    for food in spicy_foods:
        name = food.get('name', 'Unknown Food')
        cuisine = food.get('cuisine', 'Unknown Cuisine')
        heat_level = food.get('heat_level', 0)

        # Check if the food is spiciest (heat_level over 5)
        if heat_level > 5:
            # Creating a string with 🌶 emojis based on heat_level
            emoji_str = '🌶' * heat_level

            # Printing the formatted output for spiciest foods
            print(f"{name} ({cuisine}) | Heat Level: {emoji_str}")

def get_average_heat_level(spicy_foods):
    """
    Returns the average of heat_levels in spicy_foods.
    """
    # Extracting heat_levels using a list comprehension
    heat_levels = [food.get('heat_level', 0) for food in spicy_foods]

    # Calculating the average
    if heat_levels:
        average_heat_level = sum(heat_levels) / len(heat_levels)
        return average_heat_level
    else:
        return 0 

def create_spicy_food(spicy_foods, new_spicy_food):
    """
    Returns the original list of spicy_foods with a new spicy_food added.
    """
    # Make a copy of the original list to avoid modifying it in-place
    updated_spicy_foods = spicy_foods.copy()

    # Add the new_spicy_food to the list
    updated_spicy_foods.append(new_spicy_food)

    return updated_spicy_foods