from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class RepairOrder:
    customer_id: int
    vehicle_id: int
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
        problem_description: str,
        estimated_price: Optional[float] = None
    ) -> RepairOrder:
        if customer_id <= 0:
            raise ValueError("Customer ID must be valid.")

        if vehicle_id <= 0:
            raise ValueError("Vehicle ID must be valid.")

        if not problem_description or not problem_description.strip():
            raise ValueError("Problem description cannot be empty.")

        if estimated_price is not None and estimated_price < 0:
            raise ValueError("Estimated price cannot be negative.")

        return RepairOrder(
            customer_id=customer_id,
            vehicle_id=vehicle_id,
            problem_description=problem_description.strip(),
            status=RepairOrderFactory.DEFAULT_STATUS,
            created_date=str(date.today()),
            estimated_price=estimated_price
        )

order = RepairOrderFactory.create_repair_order(
    customer_id=1,
    vehicle_id=1,
    problem_description="Engine noise",
    estimated_price=250.0
)

print(order)