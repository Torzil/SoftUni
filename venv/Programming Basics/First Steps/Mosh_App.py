weight = float(input("Weight: " ))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    (final_weight) = weight * 2.20
    print (f"Weight in Lbs: {final_weight}")
elif unit.upper == "L":
    final_weight = weight * 0.45
    print(f"Weight in Kg: {final_weight}")



