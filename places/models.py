from django.db.models import Model, TextField, UniqueConstraint, ForeignKey, DO_NOTHING, \
    ImageField, FloatField, CheckConstraint, Q


class Place(Model):
    """Representa un lugar.

    Representa un lugar físico. Por ejemplo, un edificio o un espacio que los estudiantes usan.

    name:
    Nombre del lugar.

    latitude:
    latitud del punto.

    lognitude:
    longitud del punto.

    contact_info:
    Información para contactar el lugar. Por ejemplo un número de teléfono.

    schedule:
    El horario de apertura del lugar.

    photo:
    Fotografía del lugar.
    """

    name = TextField(unique=True, max_length=500)
    latitude = FloatField(null=True)
    longitude = FloatField(null=True)
    contact = TextField(max_length=1000, null=True)
    schedule = TextField(max_length=1000, null=True)
    photo = ImageField(upload_to="places/", null=True)

    class Meta:
        constraints = [
            CheckConstraint(
                check=(Q(latitude__isnull=False) & Q(longitude__isnull=False)) |
                      (Q(latitude__isnull=True) & Q(longitude__isnull=True)),
                name='place_partial_location_not_allowed'
            )
        ]


class Tag(Model):
    """Etiquetas para lugares.

    Cada lugar puede pertenecer a una o más categorías.

    Ejemplos de categorías:
        - Escuela
        - Biblioteca
        - Parqueo
        - Parada de bus

    name:
    Nombre de la etiqueta.
    """
    name = TextField(max_length=500, unique=True)


class PlaceTagged(Model):
    """Lugares con sus etiquetas específicas.

    A nivel de base de datos, representa una tabla intermedia.
    """
    tag = ForeignKey(Tag, DO_NOTHING)
    place = ForeignKey(Place, DO_NOTHING)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['place', 'tag'],
                name="placetagged_place_tag_key"
            )
        ]
