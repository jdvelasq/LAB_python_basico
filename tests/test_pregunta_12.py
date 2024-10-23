"""Calificacion"""

from homework import pregunta_12 as pregunta


def test_12():
    """Test 12"""
    assert pregunta.pregunta_12() == {
        "A": 177,
        "B": 187,
        "C": 114,
        "D": 136,
        "E": 324,
    }
