from area_module import *

def area_cal():
    print("1. Circle")
    print("2. Triangle")
    print("3. Square")
    print("4. Rectangle")
    choice = input("Enter your choice (1-4): ").strip()
    try:
        if choice == "1":
            radius = float(input("Enter radius: "))
            result = circle(radius)
        elif choice == "2":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result = triangle(base, height)
        elif choice == "3":
            side = float(input("Enter side length: "))
            result = square(side)
        elif choice == "4":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            result = rectangle(length, width)
        else:
            print("Invalid choice")
            return
        print(f"Calculated Area: {result}")
    except ValueError as e:
        print(f"Wrong Value: {e}")
    except Exception as e:
        print(f"Error: {e}")

area_cal()