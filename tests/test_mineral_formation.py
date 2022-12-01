from src.mineral_formation import mineral_formation


def test_mineral_formation1():
    assert mineral_formation([[0, 1, 0, 1],
                              [0, 1, 0, 1],
                              [0, 0, 0, 1],
                              [0, 0, 0, 0]
                              ]) == "stalactites"


def test_mineral_formation2():
    assert mineral_formation([[0, 0, 0, 0],
                              [0, 1, 0, 1],
                              [0, 0, 0, 1],
                              [0, 0, 1, 1]
                              ]) == "stalagmites"


def test_mineral_formation3():
    assert mineral_formation([[1, 0, 0, 0],
                              [0, 1, 0, 1],
                              [0, 0, 0, 1],
                              [0, 0, 1, 1]
                              ]) == "both"

