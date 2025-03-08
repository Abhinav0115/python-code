from typing import List, Tuple, Dict, Any, Union


number: List[int] = [1, 2, 3, 4, 5]

person: Tuple[str, int, float] = ('John', 25, 5.5)

scores: Dict[str, int] = {'John': 90, 'Alice': 85, 'Bob': 80}

identifier: Union[int, str] = "5D1EU" or 12345

def greeting(name: str) -> str:
    return "Hello, " + name



