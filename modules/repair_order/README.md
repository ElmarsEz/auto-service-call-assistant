# Repair Order Module

## Selected Design Pattern

This module uses the **Factory Method** design pattern.

## Why Factory Method?

Repair order creation requires validation and consistent object creation.  
Instead of creating repair orders directly in different parts of the system, the `RepairOrderFactory` centralizes this logic.

This helps to:

- keep creation logic in one place
- avoid duplicated validation
- ensure every repair order starts with the correct default status
- make the module easier to extend in the future

## Module Responsibility

The module is responsible for creating valid repair order objects.

It validates:

- customer ID
- vehicle ID
- problem description
- estimated price

## Interaction With Other Components

This module will interact with:

- Customer management module
- Vehicle management module
- Database layer
- Repair order UI form

The UI or service layer should call `RepairOrderFactory.create_repair_order()` when a new repair order needs to be created.

## Future Extension

In future versions, the factory can be extended to create different types of repair orders, such as:

- diagnostic order
- maintenance order
- emergency repair order