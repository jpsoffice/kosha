import csv
import datetime
import os
import re

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from places import Places

from kosha.people.models import Person, Occupation, Guru, GuruRole
from kosha.regions.models import Country, Nationality, Language
from kosha.organizations.models import Zone


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("file", type=str)

    def handle(self, *args, **options):
        import_file(options["file"])


field_col_map = {
    "initiated_name": 0,
    "name": 1,
    "reference_number": 2,
    "care_level": 3,
    "dob": 4,
    "dob_type": 97,
    "__age": 5,
    "gender": 6,
    "first_initiation_guru": 7,
    "second_initiation_guru": 9,
    "locality": 10,
    "state": 11,
    "country": 12,
    "district": 13,
    "address_line_1": 14,
    "zipcode": 15,
    "phone": 16,
    "mobile": 17,
    "email": 18,
    "first_initiation_date": 19,
    "first_initiation_place": 20,
    "first_initiation_recommendation": 21,
    "second_initiation_date": 22,
    "second_initiation_place": 23,
    "second_initiation_recommendation": 24,
    "occupation": 25,
    "relation_with_gm": 35,
    "permanent_address_line_1": 36,
    "permanent_locality": 37,
    "permanent_state": 38,
    "permanent_zipcode": 39,
    "permanent_country": 40,
    "zone": 41,
    "marital_status": 42,
    "nationality": 47,
    "language": 56,
    "spouse": 85,
    "children": 84,
    "intensive_care": 92,
    "meetings_0_date": 100,
    "created_at": 61,
    "siksha_gurus": [(75, 76), (77, 78), (79, 80)],
    "kc_start_date": 51,
    "is_following_four_regs": 52,
    "following_four_regs_sincs": 53,
    "chanting_rounds_number": 54,
    "chanting_sixteen_rounds_since": 55,
}

relation_with_gm_rev_map = dict(
    (
        ("Spiritual son", "SS"),
        ("Spiritual daughter", "SD"),
        ("Spiritual nephew", "SNE"),
        ("Spiritual niece", "SNI"),
        ("Spiritual son bhakta", "SSB"),
        ("Spiritual daughter bhaktin", "SDB"),
        ("Siksha disciple", "SKD"),
        ("Bhakta", "BTA"),
        ("Bhaktin", "BTI"),
        ("Well wisher", "WW"),
    )
)

marital_status_rev_map = dict(
    (
        ("Single", "SGL"),
        ("Engaged", "ENG"),
        ("Seeking", "SKG"),
        ("Married", "MRD"),
        ("Separated", "SEP"),
        ("Divorced", "DIV"),
        ("Widow", "WID"),
    )
)


def import_file(file_path):
    with open(os.path.join(settings.ROOT_DIR, file_path)) as f:
        reader = csv.reader(f)

        count = 0
        for row in reader:
            count += 1
            if count == 1:
                continue
            try:
                kwargs = {
                    "initiated_name": row[field_col_map["initiated_name"]],
                    "name": row[field_col_map["name"]],
                    "reference_number": row[field_col_map["reference_number"]],
                    "care_level": parse_care_level(row[field_col_map["care_level"]]),
                    "relation_with_gm": parse_relation_with_gm(
                        row[field_col_map["relation_with_gm"]]
                    ),
                    "dob": parse_date(row[field_col_map["dob"]]),
                    "dob_type": parse_dob_type(row[field_col_map["dob_type"]]),
                    "gender": row[field_col_map["gender"]],
                    "first_initiation_guru": parse_initiation_guru(
                        row[field_col_map["first_initiation_guru"]]
                    ),
                    "first_initiation_date": parse_date(
                        row[field_col_map["first_initiation_date"]]
                    ),
                    "first_initiation_place": parse_place(
                        row[field_col_map["first_initiation_place"]]
                    ),
                    "second_initiation_guru": parse_initiation_guru(
                        row[field_col_map["second_initiation_guru"]]
                    ),
                    "second_initiation_date": parse_date(
                        row[field_col_map["second_initiation_date"]]
                    ),
                    "second_initiation_place": parse_place(
                        row[field_col_map["second_initiation_place"]]
                    ),
                    "locality": row[field_col_map["locality"]],
                    "district": row[field_col_map["district"]],
                    "state": row[field_col_map["state"]],
                    "country": parse_country(row[field_col_map["country"]]),
                    "zipcode": row[field_col_map["zipcode"]],
                    "zone": parse_zone(row[field_col_map["zone"]]),
                    "nationality": parse_nationality(row[field_col_map["nationality"]]),
                    "language": parse_language(row[field_col_map["language"]]),
                    "marital_status": parse_marital_status(
                        row[field_col_map["marital_status"]]
                    ),
                }
                # print(kwargs)
                try:
                    person = Person.objects.get(
                        reference_number=kwargs["reference_number"]
                    )
                    for k, v in kwargs.items():
                        setattr(person, k, v)
                except Person.DoesNotExist:
                    person = Person(**kwargs)
                person.save()
            except Exception as e:
                print(e)
                print("BAD ROW: ", row)


def parse_care_level(s):
    s = s.strip().upper()
    if not s:
        return
    if s == "D":
        return "D1"
    elif s == "X":
        return "EX-D"
    else:
        return s


def parse_relation_with_gm(s):
    s = s.strip().capitalize()
    return relation_with_gm_rev_map.get(s, "")


def parse_date(s):
    m = re.match(r"(?P<day>\d{2})-(?P<month>\w{3}).*?-(?P<year>\d{2})", s)
    if m:
        day, month, year = m.groups()
        if int(year) > 19:
            year = "19" + year
        else:
            year = "20" + year
        return datetime.datetime.strptime(
            "{}-{}-{}".format(day, month, year), "%d-%b-%Y"
        ).date()


def parse_dob_type(s):
    if s.startswith("Actual") or s.startswith("Calculated"):
        return s[0]


def parse_initiation_guru(s):
    if not s.strip():
        return
    try:
        guru = Guru.objects.get(code=s)
    except Guru.DoesNotExist:
        guru = Guru.objects.create(code=s, name=s)
        diksha_role, _ = GuruRole.objects.get_or_create(name="diksha")
        siksha_role, _ = GuruRole.objects.get_or_create(name="siksha")
        guru.roles.add(diksha_role)
        guru.roles.add(siksha_role)
        guru.save()
    return guru


def parse_place(s):
    return Places(s, 0, 0)


def parse_country(s):
    country = Country.objects.filter(name__iexact=s).first()
    return country


def parse_zone(s):
    s = s.strip().title()
    if not s:
        return
    zone, _ = Zone.objects.get_or_create(name=s)
    return zone


def parse_nationality(s):
    s = s.strip()
    nationality = None
    try:
        nationality = Nationality.objects.get(nationality__iexact=s)
    except Nationality.DoesNotExist:
        try:
            nationality = Nationality.objects.get(name__iexact=s)
        except Nationality.DoesNotExist:
            pass
    return nationality


def parse_language(s):
    s = s.strip()
    try:
        lang = Language.objects.get(name__iexact=s)
        return lang
    except Language.DoesNotExist:
        pass


def parse_marital_status(s):
    s = s.strip().capitalize()
    if not s:
        return ""
    return marital_status_rev_map.get(s, "")
