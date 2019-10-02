"""
The simplest solution for this is to use recursion. See the code below for the solution.

NOTE: Code primarily taken from source below.
SEE: https://www.youtube.com/watch?v=8lhxIOAfDss
"""


def move(move_from, move_to):
    """Prints the move taken in solving the hanoi problem.

    Parameters
    ----------
    move_from(str): Initial pilar of discs
    move_to(str): Pillar to move the discs to
    """
    print(f"Move disc from {move_from} to {move_to}!")

def hanoi(num_of_discs, move_from, helper, move_to ):
    """
    A function to solve the towers of hanoi problem.
    
    Parameters
    ----------
    num_of_discs(int): How many discs are on the initial pillar
    move_from(str): Initial pilar of discs
    helper(str): The pillar to move the discs via (whichever is left)
    move_to(str): Pillar to move the discs to
    """
    if num_of_discs == 0: # Base case
        pass
    else: # Solve the remaining puzzle
        hanoi(num_of_discs-1, move_from, move_to, helper)
        move(move_from, move_to)
        hanoi(num_of_discs-1, helper, move_from, move_to )

if __name__ == "__main__":

    discs = int(input("How many discs are on the tower?: "))
    hanoi(discs, "A", "B", "C")