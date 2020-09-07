from repeated_word.repeat_word import find_first_repeat


def test_regular_str():
    text = "Once upon a time in a forest far away"
    assert find_first_repeat(text) == "a"


def test_bigger_different_case():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    assert find_first_repeat(text) == "it"


def test_punktuation_case():
    text = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    assert find_first_repeat(text) == 'summer'