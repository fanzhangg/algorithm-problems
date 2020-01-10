def move_tower(height: int, from_pole: str, to_pole: str, with_pole: str):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, to_pole, from_pole)

def move_disk(from_pole: str, to_pole: str):
    print("moving disk from ", from_pole, "to", to_pole)

move_tower(4, "A", "B", "C")
