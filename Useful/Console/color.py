#Print all possible colors/styles
"""
start = '\033['
for i in range(0,100):
    print i, start + str(i) + 'm' + 'Hello, World!' + '\033[0m'
"""

class color:
    reset_all =     '\033[0m'
    
    class style:    
        bold =          '\033[01m'
        dim =           '\033[02m'
        italic =        '\033[03m'
        underline =     '\033[04m'
        blinking =      '\033[05m'
        inverted =      '\033[07m'
        invisible =     '\033[08m'
        
    class fg:
        reset =         '\003[39m'
        
        black =         '\033[30m'
        dark_red =      '\033[31m'
        dark_green =    '\033[32m'
        dark_yellow =   '\033[33m'
        blue =          '\033[34m'
        magenta =       '\033[35m'
        cyan =          '\033[36m'
        grey =          '\033[37m'
        
        dark_grey =     '\033[90m'
        red =           '\033[91m'
        green =         '\033[92m'
        yellow =        '\033[93m'
        blue2 =         '\033[94m'
        magenta2 =      '\033[95m'
        light_cyan =    '\033[96m'
        light_grey =    '\033[97m'
    
    class bg:
        reset =         '\033[49m'
        
        black =         '\033[40m'
        red =           '\033[41m'
        green =         '\033[42m'
        yellow =        '\033[43m'
        blue =          '\033[44m'
        purple =        '\033[45m'
        cyan =          '\033[46m'
        light_grey =    '\033[47m'


if __name__ == "__main__":
    #Testing
    print "Normal Text"
    print
    print color.fg.black + "Black Text"
    print color.fg.dark_red + "Dark Red Text"
    print color.fg.red + "Red Text"
    print color.fg.dark_green + "Dark Green Text"
    print color.fg.green + "Green Text"
    print color.fg.dark_yellow + "Dark Yellow Text"
    print color.fg.yellow + "Yellow Text"
    print color.fg.blue + "Blue Text"
    print color.fg.magenta + "Magenta Text"
    print color.fg.cyan + "Cyan Text"
    print color.fg.light_cyan + "Light Cyan Text"
    print color.fg.grey + "Grey Text"
    print color.fg.light_grey + "Light Grey Text" + color.fg.reset
    print
    print color.bg.black + "Black Background" + color.bg.reset
    print color.bg.red + "Red Background"  + color.bg.reset
    print color.bg.green + "Green Background"  + color.bg.reset
    print color.bg.yellow + "Yellow Background"  + color.bg.reset
    print color.bg.blue + "Blue Background"  + color.bg.reset
    print color.bg.purple + "Purple Background"  + color.bg.reset
    print color.bg.cyan + "Cyan Background"  + color.bg.reset
    print color.bg.light_grey + "Light Grey Background" + color.bg.reset
    print
    print color.fg.yellow + color.style.bold + "Bold Text" + color.reset_all
    print color.fg.yellow + color.style.dim + "Dim Text" + color.reset_all
    print color.fg.yellow + color.style.italic + "Italic Text" + color.reset_all
    print color.fg.yellow + color.style.underline + "Underlined Text" + color.reset_all
    print color.fg.yellow + color.style.blinking + "Blinking Text" + color.reset_all
    print color.fg.yellow + color.style.inverted + "Inverted Text" + color.reset_all
    print color.fg.yellow + color.style.invisible + "Invisible Text" + color.reset_all

