import datetime as dt

def mean(value):
    if isinstance(value, list):
        the_mean = sum(value) / len(value)
    else:
        the_mean = sum(value.values()) / len(value)

    return the_mean

def pow(numb, power):
    return numb ** power

def ounces_to_ml(qty):
    print(qty,  'ounces =', (29.57353 * qty), 'milliliters')

x = dt.datetime.now()
print("timestamp", x)

rates = [32, 43, 43, 54, 65]
rates.append(43)
rates.append(43)
rates.append(43)

ratesDict = {"abs": 43, "sample": 33, "sam": 20}

print('mean of list', mean(rates))
print('mean of dict', mean(ratesDict))

number = float(input('Enter number'))
message = f'square of {number} is {pow(number, 2)}'
print(message)
# for i in range(4):
#     ounces_to_ml(i)

# for i in range(4):
#     print('square of', i, 'is', pow(i, i))
