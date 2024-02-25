def loading_bar(percent):
    if percent == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{percent}% [{'%' * int(percent / 10)}{'.' * int(10 - percent / 10)}]\nStill loading..."


percent_loaded = int(input())

print(loading_bar(percent_loaded))
