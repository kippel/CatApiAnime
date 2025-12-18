
from typing import List


def serializes(bar: dict) -> dict:
    """Converteix l'_id de MongoDB a string per JSON."""
    return {**bar, "_id": str(bar["_id"])}


def serializes_delete(bar: dict) -> dict:
    """Converteix l'_id de MongoDB a string per JSON."""
    new_bar = bar.copy()
    new_bar.pop("_id", None)
    return new_bar


async def serializes_list(bar) -> List[dict]:
    return [serializes(foo) async for foo in bar]