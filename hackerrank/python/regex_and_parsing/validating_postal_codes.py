regex_integer_in_range = r"^[1-9][\d]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

# ^     start of the string
# [1-9] any number between 1 and 9
# [\d]  any number
# {5}   the previous condition must apply n times
# $     end of the string
