# FILE NAME - convert_C_to_F_02.py

# NAME: Amy Nuessle
# DATE: March 2 2026
# BRIEF DESCRIPTION:  Working off convert_C_to_F_01 adding conversion of F to C



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import math

########## ENTER YER CODE BELOW THIS LINE ##########
print("===== Temperature Converter =====")
print()
print("  1. Convert from Celsius to Fahrenheit")
print("  2. Convert from Fahrenheit to Celsius")
print()
choice = int(input("Please choose from the above menu: "))
temperature = float(input("Enter a temperature to convert: "))
print()

if choice == 1:
    fahrenheit_output = temperature * 9/5 + 32
    print("{} degrees Celsius is {} degrees Fahrenheit.".format(temperature, fahrenheit_output))

if choice == 2:
    celsius_output = (temperature - 32) * 5/9
    print("{} degrees Fahrenheit is {} degrees Celsius.".format(temperature, celsius_output))











########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab? The math equation for coverting from F to C was different than I expected, also got confused a bit on the line for choice







'''