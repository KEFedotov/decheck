import os
from pyats.easypy import Task


def main():
    test_path = os.path.dirname(os.path.abspath(__file__))
    testscripts = [
        os.path.join(test_path, 'a1_check.py'),
        os.path.join(test_path, 'a2_check.py'),
        os.path.join(test_path, 'a3_check.py')
    ]

    for task in testscripts:
        sub_check = Task(testscript = task)
        sub_check.start()
        sub_check.wait()
    