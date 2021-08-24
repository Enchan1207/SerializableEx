#
#
#
from __future__ import annotations
from typing import Any, Dict, Optional


class Serializable():

    """
    そのオブジェクトが「直列化(シリアライズ)」可能であることを示すインタフェース。
    """

    def serialized(self) -> Dict[str, Any]:
        """
        オブジェクトをシリアライズした結果を返します。

        Returns:
            Dict[str, Any] : インスタンスのシリアライズ結果。
        """
        raise NotImplementedError("serialized() -> Dict[str, Any] is not implemented")

    @staticmethod
    def deserialized(serialized: Dict[str, Any]) -> Optional[Serializable]:
        """
        シリアライズされたデータからインスタンスを復元します。
        
        Returns:
            Optional[Serializable] : 変換に失敗した場合。
        """
        raise NotImplementedError("deserialized(str) -> Optional[Serializable] is not implemented")
