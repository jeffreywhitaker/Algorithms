#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    # break if not same ingredients
    if recipe.keys() != ingredients.keys():
        print('recipe keys', recipe.keys())
        print('ingredients keys', ingredients.keys())
        return 0

    # get lenth of dictionaries
    keysList = recipe.keys()
    keysList = list(keysList)
    print('keysList', keysList)

    # make an array
    howManyCanBeMade = []

    # divide to get an answer for each ingredient
    for key in keysList:
        howManyPerIngredient = ingredients[key] // recipe[key]
        print('how Many Per Ingredient', key, howManyPerIngredient)
        howManyCanBeMade.append(howManyPerIngredient)

    # return lowest number in array
    return min(howManyCanBeMade)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
