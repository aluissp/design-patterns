from round import RoundHole
from round import RoundPeg
from square import SquarePeg
from adapters import SquarePegAdapter


def main():
    # Round fits round, no surprise.
    hole = RoundHole(5)
    rpeg = RoundPeg(5)

    if hole.fits(rpeg):
        print('Round peg r5 fits round hole r5.')

    smallSqPeg = SquarePeg(2)
    largeSqPeg = SquarePeg(20)
    # hole.fits(smallSqPeg); # Won't compile.

    # Adapter solves the problem.
    smallSqPegAdapter = SquarePegAdapter(smallSqPeg)
    largeSqPegAdapter = SquarePegAdapter(largeSqPeg)

    if hole.fits(smallSqPegAdapter):
        print('Square peg w2 fits round hole r5.')

    if not hole.fits(largeSqPegAdapter):
        print('Square peg w20 does not fit into round hole r5.')


if __name__ == '__main__':
    main()
