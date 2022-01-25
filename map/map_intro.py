import timeit


text = "what have the romans ever done for us"


def comp_caps():
    capitals = [char.upper() for char in text]
    return capitals


#  use map
def map_caps():
    map_capitals = list(map(str.upper, text))
    return map_capitals


def comp_words():
    words = [word.upper() for word in text.split(' ')]
    return words


#  use map
def map_words():
    map_w = list(map(str.upper, text.split(' ')))
    return map_w


if __name__ == "__main__":
    # print(timeit.timeit("x = comp_caps()", setup="from __main__ import comp_caps", number=1000))
    # print(timeit.timeit("x = map_caps()", setup="from __main__ import map_caps", number=1000))
    # print(timeit.timeit("x = comp_words()", setup="from __main__ import comp_words", number=1000))
    # print(timeit.timeit("x = map_words()", setup="from __main__ import map_words", number=1000))
    print(timeit.timeit(comp_caps, number=100000))
    print(timeit.timeit(map_caps, number=100000))
    print(timeit.timeit(comp_words, number=100000))
    print(timeit.timeit(map_words, number=100000))
