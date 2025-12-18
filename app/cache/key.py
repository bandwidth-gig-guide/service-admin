class RECORD:
    ARTIST = "artist"
    EVENT = "event"
    VENUE = "venue"



class ARTIST:
    DETAILED = f"{RECORD.ARTIST}:detailed"
    BRIEF = f"{RECORD.ARTIST}:brief"
    RECOMMENDED = f"{RECORD.ARTIST}:recommended"
    IDS = f"{RECORD.ARTIST}:ids"

    ADMIN_UNRESEARCHED = f"{RECORD.ARTIST}:unresearched"
    ADMIN_DETAILED = f"admin:{RECORD.ARTIST}:detailed"
    ADMIN_ID_AND_TITLE = f"admin:{RECORD.ARTIST}:id_and_title"
    ADMIN_IDS = f"admin:{RECORD.ARTIST}:ids"


class EVENT:
    DETAILED = f"{RECORD.EVENT}:detailed"
    BRIEF = f"{RECORD.EVENT}:brief"
    RECOMMENDED = f"{RECORD.EVENT}:recommended"
    IDS = f"{RECORD.EVENT}:ids"
    IDS_BY_DATE = f"{RECORD.EVENT}:ids_by_date"

    ADMIN_DETAILED = f"admin:{RECORD.EVENT}:detailed"
    ADMIN_IDS = f"admin:{RECORD.EVENT}:ids"


class VENUE:
    DETAILED = f"{RECORD.VENUE}:detailed"
    BRIEF = f"{RECORD.VENUE}:brief"
    RECOMMENDED = f"{RECORD.VENUE}:recommended"
    IDS = f"{RECORD.VENUE}:ids"
    CITIES = f"{RECORD.VENUE}:cities"

    ADMIN_DETAILED = f"admin:{RECORD.VENUE}:detailed"
    ADMIN_ID_AND_TITLE = f"admin:{RECORD.VENUE}:id_and_title"
    ADMIN_IDS = f"admin:{RECORD.VENUE}:ids"




KEYS_INDIVIDUAL = {
    "artist": [ARTIST.DETAILED, ARTIST.BRIEF, ARTIST.RECOMMENDED],
    "venue": [VENUE.DETAILED, VENUE.BRIEF, VENUE.RECOMMENDED],
    "event": [EVENT.DETAILED, EVENT.IDS_BY_DATE, EVENT.RECOMMENDED],
}

KEYS_UNIVERSAL = {
    "artist": [ARTIST.ADMIN_ID_AND_TITLE, ARTIST.ADMIN_UNRESEARCHED],
    "venue": [VENUE.ADMIN_ID_AND_TITLE],
    "event": [EVENT.IDS_BY_DATE],
}

KEYS_UNIVERSAL_FILTERABLE = {
    "artist": [ARTIST.IDS, VENUE.ADMIN_IDS],
    "venue": [VENUE.IDS, VENUE.ADMIN_IDS],
    "event": [EVENT.IDS, EVENT.ADMIN_IDS],
}