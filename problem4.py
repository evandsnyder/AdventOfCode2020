#!/usr/local/bin/python3

import re

import time
start = time.time()

def readfile(file):
    data = []
    with open(file) as f:
        data = f.read().split('\n\n')

    passports = []
    for passport in data:
        passports.append(passport.replace('\n', ' ').split(' '))

    return passports

def problem1():
    passports = readfile('problem4.txt')
    count = 0
    for passport in passports:
        data = dict()
        for field in passport:
            info, content = field.split(':')
            data[info] = content
        if len(data) < 7 or (len(data) == 7 and "cid" in data):
            pass
        else:
            count += 1 
    print(count)

def isValid(passport):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.
    try:
        if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
            return False
        if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
            return False
        if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
            return False
        
        if len(passport["hgt"]) < 4: return False
        height = int(passport["hgt"][:-2])
        if passport["hgt"][-2:] == 'cm':
            if height >193 or height <150:
                return False
        else:
            if height > 76 or height < 59:
                return False
        

        hcl = re.compile("^#[0-9a-f]{6}$")
        if not hcl.match(passport["hcl"]):
            return False
        
        if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

        ppid = re.compile("^[0-9]{9}$")
        if not ppid.match(passport["pid"]):
            return False

    except NameError as e:
        print(e)
        print(passport)
        return False
    return True


def problem2():
    passports = readfile('problem4.txt')
    count = 0
    for passport in passports:
        data = dict()
        for field in passport:
            info, content = field.split(':')
            data[info] = content
        if len(data) < 7 or (len(data) == 7 and "cid" in data):
            continue
        if(isValid(data)):
            count += 1
    print(count)

problem1()
problem2()

print(time.time()-start)