def migratory_birds(arr):
    bird_count = {}
    for bird_id in arr:
        if bird_count.get(bird_id):
            bird_count[bird_id] += 1
        else:
            bird_count[bird_id] = 1

    most_sighted = {"id": 0, "sights": 0}
    for bird_key in bird_count.keys():
        if bird_count[bird_key] > most_sighted["sights"] or (bird_key < most_sighted["id"] and bird_count[bird_key] == most_sighted["sights"]):
            most_sighted["id"] = bird_key
            most_sighted["sights"] = bird_count[bird_key]

    return most_sighted["id"]


def test_migratory_birds():
    inputs = [5, 4, 4, 4, 3, 3, 3, 2, 1]

    result = migratory_birds(inputs)

    assert result == 3
