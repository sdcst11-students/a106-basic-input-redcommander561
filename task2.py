#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

data = input("Please enter a number and then press the Enter Key")
data = int(data)
V = 1.33333333333333 * 3.14 * data **3

print(f"{V}")