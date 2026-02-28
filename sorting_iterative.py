#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) - Must check all adjacent pairs in worst case
    Memory usage: O(1) - Only uses a constant amount of extra space"""
    # Check that all adjacent items are in order, return early if not
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) - Two nested loops, worst case when reversed
    Memory usage: O(1) - Sorts in place with constant extra space"""
    # Repeat until all items are in sorted order
    for i in range(len(items)):
        swapped = False
        # Swap adjacent items that are out of order
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        # If no swaps occurred, list is sorted
        if not swapped:
            break


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) - Two nested loops regardless of input
    Memory usage: O(1) - Sorts in place with constant extra space"""
    # Repeat until all items are in sorted order
    for i in range(len(items) - 1):
        # Find minimum item in unsorted items
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        # Swap it with first unsorted item
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
