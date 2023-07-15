def estimate_car_price(manufacturer: str, model: str, year: int, mileage: float) -> float:
    """Estimate the price of a used car given some attributes."""
    
    # Start with a base price
    base_price = 20000
    
    # Add or subtract value based on manufacturer
    if manufacturer == "Toyota":
        base_price += 2000
    elif manufacturer == "Honda":
        base_price += 1500
    elif manufacturer == "Ford":
        base_price -= 1000
        
    # Add or subtract value based on model 
    if model == "Camry":
        base_price += 1500
    elif model == "Civic":
        base_price += 1000
    elif model == "F-150":
        base_price += 500
        
    # Reduce price as years go up 
    base_price -= (2023 - year) * 500
    
    # Reduce price as mileage goes up
    base_price -= (mileage / 10000) * 1000
    
    return base_price

#print(estimate_car_price("Ford","Focus", 2000, 30000))
