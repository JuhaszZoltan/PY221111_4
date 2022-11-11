def van_benne_paros(sorozat:list[int]) -> bool:
    for n in sorozat:
        if n % 2 == 0:
            return True
    return False


def lin_kereses(sorozat:list[int], keresett_ertek:int) -> int:
    index:int = 0
    while index < len(sorozat):
        if sorozat[index] == keresett_ertek:
            return index
        index += 1
    return -1