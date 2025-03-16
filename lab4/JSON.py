#JSON — это синтаксис для хранения и обмена данными.
"""
json.loads() JSON жолын Python объектісіне айналдырады.
json.dumps()  Python объектісін JSON жолына айналдырады.
json.dump() JSON-ды файлға жазады.
json.load()  JSON-ды файлдан оқиды.
indent және sort_keys=True параметрлері JSON-ды әдемі форматтауға мүмкіндік береді.
    """
import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

interfaces = data.get("imdata", [])

print("Interface Status")
print("=" * 100)
print(f"{'DN':<50}{'Description':<20}{'Speed':<10}{'MTU':<7}")
print("-" * 100)

for item in interfaces:
    attributes = item.get("l1PhysIf", {}).get("attributes", {})
    dn = attributes.get("dn", "N/A")
    description = attributes.get("descr", "N/A")
    speed = attributes.get("speed", "N/A")
    mtu = attributes.get("mtu", "N/A")
    print(f"{dn:<50}{description:<20}{speed:<10}{mtu:<6}")

import json

data = {
    "name": "Жарас",
    "age": 22,
    "city": "Алматы",
    "languages": ["Python", "C++", "JavaScript"]
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print()