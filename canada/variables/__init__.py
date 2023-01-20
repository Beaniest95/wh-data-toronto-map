from dataclasses import dataclass
from os import read

from variables.google import GoogleMapVariables

@dataclass
class ServerVariables:
    google: GoogleMapVariables

    @classmethod
    def get(cls) -> 'ServerVariables':
        return cls(
            google=GoogleMapVariables.get()
        )

server_variables = ServerVariables.get()
