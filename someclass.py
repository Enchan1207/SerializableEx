#
#
#
import uuid
from typing import Dict, Optional, Any
from src.serializable import Serializable

class SomeClass(Serializable):

    def __init__(self, name: str, datas: Optional[Dict[str, float]] = None) -> None:
        self.identifier = uuid.uuid4().hex
        self.name = name
        self.datas = datas or {}
    
    def add_data(self, key: str, value: str) -> None:
        self.datas[key] = value

    def __str__(self) -> str:
        return f"SomeClass object (id: {self.identifier} name: {self.name} datas: {self.datas})"
    
    def serialized(self) -> Dict[str, Any]:
        serialized_dict = {
            'id': self.identifier,
            'name': self.name,
            'datas': self.datas
        }
        return serialized_dict

    @staticmethod
    def deserialized(serialized: Dict[str, Any]) -> Optional[Serializable]:
        identifier, name, datas = tuple([serialized.get(key) for key in ['id', 'name', 'datas']])
        
        if None in [identifier, name, datas]:
            return None

        result = SomeClass(name, datas)        
        result.identifier = identifier

        return result
