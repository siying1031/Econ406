'''
Siying homework2 Q1
'''
import math
from math import e

# Q1.a
def compute_elasticity(p1:float, p2:float, q1:float, q2:float) -> float:
    '''calculate elasticity based on the taylor-series approximation form givened
        by inputs of two prices and two quantities.

    Parameters
    ----------
    p1: float
        initial price
    p2: float
        new price
    p3: float
        initial sales
    p4: float
        new sales
    Returns
    -------
    elasiticity which is calculated by taylor-series approximation form.
    '''
    elastic = (math.log(q2/q1)) / (math.log(p2/p1))
    return abs(elastic)

# Q1.b
def check_elasticity(elasitic:float) -> str:
    '''check whether an elasticity is elastic, inelastic, or unit-elastic.

    Parameters
    ----------
    e : float
        elasiticity

    Returns
    -------
    str
        the descriptions of the elasiticity of demand.

    '''
    if elasitic < 0:
        elasitic = abs(elasitic)
    if elasitic != 1:
        if 0 < elasitic < 1:
            return str('The demand is inelastic ')

        else:
            return str('The demand is elastic')
    else:
        return str('The demand is unit elastic')

# Q1.c
def compute_demand(sales:float, init_price:float, new_price:float, elastic:float):
    '''calculates the predicted demand at the new price given by initial sales
    of a product, an initial price, a newprice, and an elasticity. Using the formula:
    [e = ln(q2/q1) / ln(p2/p1)]
    Parameters
    ----------
    sales : float
        initial slaes of the product
    initPrice : float
        initial price of the product
    newPrice : float
        new price of the product
    elastic : float
        elasticity of the product.

    Returns
    -------
    demand : float
        predicited demand

    '''
    demand = e**( math.log(sales) + elastic*(math.log(new_price)-math.log(init_price)) )
    return demand

#  e > 1 : elastic
#  0 < e < 1:inelastic
#  e = 1 unit-elastic

# Q1.d

def main():
    '''ask the user whether to calculate either ​elasticity​ or ​demand


    Returns
    -------
    dic:dictionary
    new prices as the key and demand quantities as the value

    '''
    temp = input('Press E: Calculate Elasticity | Press D: Calculate Demand: \n')
    if temp == 'E':
        old_price = float(input('Please enter the old price: \n'))
        new_price = float(input('Please enter the new price: \n'))
        old_quant = float(input('Please enter the old quantity:\n'))
        new_quant = float(input('Please enter the new quantity:\n'))
        print('The new elasticity is' , \
            str(compute_elasticity(old_price,new_price,old_quant,new_quant)), \
            check_elasticity(compute_elasticity(old_price,new_price,old_quant,new_quant)) )
    elif temp == 'D':
        sales = float(input('Please enter the sales quantity: \n'))
        init_price = float(input('Please enter the initial price: \n'))
        elastic = float(input('Please enter the elasticity: \n'))
        dic = {}
        num_data = int(input('Please enter the number of new prices need to be checked? \n'))
        for _ in range(num_data):
            new_price = float(input('Please enter the price: \n'))
            dic[new_price] = compute_demand(sales, init_price, new_price, elastic)
        print('The relationship between elasticity of demand and price are', dic)
        return
if __name__ == '__main__':
    main()