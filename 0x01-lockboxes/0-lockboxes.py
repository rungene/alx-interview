#!/usr/bin/python3
"""
0-lockboxes module
"""


def canUnlockAll(boxes):
    """
    Checks if boxes(provided as args) can be opended by provided
    keys
    Args:
        boxes: list of lists

    Return:
        True if all boxes can be opened, else return False
    """
    box_len = len(boxes)
    boxes_unlocked = [False] * box_len
    boxes_unlocked[0] = True

    def check_box(id_box):
        """Recursive function exploring keys in box"""
        for key in boxes[id_box]:
            if not boxes_unlocked[key]:
                boxes_unlocked[key] = True
                check_box(key)

    check_box(0)

    return all(boxes_unlocked)
