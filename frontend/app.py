import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from modules.repair_order.repair_order import RepairOrderFactory


st.set_page_config(
    page_title="Car Service Management System",
    page_icon="🔧",
    layout="centered"
)

st.title("Car Service Management System")
st.subheader("Create Repair Order")

st.write(
    "Use this form to create a new repair order for a registered customer and vehicle."
)

with st.form("repair_order_form"):
    customer_id = st.number_input(
        "Customer ID",
        min_value=1,
        step=1
    )

    vehicle_id = st.number_input(
        "Vehicle ID",
        min_value=1,
        step=1
    )

    problem_description = st.text_area(
        "Problem Description",
        placeholder="Example: Engine noise, oil leak, brake issue..."
    )

    estimated_price = st.number_input(
        "Estimated Price",
        min_value=0.0,
        step=10.0
    )

    submitted = st.form_submit_button("Create Repair Order")

if submitted:
    try:
        repair_order = RepairOrderFactory.create_repair_order(
            customer_id=customer_id,
            vehicle_id=vehicle_id,
            problem_description=problem_description,
            estimated_price=estimated_price
        )

        st.success("Repair order created successfully.")

        st.json({
            "customer_id": repair_order.customer_id,
            "vehicle_id": repair_order.vehicle_id,
            "problem_description": repair_order.problem_description,
            "status": repair_order.status,
            "created_date": repair_order.created_date,
            "estimated_price": repair_order.estimated_price
        })

    except ValueError as error:
        st.error(str(error))