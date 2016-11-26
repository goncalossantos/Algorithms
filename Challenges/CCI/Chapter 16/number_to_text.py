
tens = [
    "_", "_", "twenty", "thirty", "torty",
    "fifty", "sixty", "seventy", "eighty",
    "ninety",
]

digits = [
    "zero",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten",
    "eleven", "twelve", "thirteen", "fourteen",
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
]

negative = "Negative"
hundred = "hundred"
group_index = ["", "thousand", "million", "billion", "trillion", "quadrillion"]


def convert_group(i, group):

    prefix = []
    suffix = []

    # Deal with suffix
    if len(group_index) > i:
        suffix = group_index[i]
    else:
        raise Exception("Number too big")

    # Deal with the hundreds
    if len(group) == 3 and int(group) > 0:
        prefix.append(digits[int(group[0])])
        prefix.append(hundred)
        # Hundreds deal with, lets remove from consideration
        group = group[1:]

    # Deal with > 20 and < 100 groups
    if len(group) == 2 and int(group) >= 20:
        prefix.append(tens[int(group[0])])
        group = group[1:]

    # Deal with < 20 groups
    if int(group) > 0:
        prefix.append(digits[int(group)])

    # Append the suffix
    prefix.append(suffix)
    return prefix


def number_to_text(number):

    result = []
    prefix = ""
    # If negative convert to positive
    if number < 0:
        number = -number
        prefix = negative
    if number == 0:
        return digits[0]
    chars = str(number)
    # reverse number
    chars = chars[::-1]
    # group number by groups of 3 chars, starting with the least
    # significate digit
    groups = [chars[i:i + 3][::-1] for i in range(0, len(chars), 3)]
    result = []
    # convert every group
    for i, group in enumerate(groups):
        result.append(" ".join(convert_group(i, group)))

    # return the string - reversed to get back to the normal order
    return prefix + " " + " ".join(reversed(result))


def test_number_to_text():

    expected = "Negative one hundred twenty three " \
        "billion four hundred fifty " \
        "six million seven hundred "\
        "eighty nine thousand one "\
        "hundred twenty three "
    result = number_to_text(-123456789123)
    assert result == expected

