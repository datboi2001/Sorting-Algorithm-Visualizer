from DrawInformation import DrawInformation
from utilities import draw_list
from typing import List, Dict, Callable, Generator


class AlgorithmList:
    """
    A class that contains all of the sorting algorithm
    """
    def __init__(self, algo_dict: Dict[str, Callable[[DrawInformation, bool], Generator[bool, None, List[int]]]]):
        self._list = []
        for name, func_name in algo_dict.items():
            self._list.append((name, func_name))
        self._cur_pointer = 0

    def next(self) -> (str, Callable[[DrawInformation, bool], Generator[bool, None, List[int]]]):
        """
        Go to the next algorithm and return it
        """
        if self._cur_pointer < len(self._list) - 1:
            self._cur_pointer += 1
        else:
            self._cur_pointer = 0
        return self.get_current_algo()

    def back(self) -> (str, Callable[[DrawInformation, bool], Generator[bool, None, List[int]]]):
        """
        Move back to the previous algorithm and return it
        """
        if self._cur_pointer > 1:
            self._cur_pointer -= 1
        else:
            self._cur_pointer = len(self._list) - 1
        return self.get_current_algo()

    def get_current_algo(self) -> (str, Callable[[DrawInformation, bool], Generator[bool, None, List[int]]]):
        """
        Return the current algorithm
        """
        return self._list[self._cur_pointer]


def bubble_sort(draw_info: DrawInformation, ascending: bool) -> Generator[bool, None, List[int]]:
    """

    :param draw_info: DrawInformation object
    :param ascending: Boolean that indicates whether the algorithm is sorted ascending order or descending order
    :return: None, mutates array on UI instead
    """
    array = draw_info.array
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            num1 = array[j]
            num2 = array[j + 1]
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True
    return array


def insertion_sort(draw_info: DrawInformation, ascending: bool) -> Generator[bool, None, List[int]]:
    """

    :param draw_info: DrawInformation object
    :param ascending: Boolean that indicates whether the algorithm is sorted ascending order or descending order
    :return: None, mutates array on UI instead
    """
    array = draw_info.array

    for i in range(1, len(array)):
        current = array[i]

        while True:
            ascending_sort = i > 0 and array[i - 1] > current and ascending
            descending_sort = i > 0 and array[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            array[i] = array[i - 1]
            i -= 1
            array[i] = current
            draw_list(draw_info, {i: draw_info.GREEN, i - 1: draw_info.RED}, True)
            yield True
    return array


def merge_sort(draw_info: DrawInformation, ascending: bool) -> Generator[bool, None, List[int]]:
    """

    :param draw_info: DrawInformation object
    :param ascending: Boolean that indicates whether the algorithm is sorted ascending order or descending order
    :return: None, mutates array on UI instead
    """

    array = draw_info.array
    low = 0
    high = len(array) - 1

    # sort list `array` using a temporary list `temp`
    temp = array.copy()
    # divide the list into blocks of size `m`
    # m = [1, 2, 4, 8, 16…]

    m = 1
    while m <= high - low:

        # for m = 1, i = [0, 2, 4, 6, 8…]
        # for m = 2, i = [0, 4, 8, 12…]
        # for m = 4, i = [0, 8, 16…]
        # …

        for i in range(low, high, 2 * m):
            frm = i
            mid = i + m - 1
            to = min(i + 2 * m - 1, high)
            k = frm
            i = frm
            j = mid + 1

            # loop till no elements are left in the left and right runs
            while i <= mid and j <= to:
                if array[i] < array[j] and ascending or array[i] > array[j] and not ascending:
                    temp[k] = array[i]
                    draw_list(draw_info, {k: draw_info.RED, i: draw_info.GREEN}, True)
                    yield True
                    i = i + 1
                else:
                    temp[k] = array[j]
                    draw_list(draw_info, {k: draw_info.RED, j: draw_info.GREEN}, True)
                    yield True
                    j = j + 1

                k = k + 1

            # copy remaining elements
            while i < len(array) and i <= mid:
                temp[k] = array[i]
                draw_list(draw_info, {k: draw_info.RED, i: draw_info.GREEN}, True)
                yield True
                k = k + 1
                i = i + 1

            for i in range(frm, to + 1):
                array[i] = temp[i]
        m = 2 * m
    return array


def quick_sort(draw_info: DrawInformation, ascending: bool) -> Generator[bool, None, List[int]]:
    """

    :param draw_info: DrawInformation object
    :param ascending: Boolean that indicates whether the algorithm is sorted ascending order or descending order
    :return: None, mutates array on UI instead
    """
    array = draw_info.array
    high, low = len(array) - 1, 0
    # Create an auxiliary stack
    size = high - low + 1
    stack = [0] * size

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top += 1
    stack[top] = low
    top += 1
    stack[top] = high
    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1

        # Set pivot element at its correct position in
        # sorted array
        store_index = (low - 1)
        x = array[high]

        for j in range(low, high):
            if array[j] < x and ascending or array[j] > x and not ascending:
                # increment index of smaller element
                store_index = store_index + 1
                array[store_index], array[j] = array[j], array[store_index]
                draw_list(draw_info, {store_index: draw_info.RED, j: draw_info.BLUE, high: draw_info.GREEN}, True)
                yield True
        array[store_index + 1], array[high] = array[high], array[store_index + 1]
        draw_list(draw_info, {store_index + 1: draw_info.GREEN, high: draw_info.RED}, True)
        yield True
        p = store_index + 1
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = p - 1
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < high:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = high
    return array
