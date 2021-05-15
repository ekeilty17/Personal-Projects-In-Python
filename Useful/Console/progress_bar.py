from sys import stdout
from time import sleep


# A bit more complex but can be very useful
def progressBar(name, value, endvalue=100, bar_length = 50, white_space = 20):
        percent = float(value) / endvalue
        arrow = '-' * int(round(percent*bar_length) - 1) + '>'
        spaces = ' ' * (bar_length - len(arrow))
        stdout.write("\r{0: <{1}} : [{2}]{3}%".format(name, white_space, arrow + spaces, int(round(percent*100))))
        stdout.flush()

        if value == endvalue:
             stdout.write('\n\n')

if __name__ == "__main__":
    """
    # Simple example of replacing a line
    stdout.write("This will be replaced: HELLO")
    stdout.flush()
    sleep(1)
    stdout.write("\rThis will be replaced: BYE  \n")
    stdout.flush()
    """

    for i in range(101):
        progressBar("Test", i)
        sleep(0.1)
