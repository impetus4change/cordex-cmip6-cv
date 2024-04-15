import json
import sys

from cordex_cv import update_table

table = "CORDEX-CMIP6_institution_id.json"
table_name = "institution_id"


def update_institution_id(entry):
    return update_table(entry, table, table_name, style="flat")


def get_entries(content):
    return json.loads(content)


if __name__ == "__main__":
    content = sys.argv[1]
    # content = '{"institution_id": "INSTITUTE", "institution": "My institute"}'
    entry = get_entries(content)
    new_id = update_institution_id(entry)
    print(new_id)
