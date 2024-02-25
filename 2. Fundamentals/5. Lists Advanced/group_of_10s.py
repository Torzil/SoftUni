def tens_splitter(nums_list):
    current_group = 10
    while nums_list:
        filtered_list = [num for num in nums_list if num <= current_group]
        for item in filtered_list:
            nums_list.remove(item)
        print(f"Group of {current_group}'s: {filtered_list}")
        current_group += 10


numbers_list = [int(number) for number in input().split(", ")]
tens_splitter(numbers_list)
