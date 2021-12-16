from pathlib import Path


def get_row(passport):
    lower_bound = 0
    upper_bound = 127

    for i in range(6):
        # range is 6 because there are 7 characters of
        # Fs and Bs (0 counts as 1)
        half = (upper_bound - lower_bound) // 2
        # / is divide and gives decimal
        # // gives the full divisible number
        # each time we're using lower bound as our base
        # must use upper and lower before if statements
        # otherwise it won't be able to assign them lower
        # down in the if statements
        if passport[i] == 'F':
            upper_bound = half
        # if F then take lower as 0 and upper as 63
        elif passport[i] == 'B':
            lower_bound = half + 1
        # if B then take lower as 64 and upper as 127
        # print(f"upper bound = {upper_bound}, lower bound = {lower_bound}")
    if passport[6] == 'F':
        # if the final character in the F B string is F then
        # return lower bound if not then upper bound
        return lower_bound

    else:
        return upper_bound


def get_col(passport):
    upper_bound = 7
    lower_bound = 0

    for i in range(2):
        # range is 2 because there are 3 characters for seat rows
        half = (upper_bound + lower_bound) // 2
        if passport[i] == 'R':
            lower_bound = half + 1

        elif passport[i] == 'L':
            upper_bound = half

    if passport[2] == 'L':
        return lower_bound

    else:
        return upper_bound


with open(Path(__file__).resolve().parent / "dummy.txt") as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    largest_seat = 0

    for passport in data:
        print(get_row(passport[:7]))
        row = get_row(passport[:7])
        # we are looping through i in passport for all
        # characters <7 (i.e. 1-6 inc.)
        print(get_col(passport[7:]))
        col = get_col(passport[7:])
        # now for characters at index 7 and on (i.e. 7-9 inc.)

        seat_id = row * 8 + col
        if seat_id > int(largest_seat):
            largest_seat = seat_id

print(largest_seat)
