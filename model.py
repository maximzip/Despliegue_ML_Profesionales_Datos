# Funciones predecir(), cargar_modelo(), normalizar_country()


PAISES_CONOCIDOS = {'Australia', 'Brazil', 'Canada', 'France', 'Germany', 'India',
                    'Italy', 'Netherlands', 'Otros', 'Poland', 'Spain', 'Ukraine',
                    'United Kingdom of Great Britain and Northern Ireland',
                    'United States of America'}
# El resto de paises va en otros 

def normalizar_country(country):
    return country if country in PAISES_CONOCIDOS else 'Otros'


