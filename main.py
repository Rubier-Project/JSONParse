datax = {
    "name": "ali",
    "age": 4,
    "is_male": True,
    "is_femail": False,
    "result": {
        "have_sis": True,
        "sis_result": {
            "have_kos": True,
            "size_of_kos": 43
        }
    },
    1: 'kos',
    2: True,
    3: 6,
    4: {
        "kir": "kon"
    }
}

# set - tuple

import os

os.system("")

def TupleParse(data: tuple):
    d = "\033[00m( "
    num += 0

    for item in data:
        num += 1

        if type(item) == str:
            if len(data) - num == 0:
                d += f"\033[32m'{item}'\033[00m "
            else:
                d += f"\033[32m'{item}'\033[00m, "

        if type(item) == int:
            if len(data) - num == 0:
                d += f"\033[93m{item}\033[00m "
            else:
                d += f"\033[93m{item}\033[00m, "

        if type(item) == bool:
            if len(data) - num == 0:
                if item == True:
                    d += f"\033[94mtrue\033[00m "
                else:
                    d += f"\033[91mfalse\033[00m "
            
            else:
                if item == True:
                    d += f"\033[94mtrue\033[00m, "
                else:
                    d += f"\033[91mfalse\033[00m, "

        if type(item) == tuple:
            if len(data) - num == 0:
                d += f"\033[00m{TupleParse(item)}\033[00m "
            else:
                d += f"\033[00m{TupleParse(item)}\033[00m "

        if type(item) == dict:
            if len(data) - num == 0:
                d += f"\033[00m{DictParse(item)}\033[00m "
            else:
                d += f"\033[00m{DictParse(item)}\033[00m "

        if type(item) == list:
            if len(data) - num == 0:
                d += f"\033[00m{ListParse(item)}\033[00m "
            else:
                d += f"\033[00m{ListParse(item)}\033[00m "

        if type(item) == set:
            if len(data) - num == 0:
                d += f"\033[00m{SetParse(item)}\033[00m "
            else:
                d += f"\033[00m{SetParse(item)}\033[00m "

def SetParse(data: set):
    d = "\033[00m{ "
    num = 0

    for item in data:
        num += 1
        
        if type(item) == str:
            if len(data) - num == 0:
                d += f"\033[32m'{item}'\033[00m "
            else:
                d += f"\033[32m'{item}'\033[00m, "

        if type(item) == int:
            if len(data) - num == 0:
                d += f"\033[93m{item}\033[00m "
            else:
                d += f"\033[93m{item}\033[00m, "

        if type(item) == bool:
            if len(data) - num == 0:
                if item == True:
                    d += f"\033[94mtrue\033[00m "
                else:
                    d += f"\033[91mfalse\033[00m "

            else:
                if item == True:
                    d += f"\033[94mtrue\033[00m, "
                else:
                    d += f"\033[91mfalse\033[00m, "

    d += " \033[00m}"

def ListParse(data: list):
    d = "\033[00m[ "
    num = 0

    for item in data:
        num += 1

        if type(item) == str:
            if len(data) - num == 0:
                d += f"\033[32m'{item}'\033[00m "
            else:
                d += f"\033[32m'{item}'\033[00m, "
        
        if type(item) == int:
            if len(data) - num == 0:
                d += f"\033[93m{item}\033[00m "
            else:
                d += f"\033[93m{item}\033[00m, "

        if type(item) == bool:
            if len(data) - num == 0:
                if item == True:
                    d += f"\033[94mtrue\033[00m "
                else:
                    d += f"\033[91mfalse\033[00m "

            else:
                if item == True:
                    d += f"\033[94mtrue\033[00m, "
                else:
                    d += f"\033[91mfalse\033[00m, "

        if type(item) == list:
            if len(data) - num == 0:
                d += f"\033[93m{ListParse(item)}\033[00m "
            else:
                d += f"\033[93m{ListParse(item)}\033[00m, "

        if type(item) == dict:
            if len(data) - num == 0:
                d += f"\033[93m{DictParse(item)}\033[00m "
            else:
                d += f"\033[93m{DictParse(item)}\033[00m, "

        if type(item) == tuple:
            if len(data) - num == 0:
                d += f"\033[00m{TupleParse(item)}\033[00m "
            else:
                d += f"\033[00m{TupleParse(item)}\033[00m "

        if type(item) == set:
            if len(data) - num == 0:
                d += f"\033[00m{SetParse(item)}\033[00m "
            else:
                d += f"\033[00m{SetParse(item)}\033[00m "

    d += "\033[00m]"

    return d

