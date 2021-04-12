travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visit_count, cities):
    log = {
        "country": country,
        "visits": visit_count,
        "cities": cities
    }
    travel_log.append(log)


if __name__ == "__main__":
    for log in travel_log:
        print(log)
    print()

    add_new_country(country='USA', visit_count=1, cities=['San Francisco', 'Las Vegas'])
    for log in travel_log:
        print(log)
    print()

    add_new_country('Canada', 1, ['Vancouver'])
    for log in travel_log:
        print(log)
    print()
