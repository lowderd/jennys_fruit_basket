#!usr/bin/python

# Challenge #243 Jenny's Fruit Basket
# https://www.reddit.com/r/dailyprogrammer/comments/3v4zsf/20151202_challenge_243_intermediate_jennys_fruit/

import fileinput
import inflect

from collections import defaultdict


# Inflect engine for creating making fruit names plural
inf_eng = inflect.engine()


def cart(market, goal):
    """
    This function returns a list of dictionaries containing the number of each
    fruit that should be purchased for the check out price to be exactly $5.
    :param market: List of tuples containing the fruit names and prices
    :param goal: Price target in cents
    :return: List of dictionaries containing the fruit to purchase
    """

    if goal < 0 or not market:
        # No solution
        return []

    if goal == 0:
        # Wooo!!! Solution found
        return [defaultdict(int)]

    fruit, price = market[0]

    in_cart = cart(market, goal - price)

    for answer in in_cart:
        answer[fruit] += 1

    add_to_cart = cart(market[1:], goal)

    return in_cart + add_to_cart


def print_solution(solution):
    """
    This function formats and prints solutions that were generated by the cart
    function.
    :param solution: Solution to print
    :return: None
    """
    solution_str = ""
    for key, val in solution.items():
        if val > 1:
            key = inf_eng.plural(key)
        solution_str += "{} {}, ".format(val, key)
    print(solution_str[:-2])

if __name__ == '__main__':
    market = []
    for line in fileinput.input():
        fruit, price = line.split()
        market.append((fruit, int(price)))

    num_solutions = 0
    for solution in cart(market, 500):
        print_solution(solution)
        num_solutions += 1

    print('Total Number of Solutions: {}'.format(num_solutions))
