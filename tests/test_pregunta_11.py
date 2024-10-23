"""Calificacion"""

from homework import pregunta_11 as pregunta


def test_11():
    """Test 11"""
    assert pregunta.pregunta_11() == {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
