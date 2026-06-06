# Repair Order Creation Flow

```mermaid
flowchart TD

A[Start] --> B[Service Manager Opens Repair Order Form]
B --> C[Select Customer]
C --> D[Select Vehicle]
D --> E[Enter Problem Description and Estimated Price]

E --> F[Send Data to RepairOrderFactory]

F --> G{Input Valid?}

G -->|No| H[Return Validation Error]
H --> Z[End]

G -->|Yes| I[Create RepairOrder Object]

I --> J[Set Default Status = New]
J --> K[Return RepairOrder Object]

K --> L[Save Repair Order in Database]
L --> M[Display Success Message]

M --> Z[End]