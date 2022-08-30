def top_n(items, n):
    """Return the top n items in an array, in descending order.

    Args:
        items (array): list or array-like object containing numerical values.
        n (int): number of top items to return.

    Returns:
        array: top n items, in descending order.

    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 3]
    """
    for i in range (n): # keep sorting until we have top items
        for j in range(len(items)-1-i):

            if items [j] > items[j+1]: # If this item is bigger than the next items
                items[j], items[j+1] = items[j+1], items[j] # swop the two

    #get last two items
    top_n = items[-n:]

    #Return in desc order
    return top_n[::-1]
