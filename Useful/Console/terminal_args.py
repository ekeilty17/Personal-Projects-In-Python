import sys

def get_args_sys():
    
    tags = {    "--age" : {"val":None, "type":int},
                "--pet" : {"val":"dog", "type":str}
            }
    
    for arg in sys.argv[1:]:

        i = arg.find('=') 
        key = arg[:i]
        val = arg[i+1:]

        if key in tags:
            tags[key]["val"] = tags[key]["type"](val)
    
    return tags

print(get_args_sys())



from argparse import ArgumentParser

def get_args_parser():
    parser = ArgumentParser(description="Getting arguments from terminal")

    parser.add_argument('--age', default=None, type=int, required=True, help='How old are you?')
    parser.add_argument('--pet', type=str, default='dog', choices=['dog', 'cat', 'fish', 'snake'])

    args = parser.parse_args()

    return args

print(get_args_parser())
