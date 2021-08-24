#
# Serializableオブジェクトをjson形式でシリアライズする
#
import json
from typing import Any, Dict, Union
from serializable import Serializable

class JSONSerializer():

    """
    Serializableなオブジェクトをjson形式に変換するシリアライザ。
    """

    def serialize(self, object: Union[Serializable, Dict[str, Any]]) -> str:

        """
        Serializableオブジェクトまたは辞書オブジェクトをjsonシリアライズします。

        Returns:
            str : 変換結果。

        Raises:
            ValueError: 引数が不正であった場合。
            TypeError: JSONパースに失敗した場合。
        """

        # 型チェック dictでもなくserializableでもなければエラー
        if type(object) is not dict and not issubclass(type(object), Serializable):
            raise ValueError("Invalid argument.")
        
        # Serializableならオブジェクトの辞書表現をもらう
        dict_represented = object
        if issubclass(type(object), Serializable):
            dict_represented = object.serialized()
        
        # 辞書をjsonパース
        result = json.JSONEncoder().encode(dict_represented)
        
        return result

    def deserialize(self, serialized: str) -> Dict[str, Any]:
        """
        jsonシリアライズされたデータを辞書型にデシリアライズします。
        """

        return json.JSONDecoder().decode(serialized)
