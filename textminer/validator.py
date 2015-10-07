def binary_numbers(string):
    if re.search(r"[2-9]", string):
        return False
    return True


def binary_even(string):
    if re.search(r"0$", string):
        return True
    return False


def hexadecimal(string):
    if re.search(r"[A-F]\d", string):
        return True
    return False


def word(string):
    if re.findall(r"(\w+[^\d\S])", string):
        return True
    return False


def words(string):
    if re.findall(r"(\w+[^\d\S])", string):
        return True
    return False


def phone_numbers(string):
    if re.findall(r"(\(?[\d]{3}\)?).?([\d]{3}.?[\d]{4})", string)
        return True
    return False


def money(string):
    if string.count(','):
        if not re.findall(r",\d{3}", string):
            return False
        string = re.findall(r"([^\,])", string)
        string = ''.join(string)
    cash_money = {}
    if string.count('.'):
        if not re.findall(r".\d{2}", string):
            return False
    if string.count('$') > 1:
        return False
    cash = re.findall(r"(\S)(\d+.?(?:\d+))", string)
    if len(cash[0]) < 2:
        return False
    return True


def zips(string):
    zip_code = {}
    full_zip = re.findall(r"(\d+)(-?\d{4})?", string)
    if full_zip == []:
        return False
    zips, plus4 = full_zip[0]
    if len(zips) != 5:
        return False
    zip_code["zip"] = zips
    if plus4 == '':
        plus4 = False
    return True


def date(string):
    tests = [r"(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4}|\d{2})",
            r"(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{2})"]
    for test in tests:
        match = re.match(test, string)
        if match:
            return True


## HARD MODE BEGINS


def hard_date(string):


def email(string):


def address(string):
