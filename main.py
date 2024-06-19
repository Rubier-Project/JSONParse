datax = {
    "name": "ali",
    "age": 4,
    "is_male": True,
    "is_femail": False,
    "result": {
        "have_sis": True
    }
}

import os

os.system("")

def DictParse(data: dict):
    d = "{ "
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

        if type(key) == str and type(val) == dict:
            d += f"\033[00m{key}: \033[00m{DictParse(val)}"

    d += "\033[00m}"

    return d

print(DictParse(datax))
