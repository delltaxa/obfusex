import os
import base64
import random

from colorama import Fore, Back

################
logo = f"""{Fore.BLUE}       _      __                
      | |    / _|                    
  ___ | |__ | |_ _   _ ___  _____  __
 / _ \| '_ \|  _| | | / __|/ _ \ \/ /
| (_) | |_) | | | |_| \__ \  __/>  < 
 \___/|_.__/|_|  \__,_|___/\___/_/\_\\{Fore.RESET}
"""
#################

OFFSET = 30
VARIABLE_NAME = '_' * 100

def randomst_ints(count):
    result=""
    ints="0123456789"
    for x in range(count):
        result += ints[random.randint(0, ints.__len__() - 1)]
    return result

def addbuffer(st, buffer):
    result = ""
    for x in range(st.__len__()):
        if random.randint(1, 100) % 2 == 0:
            pass
        else:
            result += buffer 
        result += st[x]
    return result

def addbuffer_low(st, buffer):
    result = ""
    for x in range(st.__len__()):
        if random.randint(1, 100) % 8 == 0:
            pass
        else:
            result += buffer
        result += st[x]
    return result

def obfuscate(content):
    print(f" {Fore.BLUE}[*]{Fore.RESET} Adding buffer")
    print(f" {Fore.BLUE}[*]{Fore.RESET} Encoding payload + buffer")
    b64_content = base64.b64encode(addbuffer(addbuffer(addbuffer(content, "碼"), "國"), "大").encode()).decode()
    index = 0
    print(f" {Fore.BLUE}[*]{Fore.RESET} Generating variables\n")
    code = f'{VARIABLE_NAME} = ""; _______________________=b"\\xe7\\xa2\\xbc\\xe5\\x9c\\x8b\\xe5\\xa4\\xa7".decode(); ______________________=1; import base64 as ___________________________________________________________________; __________________________________________________________________ = ___________________________________________________________________.b64decode;'
    print(f" {Fore.YELLOW}[BUFFER_LOW]{Fore.GREEN} ", end='', flush='true')

    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)

        _str = base64.b64encode(_str.encode())
        _str = _str.decode()
        _str = addbuffer_low(str(_str), "碼")
        print(".", end='', flush='true')
        
        code += f'{VARIABLE_NAME} += (__________________________________________________________________("{_str}".replace(_______________________[______________________ - ______________________], "_________".replace("_", "")).encode() )).decode("unicode_escape");'
        index += OFFSET
    print(f" {Fore.RESET}\n")
    print(f" {Fore.BLUE}[*]{Fore.RESET} Fusing with main code")
    decoy = randomst_ints(4950)

    viriung = f"""____________________________________________________________________=___________________________________________________________________=__________________________________________________________________=_________________________________________________________________=________________________________________________________________=_______________________________________________________________=______________________________________________________________=_____________________________________________________________=____________________________________________________________=___________________________________________________________=__________________________________________________________="??????A///>>>>::APP[+67*(55)]"
if ________________________________________________________________==_______________________________________________________________:
    _______________________________________________________________="{decoy}"
    if ________________________________________________________________ != _______________________________________________________________: pass
    else: ____(___).___"""
    code += f'__________________________={VARIABLE_NAME};_________________________=1; ________________________=b"\\xe7\\xa2\\xbc\\xe5\\x9c\\x8b\\xe5\\xa4\\xa7".decode();_____="\\x75\\x74\\x66\\x2d\\x38";__=""*1;______=__import__;_______=exec;________="\\x62\\x61\\x73\\x65\\x36\\x34";_____________=_____; _______(______(________).b64decode(__________________________.encode(_____________)).decode(_____________).replace(________________________[_________________________ - _________________________], __).replace(________________________[_________________________], __).replace(________________________[_________________________ + _________________________], __))'
    
    print(f" {Fore.BLUE}[*]{Fore.RESET} Planting Decoy\n")

    code = viriung + "\n" + code
    
    print(f" {Fore.GREEN}[+] Stage 1 done!{Fore.RESET}\n")
    
    return code

def main():
    print(logo)
    try:
        file_content = """print("Hello, World!")"""

        obfuscated_content = obfuscate(file_content)

        print(f" {Fore.GREEN}[+] Obfuscation done!{Fore.RESET}")

        filename = "_obf.py"
        with open(filename, "w+") as f:
            f.write(obfuscated_content)
            f.close()


        print(f" {Fore.GREEN}[+] Wrote to {filename}")
        print()

        # print(obfuscated_content)
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()