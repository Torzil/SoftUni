balls_to_be_picked = int(input())
total_points = 0
number_of_red_balls = 0
number_of_orange_balls = 0
number_of_yellow_balls = 0
number_of_white_balls = 0
number_of_other_colors_picked = 0
divides_from_black_balls = 0

for ball in range(balls_to_be_picked):
    current_ball_color = input()
    if current_ball_color == "red":
        total_points += 5
        number_of_red_balls += 1
    elif current_ball_color == "orange":
        total_points += 10
        number_of_orange_balls += 1
    elif current_ball_color == "yellow":
        total_points += 15
        number_of_yellow_balls += 1
    elif current_ball_color == "white":
        total_points += 20
        number_of_white_balls += 1
    elif current_ball_color == "black":
        total_points //= 2
        divides_from_black_balls += 1
    else:
        number_of_other_colors_picked += 1

print(f"Total points: {total_points}")
print(f"Red balls: {number_of_red_balls}")
print(f"Orange balls: {number_of_orange_balls}")
print(f"Yellow balls: {number_of_yellow_balls}")
print(f"White balls: {number_of_white_balls}")
print(f"Other colors picked: {number_of_other_colors_picked}")
print(f"Divides from black balls: {divides_from_black_balls}")
