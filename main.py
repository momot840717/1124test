def geometric_progression(first_num: int, ratio: float, n: int) -> tuple[float, list]:
    """ 等比數列、總和

    Args:
        first_num (int): 首項
        ratio (float): 等比
        n (int): 項數

    Returns:
        tuple[float, list]: 總和
    """
    gp = [first_num]
    for i in range(1, n):
        gp.append(ratio**(i))
    if ratio == 1:
        return first_num * n, gp
    return first_num * (1 - ratio ** n)/ (1-ratio), gp

def arithmetic_progression(first_num: int, difference: float, n: int) -> tuple[float, list]:
    """ 等差數列、總和

    Args:
        first_num (int): 首項
        difference (float): 等差
        n (int): 項數

    Returns:
        tuple[float, list]: 總和
    """
    ap = [first_num]
    for i in range(1, n):
        ap.append(first_num + difference * i)
    return n*(first_num + first_num + (n-1) * difference)/2 , ap


print(geometric_progression(1, 2, 5))
print(arithmetic_progression(1, 2, 5))