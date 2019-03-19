def setup(file):
    with open(file) as f:
        file = f.read().split('\n')

    coordinates = []
    for point in file:
        coordinates.append(list(map(int, point.split(', '))))

    return coordinates


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def main():
    print("Finding Dangerous Locations...")
    coordinates = setup('coordinates.txt')

    low_x = min([point[0] for point in coordinates])
    high_x = max([point[0] for point in coordinates])
    low_y = min([point[1] for point in coordinates])
    high_y = max([point[1] for point in coordinates])

    reference_dict = {n: coord for n, coord in enumerate(coordinates)}
    plane = {}

    for x in range(low_x, high_x + 1):
        for y in range(low_y, high_y + 1):
            point = [x, y]
            lowest = (0, 1e5, True)
            for n, location in enumerate(coordinates):
                distance = manhattan_distance(location, point)
                if distance < lowest[1]:
                    lowest = (n, distance, True)
                elif distance == lowest[1]:
                    lowest = (lowest[0], lowest[1], False)

            if lowest[2]:
                plane.setdefault(lowest[0], 0)
                plane[lowest[0]] += 1

    for point in reference_dict:
        if reference_dict[point][0] == low_x or reference_dict[point][0] == high_x or reference_dict[point][1] == low_y or reference_dict[point][1] == high_y:
            plane.pop(point)

    print(plane)
    print(reference_dict)
    print(max(plane.values()))

if __name__ == '__main__':
    main()