"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.
    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, "r") as file:
        reader = csv.DictReader(file)
        neo_obj_arr = []
        for row in reader:
            row["name"] = row["name"] or None
            row["diameter"] = float(row["diameter"]) if row["diameter"] else None
            row["pha"] = False if row["pha"] in ["", "N"] else True

            neo = NearEarthObject(
                designation=row["pdes"],
                name=row["name"],
                diameter=row["diameter"],
                hazardous=row["pha"]
            )

            neo_obj_arr.append(neo)

    return neo_obj_arr


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    ca_obj_arr = []
    with open(cad_json_path) as f:
        loader = json.load(f)
        ca_arr = [dict(zip(loader["fields"], i)) for i in loader['data']]

        for row in ca_arr:
            ca_info = {
                'designation': row['des'],
                'time': row['cd'],
                'distance': row['dist'],
                'velocity': row['v_rel']
            }

            ca_obj_arr.append(CloseApproach(**ca_info))

        f.close()
    return ca_obj_arr


if __name__ == '__main__':
    neo_obj_arr = load_neos('./data/neos.csv')
