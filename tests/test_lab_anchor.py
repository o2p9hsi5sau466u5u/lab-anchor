from src.lab_anchor.core import pack


def test_pack_keeps_first():
    rows = [{"id": "a"}, {"id": "a"}, {"id": "b"}]
    assert pack(rows) == [{"id": "a"}, {"id": "b"}]
