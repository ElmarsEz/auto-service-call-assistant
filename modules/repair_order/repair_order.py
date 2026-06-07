from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class RepairOrder:
    customer_id: int
    vehicle_id: int
    brand: str
    model: str
    engine: str
    problem_category: str
    problem_description: str
    status: str
    created_date: str
    estimated_price: Optional[float] = None


class RepairOrderFactory:
    """
    Factory responsible for creating valid repair order objects.
    """

    DEFAULT_STATUS = "New"

    @staticmethod
    def create_repair_order(
        customer_id: int,
        vehicle_id: int,
        brand: str,
        model: str,
        engine: str,
        problem_category: str,
        problem_description: str,
        estimated_price: Optional[float] = None
    ) -> RepairOrder:
        if customer_id <= 0:
            raise ValueError("Customer ID must be valid.")

        if vehicle_id <= 0:
            raise ValueError("Vehicle ID must be valid.")

        if not brand or not brand.strip():
            raise ValueError("Vehicle brand cannot be empty.")

        if not model or not model.strip():
            raise ValueError("Vehicle model cannot be empty.")

        if not engine or not engine.strip():
            raise ValueError("Engine cannot be empty.")

        if not problem_category or not problem_category.strip():
            raise ValueError("Problem category cannot be empty.")

        if not problem_description or not problem_description.strip():
            raise ValueError("Problem description cannot be empty.")

        if estimated_price is not None and estimated_price < 0:
            raise ValueError("Estimated price cannot be negative.")

        return RepairOrder(
            customer_id=customer_id,
            vehicle_id=vehicle_id,
            brand=brand.strip(),
            model=model.strip(),
            engine=engine.strip(),
            problem_category=problem_category.strip(),
            problem_description=problem_description.strip(),
            status=RepairOrderFactory.DEFAULT_STATUS,
            created_date=str(date.today()),
            estimated_price=estimated_price
        )