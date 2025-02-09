def main():
    spacecraft = {"name": "Voyager 1", "distance": "163"}
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
======================REPORT======================

Name of Spacecraft : {spacecraft["name"]}
Distance of Spacecraft : {spacecraft["distance"]}

==================================================
"""
main()  