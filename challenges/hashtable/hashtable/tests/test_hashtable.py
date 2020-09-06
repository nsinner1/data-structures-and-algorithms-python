from hashtable.hashtable import HashTable


def test_hashtable_default_size():
    hashtable = HashTable()
    expected = 1024
    actual = hashtable.size
    assert actual == expected


def test_hashtable_size_58_pass():
    hashtable = HashTable(58)
    expected = 58
    actual = hashtable.size
    assert actual == expected


def test_hashtable_size_58_fail():
    hashtable = HashTable(58)
    expected = 57
    actual = hashtable.size
    assert actual != expected


def test_single_hash_pass():
    hashtable = HashTable()
    hashtable.add('roger', 45)
    actual = hashtable.get('roger')
    expected = 45
    assert actual == expected


def test_single_hash_fail():
    hashtable = HashTable()
    hashtable.add('roger', 45)
    actual = hashtable.get('roger')
    expected = 44
    assert actual != expected


def test_no_random_hash():
    hashtable = HashTable()
    one = hashtable._hash('test')
    two = hashtable._hash('test')
    three = hashtable._hash('test')
    four = hashtable._hash('test')
    five = hashtable._hash('test')
    assert one == two == three == four == five


def test_add_collision():
    hashtable = HashTable()
    bucket_number_1 = hashtable.add('test_key', 'test_value')
    bucket_number_2 = hashtable.add('tset_key', 'tset_value')
    bucket_number_3 = hashtable.add('tste_key', 'tste_value')

    assert bucket_number_1 == bucket_number_2 == bucket_number_3
    assert hashtable._buckets[bucket_number_1].head.val[1] == 'test_value'
    assert hashtable._buckets[bucket_number_1].head.next.val[1] == 'tset_value'
    assert hashtable._buckets[bucket_number_1].head.next.next.val[1] == 'tste_value'


def test_contains_pass():
    hashtable = HashTable()
    hashtable.add('test_key', 'test_value')
    assert hashtable.contains('test_key') == True


def test_contains_fail():
    hashtable = HashTable()
    hashtable.add('test_key', 'test_value')
    assert hashtable.contains('not_test_key') == False