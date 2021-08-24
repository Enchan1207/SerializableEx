#
#
#
import uuid
from typing import Dict, Optional, Any
from serializable import Serializable

class SomeClass(Serializable):

    def __init__(self, name: str, datas: Dict[str, float] = {}) -> None:
        self.id = uuid.uuid4().hex
        self.name = name
        self.datas = datas
    
    def add_data(self, key: str, value: str) -> None:
        self.datas[key] = value

    def __str__(self) -> str:
        return f"SomeClass object (id: {self.id} name: {self.name} datas: {self.datas})"
    
    def serialized(self) -> Dict[str, Any]:
        serialized_dict = {
            'id': self.id,
            'name': self.name,
            'datas': self.datas
        }
        return serialized_dict

    @staticmethod
    def deserialized(serialized: Dict[str, Any]) -> Optional[Serializable]:
        id, name, datas = tuple([serialized.get(key) for key in ['id', 'name', 'datas']])
        
        if None in [id, name, datas]:
            return None

        result = SomeClass(name, datas)        
        result.id = id

        return result