def DictParse(data: dict):
    d = "\033[00m{ "
    num = 0

    for key, val in data.items():
        num += 1

        if type(key) == str and type(val) == str:
            if len(data.keys()) - num == 0:
                d += f"\033[00m{key}: \033[32m'{val}'\033[00m "
            else:
                d += f"\033[00m{key}: \033[32m'{val}'\033[00m, "

        if type(key) == str and type(val) == int:
            if len(data.keys()) - num == 0:
                d += f"\033[00m{key}: \033[93m{val}\033[00m "
            else:
                d += f"\033[00m{key}: \033[93m{val}\033[00m, "

        if type(key) == str and type(val) == bool:
            if len(data.keys()) - num == 0:
                if str(val) == "True":
                    d += f"\033[00m{key}: \033[94mtrue\033[00m "
                else:
                    d += f"\033[00m{key}: \033[91mfalse\033[00m "
            else:
                if str(val) == "True":
                    d += f"\033[00m{key}: \033[94mtrue\033[00m, "
                else:
                    d += f"\033[00m{key}: \033[91mfalse\033[00m, "

        if type(key) == int and type(val) == str:
            if len(data.keys()) - num == 0:
                d += f"\033[93m{key}\033[00m: \033[32m'{val}'\033[00m "
            else:
                d += f"\033[93m{key}\033[00m: \033[32m'{val}'\033[00m, "

        if type(key) == int and type(val) == int:
            if len(data.keys()) - num == 0:
                d += f"\033[93m{key}\033[00m: \033[93m{val}\033[00m "
            else:
                d += f"\033[93m{key}\033[00m: \033[93m{val}\033[00m, "

        if type(key) == int and type(val) == bool:
            if len(data.keys()) - num == 0:
                if str(val) == "True":
                    d += f"\033[93m{key}\033[00m: \033[94mtrue\033[00m "
                else:
                    d += f"\033[93m{key}\033[00m: \033[91mfalse\033[00m "
            else:
                if str(val) == "True":
                    d += f"\033[93m{key}\033[00m: \033[94mtrue\033[00m, "
                else:
                    d += f"\033[93m{key}\033[00m: \033[91mfalse\033[00m, "

        if type(key) == int and type(val) == dict:
            if len(data.keys()) - num == 0:
                d += f"\033[93m{key}\033[00m: \033[00m{DictParse(val)} "
            else:
                d += f"\033[93m{key}\033[00m: \033[00m{DictParse(val)}, "

        if type(key) == int and type(val) == tuple:
            if len(data.keys()) - num == 0:
                d += f"\033[93m{key}\033[00m: \033[00m{TupleParse(val)} "
            else:
                d += f"\033[93m{key}\033[00m: \033[00m{TupleParse(val)}, "

        if type(key) == int and type(val) == set:
            if len(data.keys()) - num == 0:
                d += f"\033[93m{key}\033[00m: \033[00m{SetParse(val)} "
            else:
                d += f"\033[93m{key}\033[00m: \033[00m{SetParse(val)}, "

        if type(key) == int and type(val) == list:
            if len(data.keys()) - num == 0:
                d += f"\033[93m{key}\033[00m: \033[00m{ListParse(val)} "
            else:
                d += f"\033[93m{key}\033[00m: \033[00m{ListParse(val)}, "

        if type(key) == str and type(val) == dict:
            if len(data.keys()) - num == 0:
                d += f"\033[00m{key}\033[00m: \033[00m{DictParse(val)} "
            else:
                d += f"\033[00m{key}\033[00m: \033[00m{DictParse(val)}, "

        if type(key) == str and type(val) == tuple:
            if len(data.keys()) - num == 0:
                d += f"\033[00m{key}\033[00m: \033[00m{TupleParse(val)} "
            else:
                d += f"\033[00m{key}\033[00m: \033[00m{TupleParse(val)}, "

        if type(key) == str and type(val) == set:
            if len(data.keys()) - num == 0:
                d += f"\033[00m{key}\033[00m: \033[00m{SetParse(val)} "
            else:
                d += f"\033[00m{key}\033[00m: \033[00m{SetParse(val)}, "

        if type(key) == str and type(val) == list:
            if len(data.keys()) - num == 0:
                d += f"\033[00m{key}\033[00m: \033[00m{ListParse(val)} "
            else:
                d += f"\033[00m{key}\033[00m: \033[00m{ListParse(val)}, "

    d += "\033[00m}"

    return d
