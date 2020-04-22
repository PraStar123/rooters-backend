from django.db.models import TextChoices


class BUS_PERMIT_TYPE(TextChoices):
    ALL_INDIA = 'ALL'
    CONTRACT = 'CON'


class BUS_MAKE_TYPE(TextChoices):
    VOLVO = 'VOLV'
    SCANIA = 'SCAN'
    MERCEDEZ_BENZ = 'MBEN'
    BHARAT_BENZ = 'BBEN'
    ASHOK_LEYLAND = 'ALEY'
    TATA_MOTORS = 'TATA'
    VEERA = 'VEER'


class BUS_LAYER_TYPE(TextChoices):
    SINGLE = 'SIN'
    DOUBLE = 'DOU'


class BUS_SEAT_STRUCTURE_TYPE(TextChoices):
    TWO_PLUS_TWO = '2+2'
    TWO_PLUS_ONE = '2+1'


class BUS_SEAT_TYPE(TextChoices):
    SEATER = "Seater"
    SEMI_SLEEPER = "Semi-Sleeper"
    SLEEPER = "Sleeper"
    SEATER_SLEEPER = "Seater-Sleeper"
    SLEEPER_SEMI_SLEEPER = "Semi-Sleeper + Sleeper"


class BUS_CLIMATE_TYPE(TextChoices):
    AIR_CONDITIONED = 'A/C'
    NON_AIR_CONDITIONED = 'NAC'


class SEAT_BOOKING_STATUS(TextChoices):
    BOOKED = 'BKD'
    BLOCKED = 'BLK'
    OPEN = 'OPN'


class SPECIAL_TYPE(TextChoices):
    LADIES = 'LAD'
    HANDICAPPED = 'HAN'


class WINDOW_TYPE(TextChoices):
    WINDOW = 'WIN'
    AISLE = 'AIL'