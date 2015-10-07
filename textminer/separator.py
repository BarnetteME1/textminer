def words(inputs):
    words = re.findall(r"(\w\S+[^\d ])", inputs)
    if words == []:
        return None
    else:
        return words


def phone_numbers(inputs):
    phone_number = {}
    numbers = re.findall(r"(\(?[\d]{3}\)?).?([\d]{3}.?[\d]{4})", inputs)
    if numbers == []:
        return None
    area_code, number = numbers[0]
    phone_number["number"] = number
    phone_number["area_code"] = area_code
    return phone_number


def money(inputs):
    if inputs.count(','):
        if not re.findall(r",\d{3}", inputs):
            return None
        inputs = re.findall(r"([^\,])", inputs)
        inputs = ''.join(inputs)
    cash_money = {}
    if inputs.count('.'):
        if not re.findall(r".\d{2}", inputs):
            return None
    if inputs.count('$') > 1:
        return None
    cash = re.findall(r"(\S)(\d+.?(?:\d+))", inputs)
    if len(cash[0]) < 2:
        return None
    symbol, amount = cash[0]
    if len(symbol) >1 and len(symbol) < 1:
        return None
    cash_money["currency"] = symbol
    cash_money["amount"] = float(amount)
    return cash_money


def zips(inputs):
    zip_code = {}
    full_zip = re.findall(r"(\d+)(-?\d{4})?", inputs)
    if full_zip == []:
        return None
    zips, plus4 = full_zip[0]
    if len(zips) != 5:
        return None
    zip_code["zip"] = zips
    if plus4 == '':
        plus4 = None
        zip_code["plus4"] = plus4
    else:
        zip_code["plus4"] = plus4[1:]
    return zip_code


def extract_date(inputs):
    tests = [r"(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4}|\d{2})",
            r"(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{2})"]
    for test in tests:
        match = re.match(test, inputs)
        if match:
            return match

def clean_date(year, month, day):
    day = int(day)
    month = int(month)
    year = int(year)

    return {"year": year, "month": month, "day": day}


def date(inputs):
    match = extract_date(inputs)
    if not match:
        return None
    ddict = match.groupdict()
    ddict = clean_date(**ddict)
    return ddict


## HARD MODE BEGINS


def date(inputs):


def hard_date(inputs):


def email(inputs):


def address(inputs):
