# Spec-Driven UI Experiment

## Date

2026-06-07

## Feature

Repair Order Creation

## Goal

The goal of this experiment was to generate a frontend interface using a strict design contract defined in DESIGN.md.

## Design Contract Used

The UI was required to follow these constraints:

- Use Streamlit
- Use a simple form-based layout
- Use clear labels
- Use one primary action button
- Display validation errors clearly
- Connect the UI to the existing RepairOrderFactory backend module

## Prompt Used

Create a Streamlit frontend for the Repair Order Creation feature.

Use the DESIGN.md file as the design contract.

The UI must include:
- Customer ID input
- Vehicle ID input
- Problem description input
- Estimated price input
- Create Repair Order button

The button must call the existing backend logic:

modules/repair_order/repair_order.py

Use:

RepairOrderFactory.create_repair_order()

Do not duplicate business logic in the UI. The UI should only collect input, call the backend module, and display the result.

## Result

The generated UI followed the design contract and used Streamlit as required.

The interface successfully connected to the backend repair order module. When the form was submitted, the UI called RepairOrderFactory.create_repair_order() and displayed either a success message or validation error.

## Evaluation

The AI followed the design constraints reasonably well. It did not create unnecessary custom CSS or generic dashboard elements.

The connection between UI and backend required one clear prompt that explicitly mentioned the existing module path and factory method.

## Accessibility and Structure

The generated UI used labeled input fields and clear feedback messages.

The structure was simple and understandable.

## Conclusion

Spec-Driven Development helped prevent vague UI generation. The DESIGN.md file worked as a useful constraint for the AI assistant and helped keep the frontend aligned with the existing backend architecture.