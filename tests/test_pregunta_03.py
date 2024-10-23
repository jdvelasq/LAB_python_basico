"""Calificacion"""

from homework import pregunta_03 as pregunta


def test_03():
    """Test 03"""
    assert pregunta.pregunta_03() == [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
