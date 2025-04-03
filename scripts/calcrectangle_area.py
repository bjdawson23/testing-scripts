# A simple Python script to calculate the area of a rectangle

def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def main():
    print("Welcome to the Rectangle Area Calculator!")
    
    # Get user input
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        
        # Calculate the area
        area = calculate_area(length, width)
        
        # Display the result
        print(f"The area of the rectangle is: {area:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()