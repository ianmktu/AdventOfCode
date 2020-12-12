def day4():
    passports = [line.rstrip() for line in open('input.txt')]

    single_passports = []
    current_passport = {}
    for index, line in enumerate(passports):
        if line == "":
            single_passports.append(current_passport)
            current_passport = {}
        else:
            split_line = line.split(" ")
            for item in split_line:
                info = item.split(":")
                current_passport[info[0]] = info[1]

        if index == len(passports) - 1:
            single_passports.append(current_passport)
            current_passport = {}

    num_valid_passports = 0
    for passport in single_passports:
        if all(k in passport for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
            num_valid_passports += 1

    print("\n****************************************************")
    print("\nDay 4: Part 1")
    print("Total Passports: {}".format(len(single_passports)))
    print("Valid Passports: {}".format(num_valid_passports))

    num_valid_passports = 0
    for passport in single_passports:
        if all(k in passport for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
            if len(passport['byr']) == 4 and (int(passport['byr']) < 1920 or int(passport['byr']) > 2002):
                continue
            if len(passport['iyr']) == 4 and (int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020):
                continue
            if len(passport['eyr']) == 4 and (int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030):
                continue
            if "cm" not in passport['hgt'] and "in" not in passport['hgt']:
                continue
            if "cm" in passport['hgt'] and (int(passport['hgt'].replace("cm", "")) < 150 or int(passport['hgt'].replace("cm", "")) > 193):
                continue
            if "in" in passport['hgt'] and (int(passport['hgt'].replace("in", "")) < 59 or int(passport['hgt'].replace("in", "")) > 76):
                continue
            valid_colour_chars = set('0123456789abcdef')
            if len(passport['hcl']) != 7 or passport['hcl'][0] != '#' or any((c not in valid_colour_chars) for c in passport['hcl'][1:]):
                continue
            if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                continue
            valid_pid_chars = set('0123456789')
            if len(passport['pid']) != 9 or any((c not in valid_pid_chars) for c in passport['pid']):
                continue
            num_valid_passports += 1

    print("\nDay 4: Part 2")
    print("Total Passports: {}".format(len(single_passports)))
    print("Valid Passports: {}".format(num_valid_passports))
    print("\n****************************************************")


if __name__ == '__main__':
    day4()