import pytest

from assignment import (
    vocabulary,
    retrieve_from_dict,
    add_to_dict,
    update_dict,
    delete_from_dict,
    in_dict,
    loop_over_dict,
    loop_over_dict_values,
    dictionary_of_lists,
    dictionary_of_dictioaries
)

def test_vocabulary():
    assert vocabulary() == "key"

def test_retrieve_from_dict():
    assert retrieve_from_dict() == 2

def test_add_to_dict():
    result = add_to_dict()
    assert result['d'] == 4
    assert len(result) == 4

def test_update_dict():
    result = update_dict()
    assert result['b'] == 5
    assert len(result) == 3

def test_delete_from_dict():
    result = delete_from_dict()
    assert 'b' not in result
    assert len(result) == 2

def test_in_dict():
    assert in_dict({'a': 1, 'b': 2, 'c': 3}) == True
    assert in_dict({'a': 1, 'c': 3}) == False

def test_loop_over_dict():
    result = loop_over_dict({'a': 1, 'b': 2, 'c': 3})
    assert result == ['a', 'b', 'c']

def test_loop_over_dict_values():
    result = loop_over_dict_values({'a': 1, 'b': 2, 'c': 3})
    assert result == [1, 2, 3]

def test_dictionary_of_lists():
    result = dictionary_of_lists({'a': [1, 2], 'b': [3, 4, 5], 'c': [6, 7]})
    assert result == 5

def test_dictionary_of_dictioaries():
    result = dictionary_of_dictioaries({'a': {'x': 1}, 'b': {'c': 2}, 'c': {'d': 3}})
    assert result == 2

if __name__ == "__main__":
    pytest.main()