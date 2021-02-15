#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # find the largest number
    largestPrice = max(prices[1:])
    print('largest price', largestPrice)

    # get the point to stop searching
    sellIndex = prices.index(largestPrice)
    print('sellIndex', sellIndex)

    # shorten the array
    sellListPrices = prices[:sellIndex]
    print('sellListPrices', sellListPrices)

    # find the lowest number before that
    smallestPrice = min(sellListPrices)
    print('smallest price', smallestPrice)

    # retun negative lowest number, plus highest number
    return -smallestPrice + largestPrice


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
