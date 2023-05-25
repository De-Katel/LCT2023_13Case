from pydantic_models import Booking, ListBooking


def serializer(result: tuple):
    dct = {5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'g', 10: 'h',
           11: 'i', 12: 'j', 13: 'k', 14: 'l', 15: 'm', 16: 'n',
           17: 'o', 18: 'p', 19: 'q', 20: 'r', 21: 't', 22: 'u',
           23: 'v', 24: 'x', 25: 'y', 26: 'z'}
    lst = []
    for res in result:
        flyclass = {dct.get(el): res[el] for el in range(5, 27)}
        lst.append(Booking(
            sdat_s=res[1],
            dd=res[4],
            dtd=res[2],
            fly_class=flyclass,
            demcluster=res[32]
            ))
    result = ListBooking(items=lst)
    return result