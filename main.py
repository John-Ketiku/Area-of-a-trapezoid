game.splash("Let's calculate the area a trapezoid")
Base = game.ask_for_number("Enter the base1 of trapezoid (cm):")
Base_2 = game.ask_for_number("Enter the base2 of trapezoid (cm):")
Height = game.ask_for_number("Enter the height of trapezoid (cm) :")
Area = (Base + Base_2) * Height / 2
game.splash("The area of a trapezoid dimensions:" + str(Base) + "cm by" + str(Base_2) + "cm is " + convert_to_text(Area) + "cm^2")
game.splash("Done")