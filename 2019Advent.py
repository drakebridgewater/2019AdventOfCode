#!/usr/mgc/peteoss/bin/python3
import numpy
import argparse
import sys


def main() -> None:
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description="")
    parser.add_argument('func', type=str, help='Name of the function to call')

    args = parser.parse_args()
    print(globals()[args.func]())


def d1p1() -> int:
    """
    Problem description:
        The Elves quickly load you into a spacecraft and prepare to launch.

        At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

        Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three,
        round down, and subtract 2.

        For example:

        For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
        For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
        For a mass of 1969, the fuel required is 654.
        For a mass of 100756, the fuel required is 33583.
        The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module
        (your puzzle input), then add together all the fuel values.

        What is the sum of the fuel requirements for all of the modules on your spacecraft?
    :return:
    """
    d1_input = ("60566 53003 132271 130557 109138 64818 123247 148493 98275 67155 132365 133146 88023 92978 122790 84429 93421"
                " 76236 104387 135953 131379 125949 133614 94647 64289 87972 97331 132327 53913 79676 143110 79269 52366 62793 69437 97749 "
                " 83596 147597 115883 82062 63800 61521 139314 127619 85790 132960 141289 86146 146104 128708 133054 116777 128402 85043 "
                " 117344 107915 108669 108304 105300 75186 111352 112936 117177 93812 97737 61835 77529 145406 93489 75642 69806 109845 79133"
                " 60950 67797 111806 50597 50481 88338 102136 65377 55982 82754 68901 89232 63118 95534 98264 147706 80050 104953 "
                " 146758 122884 122024 129236 113818 58099 134318 136312 75124")

    d1_module_weights = tuple(int(x) for x in d1_input.rsplit())
    total_fuel = 0
    for m in d1_module_weights:
        total_fuel += numpy.floor(m/3) - 2
    return int(total_fuel)


if __name__ == '__main__':
    sys.exit(main())
