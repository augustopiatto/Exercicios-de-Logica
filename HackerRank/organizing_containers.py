def organizing_containers(containers):
    balls = sorted([sum((c[i] for c in containers))
                   for i in range(len(containers[0]))])
    boxes = sorted([sum(c) for c in containers])
    return 'Possible' if balls == boxes else 'Impossible'


def test_organizing_containers_1():
    result = organizing_containers([[0, 2], [1, 1]])

    assert result == "Impossible"


def test_organizing_containers_2():
    result = organizing_containers([[0, 2, 1], [1, 1, 1], [2, 0, 0]])

    assert result == "Possible"
