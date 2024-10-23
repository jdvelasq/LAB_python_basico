"""Calificacion"""

from homework import pregunta_05 as pregunta


def test_05():
    """Test 05"""
    assert pregunta.pregunta_05() == [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
