from random import Random


def random_codes(n):
    random_length = 20
    codes = []
    random = Random()
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    for i in range(n):
        code = ''
        for j in range(random_length):
            code += chars[random.randint(0, len(chars) - 1)]
        codes.append(code)
    return codes


if __name__ == '__main__':
    codes = random_codes(200)
    print codes