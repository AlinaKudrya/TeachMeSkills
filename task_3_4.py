entered_string = input()
middle_letter = round(len(entered_string)/2)
print(f"middle letter {entered_string[middle_letter]}")
if entered_string[middle_letter] == entered_string[0]:
    print(entered_string[entered_string[middle_letter]:])

