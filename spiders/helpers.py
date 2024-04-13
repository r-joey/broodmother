def convert_price_to_float(price_str):
        # Remove any non-numeric characters except for the decimal point
        price_str = ''.join(char for char in price_str if char.isdigit() or char == '.')

        # Convert the cleaned string to a float
        try:
            price_float = float(price_str)
            return price_float
        except ValueError:
            print("Invalid price format")
            return 0.0