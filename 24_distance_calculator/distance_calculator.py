from dataclasses import dataclass

from geopy.distance import geodesic
from geopy.geocoders import Nominatim


@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinate(self) -> tuple[float, float]:
        return self.latitude, self.longitude


def get_coordinates(address: str) -> Coordinates | None:
    """Geocode the given address."""

    geolocator = Nominatim(user_agent="distance_calculator")
    location = geolocator.geocode(address)

    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)  # type: ignore
    return None


def get_distance_km(home: str, target: str) -> float | None:
    """Convert two human readable address to coordinates then returns the distance between them."""

    home_coordinate, target_coordinate = get_coordinates(home), get_coordinates(target)

    if home_coordinate and target_coordinate:
        distance = geodesic(
            home_coordinate.coordinate(), target_coordinate.coordinate()
        )
        return distance.kilometers
    return None


def main() -> None:
    home_adddress: str = "Helsinkigade 10, Copenhagen 2150, Denmark"
    print(f"Home address: {home_adddress}")

    target_address: str = input("Enter an address: ")
    print("Calculating...")

    distance = get_distance_km(home_adddress, target_address)
    if distance is None:
        raise ValueError("Invalid target address, distance can't be calculated.")

    print(f"{home_adddress} -> {target_address}")
    print(f"{distance:,.2f} kilometer{'s' if distance > 1 else ''}")


if __name__ == "__main__":
    main()
