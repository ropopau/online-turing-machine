from pydantic import BaseModel
from typing import List

class Transition(BaseModel):
    current_state: str  
    read_symbol: str
    next_state: str
    write_symbol: str
    direction: str

class MachineModel(BaseModel):
    name: str
    tape_count: int
    init: Transition
    accept: Transition
    transitions: List[Transition]