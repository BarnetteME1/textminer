def phone_numbers(text):
    phone_number = {}
    numbers = re.findall(r"(\(?[\d]{3}\)?.?[\d]{3}.?[\d]{4})", text)
    if numbers == []:
        return None
    return numbers


## HARD MODE BEGINS


def emails(text):
