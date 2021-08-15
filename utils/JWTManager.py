import datetime
from typing import Tuple
import jwt
from utils.ConfigReader import ConfigReader

class JWTManager:

    _seed: str

    def __init__(self, algorithm='HS256') -> None:
        config_reader: ConfigReader = ConfigReader.create()
        config = config_reader.get_dict_by_section('JWT')
        self._seed = config['seed']
        self._algorithm = algorithm


    def encode(self, data: Tuple) -> str:
        data['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=43200)
        return jwt.encode(data, self._seed, algorithm=self._algorithm)


    def decode(self, token: str):
        return jwt.decode(token, self._seed,
                        algorithms=[self._algorithm])
