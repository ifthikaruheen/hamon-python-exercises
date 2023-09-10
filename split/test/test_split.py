from split.split import split
def test_split_simple():
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ratios = [0.5, 0.4, 0.1]
    
    
    result = split(items, ratios)
    print(split(items, ratios))
    # Check if the result is a list
    assert isinstance(result, list)
    
    # Check if the result has the expected number of sublists
    assert len(result) == len(ratios)
    
    # Check if all sublists are non-empty
    assert all(sublist for sublist in result)
    
    # Check if all sublists are subsets of the original items
    assert all(set(sublist).issubset(set(items)) for sublist in result)

test_split_simple()