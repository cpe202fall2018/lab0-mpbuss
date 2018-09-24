#
#Name: Morgan Buss
#Student ID: 012632655
#Date (last modified): 09/24/18
#
# Lab 00
# Section 14
# Purpose of Lab: To practice using python and submitting code via GitHub

# This function takes a user's weight input and displays what they would weigh on Mars and Jupiter
def weight_on_planets():
    user = float(input("What do you weigh on earth? "))
    mars = user*0.38
    jupiter = user*2.34
    print("\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds." % (mars,jupiter))

if __name__ == '__main__':
    weight_on_planets()
