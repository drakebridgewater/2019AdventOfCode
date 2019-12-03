import argparse
import sys
from typing import Optional, Sequence
import logging
import numpy


def main() -> None:
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description="")
    parser.add_argument('--log_lvl', default='info', choices=('debug', 'info'), help='logging level to display')
    parser.add_argument('func', type=str, help='Name of the function to call')
    parser.add_argument('args', type=int, nargs='*', help='Name of the function to call')

    args = parser.parse_args()
    logging.basicConfig(format='%(levelname)s:%(message)s', level=getattr(logging, str(args.log_lvl).upper()))

    print(globals()[args.func](*args.args))


def get_d1_input() -> Sequence[int]:
    d1_input = ("60566 53003 132271 130557 109138 64818 123247 148493 98275 67155 132365 133146 88023 92978 122790 84429 93421"
                " 76236 104387 135953 131379 125949 133614 94647 64289 87972 97331 132327 53913 79676 143110 79269 52366 62793 69437 97749 "
                " 83596 147597 115883 82062 63800 61521 139314 127619 85790 132960 141289 86146 146104 128708 133054 116777 128402 85043 "
                " 117344 107915 108669 108304 105300 75186 111352 112936 117177 93812 97737 61835 77529 145406 93489 75642 69806 109845 79133"
                " 60950 67797 111806 50597 50481 88338 102136 65377 55982 82754 68901 89232 63118 95534 98264 147706 80050 104953 "
                " 146758 122884 122024 129236 113818 58099 134318 136312 75124")
    return tuple(int(d) for d in d1_input.split())


def calculate_fuel(mass: int) -> int:
    return int(numpy.floor(mass / 3) - 2)


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
    :return: the sum of the fuel requirements
    """
    total_fuel = 0
    for m in get_d1_input():
        total_fuel += calculate_fuel(m)
    return int(total_fuel)


def d1p2(module_fuel: Optional[int] = None) -> int:
    """
    Problem description:
        During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence.
        Apparently, you forgot to include additional fuel for the fuel you just added.

        Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2.
        However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require
        negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead
         handled by wishing really hard, which has no mass and is outside the scope of this calculation.

        So, for each module mass, calculate its fuel and add it to the total.
        Then, treat the fuel amount you just calculated as the input mass and repeat the process,
         continuing until a fuel requirement is zero or negative. For example:

        - A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0,
         which would call for a negative fuel), so the total fuel required is still just 2.
        - At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel,
         which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for
         a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
        -The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

        What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account
        the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)
    :param module_fuel: used for testing and when specified the default of calling part one is not performed
    :return: the sum of the fuel requirements
    """
    module_fuel = (module_fuel,) if module_fuel else get_d1_input()
    logging.debug("input fuel: {}".format(module_fuel))

    def helper(in_mass: int):
        additional_fuel = calculate_fuel(in_mass)
        if additional_fuel <= 0:
            return 0

        logging.debug("additional_fuel is: {}".format(additional_fuel))
        return additional_fuel + helper(additional_fuel)

    return sum(helper(d) for d in module_fuel)


if __name__ == '__main__':
    sys.exit(main())
