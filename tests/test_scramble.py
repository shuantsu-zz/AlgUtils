import pytest

from main import AlgUtils


@pytest.fixture
def au():
    """au entity with gerenated scramble of 25 moves"""
    au = AlgUtils()
    au.generate_scramble_alg(25)
    return au


def test_scramble_size(au):
    """Check if the scramble has 25 moves"""
    assert len(au.alg.split()) == 25


def test_legal_alg(au):
    '''
    Three subsequent same axis moves or
    two subsequent same face moves are illegal
    '''

    def check_if_same_axis(moves):
        '''Check if three moves belong to same axis'''
        for axis in au.possible_moves.values():
            how_many = 0
            for move in moves:
                if move[0] in axis:
                    how_many += 1
            if how_many == 3:
                return True
        return False

    def check_moves_legality(alg):
        '''Check if a scramble has two subsequent moves of the same axis'''
        legality = True
        for index in range(len(alg.split())):
            moves = alg.split()[index:index + 3]
            faces = [mv[0] for mv in moves]
            is_subsequent_faces = any(i == j for i, j in zip(faces, faces[1:]))
            if check_if_same_axis(moves) or is_subsequent_faces:
                legality = False
        return legality

    assert check_moves_legality(au.alg)
    assert check_moves_legality("R R' U") == False
    assert check_moves_legality("R L' R2") == False


def test_reversed():
    '''Test if the scramble is correctly reversed'''
    au1 = AlgUtils()
    au1.apply_alg("F' U' L' B' U B2 L F' D2 F' D2 F' R2 U2 B U2 R2 B'")
    assert au1.reversed == "B R2 U2 B' U2 R2 F D2 F D2 F L' B2 U' B L U F"
    au2 = AlgUtils()
    au2.apply_alg("R F L U D B R' F' L' U' D' B' R2 F2 L2 U2 D2 B2")
    assert au2.reversed == "B2 D2 U2 L2 F2 R2 B D U L F R B' D' U' L' F' R'"
    au3 = AlgUtils()
    au3.apply_alg("R U R' U'")
    assert au3.reversed == "U R U' R'"


def test_empty_reversed():
    '''
    Test if au.reversed is empty if the alg is not applied or
    scramble is not generated
    '''
    au = AlgUtils()
    assert au.reversed is None
