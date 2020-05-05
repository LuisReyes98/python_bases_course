class CasillaDeVotacion:

    def __init__(self, id, pais):
        self._id = id  # ID
        self._pais = pais  # ARRAY de STRINGS
        self._region = None  # STRING

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no es valida en el pais')


casilla = CasillaDeVotacion(123, ['valencia', 'caracas'])
print(casilla.region)
casilla.region = 'caracas'
print(casilla.region)
