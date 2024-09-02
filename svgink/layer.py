from dataclasses import dataclass
from typing import Optional

from .elements import G

@dataclass
class Layer(G):
    inkscape__groupmode: str = "layer"
    inkscape__label: Optional[str] = None