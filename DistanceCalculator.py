import math

def calculate_travel_time(x1, y1, x2, y2):
    return 20 * math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
                          
def main():
    print("Enter the first coordinate (x1 y1):")
    x1, y1 = map(float, input().split())

    print("Enter the second coordinate (x2 y2):")
    x2, y2 = map(float, input().split())

    travel_time = calculate_travel_time(x1, y1, x2, y2)
    print("Travel time is "+str(travel_time))

main() # Call main() directly