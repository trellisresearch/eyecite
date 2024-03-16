import pytest

from eyecite import get_citations
from tests.assets.bluebook_citations import (
    bluebook_1,
    bluebook_2,
    bluebook_3,
    bluebook_4,
)


@pytest.mark.parametrize(
    ["input_text", "count"],
    [
        (bluebook_1, 3),
        (bluebook_2, 4),
        (bluebook_3, 2),
        (bluebook_4, 5),
    ],
)
def test_bluebook_count(input_text: str, count: int):
    cits = get_citations(input_text)

    for c in cits:
        print(c)
    assert len(cits) == count