# Design System

## Framework Choice

The frontend will be built using Streamlit.

Streamlit is selected because:
- it works well with Python modules
- it is fast for MVP development
- it allows simple form-based interfaces
- it does not require complex frontend setup

## Color Palette

Primary color: #2563EB  
Secondary color: #64748B  
Background color: #F8FAFC  
Card background: #FFFFFF  
Text color: #0F172A  
Error color: #DC2626  
Success color: #16A34A  

## UI Components

- Customer Information Form
- Vehicle Selection Form
- Repair Order List
- Status Management
- Manager Notes

## Typography

- Use clear and readable text
- Main page title should describe the feature
- Section headers should be short and meaningful
- Avoid decorative fonts
- Use consistent capitalization

## Spacing Rules

- Use clear separation between form sections
- Avoid overcrowded layouts
- Keep related fields grouped together
- Use one main action button per form

## Component Rules

- Buttons must have clear labels
- Primary action button must be used only once per form
- Error messages must be visible and understandable
- Success messages must confirm the created repair order
- Forms must not submit empty required fields

## Accessibility Rules

- All input fields must have descriptive labels
- Error messages must explain what went wrong
- The interface must be readable on small screens
- Do not rely only on color to communicate status

## UI Scope

The first UI version will only cover the Repair Order Creation feature.

The UI must connect to the backend module:

modules/repair_order/repair_order.py