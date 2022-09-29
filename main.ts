game.splash("Let's calculate the area a trapezoid")
let Base = game.askForNumber("Enter the base1 of trapezoid (cm):")
let Base_2 = game.askForNumber("Enter the base2 of trapezoid (cm):")
let Height = game.askForNumber("Enter the height of trapezoid (cm) :")
let Area = (Base + Base_2) * Height / 2
game.splash("The area of a trapezoid dimensions:" + Base + "cm by" + Base_2 + "cm is " + convertToText(Area) + "cm^2")
game.splash("Done")
