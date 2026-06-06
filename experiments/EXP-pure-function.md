# Pure Function Experiment

## Date

2026-06-05

## Feature

Repair Order Creation

## Prompt Used

Feature: Repair Order Creation

User Story:

As a service manager, I want to create a repair order for a vehicle, so that I can track repair work and customer requests.

Acceptance Criteria:

Given a registered customer and a registered vehicle

When the service manager enters a problem description and creates a repair order

Then a new repair order should be created with status "New"

Given a registered customer and a registered vehicle

When the service manager attempts to create a repair order without a problem description

Then the system should reject the request and display a validation error

Given a vehicle does not exist in the system

When the service manager attempts to create a repair order

Then the system should prevent creation of the repair order

Mermaid Flow:
(Insert Mermaid diagram)

Constraint:
Write the logic as a Pure Function. The function must have no side effects and return a predictable output.

---

## Result

The AI successfully generated a pure function on the first attempt.

The function validated input data and returned either a repair order object or a validation error.

No database operations or side effects were included.

---

## Reflection

The BDD requirements and Mermaid diagram provided sufficient context for the AI.

No major changes were required to obtain a correct implementation.
