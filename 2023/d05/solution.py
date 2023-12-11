from typing import List, Dict, Tuple, TypeVar, Iterator

T = TypeVar('T')


def process_mapping(lines: List[str]) -> List[Tuple[int, int, int]]:
    mapping_rules: List[Tuple[int, int, int]] = []
    for line in lines:
        if line:
            dest_start, src_start, length = map(int, line.split())
            mapping_rules.append((dest_start, src_start, length))
    return mapping_rules


def build_numbers(sequence: str) -> List[int]:
    return [int(num) for num in sequence.split() if num.isnumeric()]


def pairs(l: List[T]) -> Iterator[Tuple[T, T]]:
    it = iter(l)
    return zip(it, it)

seeds: List[int] = []

with open("input.txt", "r") as f:
    mappings: Dict[str, List[Tuple[int, int, int]]] = {}
    current_mapping: List[str] = []
    current_mapping_name: str = ""
    for line in f:
        if line.startswith("seeds"):
            seeds = build_numbers(line)
        else:
            if ":" in line:
                if current_mapping and current_mapping_name:
                    mappings[current_mapping_name] = process_mapping(current_mapping)
                current_mapping_name = line.split(":")[0].strip()
                current_mapping = []
            else:
                current_mapping.append(line.strip())

    # process last mapping
    if current_mapping_name:
        mappings[current_mapping_name] = process_mapping(current_mapping)


final_locations: Dict[int, int] = {}

for seed in seeds:
    current_number = seed
    for mapping_name in [
        "seed-to-soil map",
        "soil-to-fertilizer map",
        "fertilizer-to-water map",
        "water-to-light map",
        "light-to-temperature map",
        "temperature-to-humidity map",
        "humidity-to-location map",
    ]:
        mapping_rules = mappings[mapping_name]
        for dest_start, src_start, length in mapping_rules:
            if src_start <= current_number < src_start + length:
                current_number = current_number + dest_start - src_start
                break
    final_locations[seed] = current_number

lowest_location = min(final_locations.values())
print(lowest_location)

seed_ranges = [(start, start + length) for start, length in pairs(seeds)]

for mapping_name in [
    "seed-to-soil map",
    "soil-to-fertilizer map",
    "fertilizer-to-water map",
    "water-to-light map",
    "light-to-temperature map",
    "temperature-to-humidity map",
    "humidity-to-location map",
]:
    mapping_rules = mappings[mapping_name]
    new_seed_ranges = []

    for seed_range in seed_ranges:
        for dest_start, src_start, length in mapping_rules:
            src_end = src_start + length
            dest_end = dest_start + length
            intersect_start = max(seed_range[0], src_start)
            intersect_end = min(seed_range[1], src_end)

            if intersect_start < intersect_end:
                new_seed_ranges.append((intersect_start  + dest_start - src_start, intersect_end + dest_end - src_end))
    seed_ranges = new_seed_ranges

actual_lowest_location = min(start for start, _ in seed_ranges)
print(actual_lowest_location)

