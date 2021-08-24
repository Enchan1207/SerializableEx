#
# テスト用の適当なSerializableクラス
#
from __future__ import annotations
from typing import Any, Dict, Optional
import serializable

class SomeClass(serializable.Serializable):

    def __init__(self, name: str, datas: Optional[Dict[str, Any]] = None) -> None:
        self.name: str = name
        self.datas: Dict[str, Any] = datas or {}

    def serialized(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'datas': self.datas
        }

    @staticmethod
    def deserialized(serialized: Dict[str, Any]) -> Optional[SomeClass]:
        name, datas = tuple([serialized.get(key) for key in ['name', 'datas']])

        if None in [name, datas]:
            return None

        result = SomeClass(name, datas)
        return result


    def __str__(self) -> str:
        return f"TestClass( name: {self.name}  datas: {self.datas} )"

