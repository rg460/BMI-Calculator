# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# ![](https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv)

# **Warning** you should convert the result to a whole number. 


# 🚨 Don't change the code below 👇
height = input("enter your height in m: ");
weight = input("enter your weight in kg: ");
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Plan
# convert height from string to float and weight string to integer
height_int = float(height);
weigtht_int = float(weight);
# print(type(height_int));
# Square height_int and store in varaible 
height_squared = height_int * height_int;
# calculate BMI and make whole number
BMI = int(weigtht_int / height_squared)
# print BMI result
print(BMI);
# convert BMI into a string and store in variable 
BMI_string = str(BMI)
# print a sentence telling the user their BMI 
print("Your BMI is " + BMI_string );

