# python is command line utility

import argparse     #it will help us to make command line utility
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'div':
        return args.x / args.y
    else:
        return "Something Went Wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float, default=1.0,
                        help="Enter first number. This is utility for calculation. Please contact us.")
    parser.add_argument('--y', type=float,default=2.0,
                        help="Enter second number, This is utility for calculation. Please contact us.")
    parser.add_argument('--o', type=str,default='add',
                        help="This is utility for calculation. Please contact us for more.")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


    '''
    we can run on powershall by using those kind of arguments.
    
PS C:\Users\Kinjal> cd ~
PS C:\Users\Kinjal> cd PycharmProjects


    PS C:\Users\Kinjal\PycharmProjects\LearnPython> python .\51_cmd_line_utility.py --x 7 --y 2 --o add
9.0
PS C:\Users\Kinjal\PycharmProjects\LearnPython> python .\51_cmd_line_utility.py --x 7 --y 2 --o sub
5.0
PS C:\Users\Kinjal\PycharmProjects\LearnPython> python .\51_cmd_line_utility.py --x 7 --y 2 --o mul
14.0
PS C:\Users\Kinjal\PycharmProjects\LearnPython> python .\51_cmd_line_utility.py --x 7 --y 2 --o div
3.5
    '''