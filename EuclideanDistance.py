import math 

x_1= int(input("Enter first x value:  "))
y_1= int(input("Enter first y value:  "))
x_2= int(input("Enter second x value:  "))
y_2= int(input("Enter second y value:  "))
x_3= int(input("Enter third x value:  "))
y_3= int(input("Enter third y value:  "))


points = [(x_1,y_1),(x_2,y_2),(x_3,y_3)]
distances= []  

def euclideanDistance(point1,point2):
    distance= math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    return distance

for a in range (len(points)):
    for b in range(a + 1, len(points)):
        x = euclideanDistance(points[a], points[b])
        distances.append(x)
        
print("Calculated distances are: ", distances)        
print("Minimum distance is: " ,min(distances))
