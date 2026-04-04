# Pretend you are trying to code a new feature for an analytics product your team is working on. You need to
#  represent website interaction data in your program. Each event your application receives will contain 
# an alphanumeric id, a timestamp, an interaction score, and coordinates of a point (x,y). 
# Interaction score is represented as a number between 0 and 100. Coordinates of a point can range 
# from -50 to 50. Please represent this data the way you think is best in your code. 
# Please write a unit test that shows your code works correctly.
# Feel free to make up the values in your sample data or use the data below.
# interaction-score	x-coordinate	y-coordinate
# 30	-40	-35
# 40	20	20
# 50	-15	-10
# 60	38	21
# 70	-50	-50
# Note: You are allowed to use the internet as needed and can use any programming language you liIMPORT









import matplotlib.pyplot as plt

data = [
(30, -40, -35),
(40, 20, 20),
(50, -15,	-10),
(70, -50,	-50)
]

scores = [d[0] for d in data]

x_cords = [d[1] for d in data]
y_cords = [d[2] for d in data]



plt.scatter(x_cords, y_cords, s=scores, alpha=0.6)

plt.xlabel("x-coordinate")
plt.ylabel("y-coordinate")
#..so on

plt.show()

# import numpy an np

# def plot (data, x_range=(-50, 50), y_range=(-50, 50), score=(0, 100)):
#     x_cords= np.arrey([d[0] for d in data])