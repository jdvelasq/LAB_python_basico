"""Calificacion"""

from homework import pregunta_02 as pregunta


def test_02():
    """Test 02"""
    assert pregunta.pregunta_02() == [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
