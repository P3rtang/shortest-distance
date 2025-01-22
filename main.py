import math
from typing import Self
import random

class Point:
    def __init__(self, index: int) -> None:
        self.index = index
        self.x = random.random() * 100
        self.y = random.random() * 100
        self.z = random.random() * 100

    def __repr__(self) -> str:
        return f"(x={self.x}, y={self.y}, z={self.z})"

    def distance(self, other: Self) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

def generatePoints() -> list[Point]:
    points = []
    for i in range(0, 10):
        points.append(Point(i))

    return points

def generateCircle() -> list[Point]:
    points = []
    for i in range(1, 11):
        point = Point(i)
        point.x = math.cos(2 * math.pi / 10 * i)
        point.y = math.sin(2 * math.pi / 10 * i)
        point.z = 0
        points.append(point)
    return points


def main2(points: list[Point]):
    used = []
    new = points[0]

    for _ in points:
        distance = float('inf')
        current = new

        used.append(current) 

        for next in points:
            d = math.sqrt(pow(next.x - current.x, 2) + pow(next.y - current.y, 2) + pow(next.z - current.z, 2))
            if d < distance and next not in used and next != current:
                distance = d
                new = next
        print(f"{current}, {new}")

def main(points: list[Point]):
    current = points[0]
    seen = [current]

    for _ in points:
        distance = float("inf")

        closest = points[0]

        for next in points:
            if next in seen:
                continue
            d = current.distance(next)
            if d < distance:
                distance = d
                closest = next

        seen.append(closest)
        print(current, closest, distance)
        current = closest

if __name__ == "__main__":
    points = generateCircle()
    main(points)
    main2(points)
