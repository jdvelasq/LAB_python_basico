"""Calificacion"""

from homework import pregunta_04 as pregunta


def test_04():
    """Test 04"""
    assert pregunta.pregunta_04() == [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
