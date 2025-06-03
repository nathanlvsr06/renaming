class Prefix:
    def __init__(self, surname: str, name: str, number: int, date: str, event: str) -> None:
        ''' Initialisation '''
        self._prefix = f'{date} {event}_{surname}_{name}-{number}'
    
    def __str__(self) -> str:
        ''' Représentation informelle'''
        return self._prefix
    
    def __repr__(self) -> str:
        ''' Représentation formelle '''
        return f"Prefix<{self._prefix}>"