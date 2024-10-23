"""Calificacion"""

from homework import pregunta_09 as pregunta


def test_09():
    """Test 09"""
    assert pregunta.pregunta_09() == {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
