input_string = input()
new_string = input_string.lower()

sand_counter = new_string.count("sand")
water_counter = new_string.count("water")
fish_counter = new_string.count("fish")
sun_counter = new_string.count("sun")
total_words_found = sand_counter + water_counter + fish_counter + sun_counter

print(total_words_found)
