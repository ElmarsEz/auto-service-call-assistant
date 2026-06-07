import json
import sys
from datetime import date
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

DATA_DIR = PROJECT_ROOT / "data"
DATA_FILE = DATA_DIR / "car_service_data.json"

CAR_DATA = {
    "Audi": {
        "A4": ["1.8", "1.9 TDI", "2.0 TDI"],
        "A6": ["2.0 TDI", "2.7 TDI", "3.0 TDI"]
    },
    "BMW": {
        "320d": ["2.0 Diesel"],
        "330d": ["3.0 Diesel"]
    },
    "Volkswagen": {
        "Golf": ["1.6", "1.9 TDI", "2.0 TDI"],
        "Passat": ["1.9 TDI", "2.0 TDI"]
    },
    "Toyota": {
        "Corolla": ["1.6", "1.8"],
        "Avensis": ["1.8", "2.0"]
    }
}

PROBLEM_CATEGORIES = [
    "Engine",
    "Transmission",
    "Electrical",
    "Body Work",
    "Brakes",
    "Suspension",
    "Cooling System",
    "Exhaust System",
    "Other"
]

ORDER_STATUSES = [
    "New",
    "In Progress",
    "Waiting for Parts",
    "Completed",
    "Cancelled"
]


def load_data():
    DATA_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        return {
            "customers": [],
            "vehicles": [],
            "repair_orders": []
        }

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    DATA_DIR.mkdir(exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def get_next_id(items):
    if not items:
        return 1

    return max(item["id"] for item in items) + 1


def create_repair_order(
    data,
    customer_name,
    customer_phone,
    brand,
    model,
    engine,
    problem_category,
    problem_description,
    estimated_price
):
    if not customer_name.strip():
        raise ValueError("Customer name is required.")

    if not customer_phone.strip():
        raise ValueError("Customer phone is required.")

    if not brand:
        raise ValueError("Vehicle brand is required.")

    if not model:
        raise ValueError("Vehicle model is required.")

    if not engine:
        raise ValueError("Engine is required.")

    if not problem_category:
        raise ValueError("Problem category is required.")

    if not problem_description.strip():
        raise ValueError("Problem description is required.")

    customer_id = get_next_id(data["customers"])
    vehicle_id = get_next_id(data["vehicles"])
    order_id = get_next_id(data["repair_orders"])

    customer = {
        "id": customer_id,
        "name": customer_name.strip(),
        "phone": customer_phone.strip()
    }

    vehicle = {
        "id": vehicle_id,
        "customer_id": customer_id,
        "brand": brand,
        "model": model,
        "engine": engine
    }

    repair_order = {
        "id": order_id,
        "customer_id": customer_id,
        "vehicle_id": vehicle_id,
        "customer_name": customer["name"],
        "customer_phone": customer["phone"],
        "brand": brand,
        "model": model,
        "engine": engine,
        "problem_category": problem_category,
        "problem_description": problem_description.strip(),
        "estimated_price": estimated_price,
        "status": "New",
        "manager_note": "",
        "created_date": str(date.today())
    }

    data["customers"].append(customer)
    data["vehicles"].append(vehicle)
    data["repair_orders"].append(repair_order)

    save_data(data)

    return repair_order


st.set_page_config(
    page_title="Car Service Management System",
    page_icon="🔧",
    layout="centered"
)

st.title("Car Service Management System")
st.write("Create and manage repair orders for car service customers.")

data = load_data()

if "form_version" not in st.session_state:
    st.session_state["form_version"] = 0

if "order_created" in st.session_state:
    st.success("Repair order created successfully.")
    del st.session_state["order_created"]

form_version = st.session_state["form_version"]

tab_create, tab_orders = st.tabs(["Create Repair Order", "Repair Orders"])

with tab_create:
    st.subheader("Customer Information")

    customer_name = st.text_input(
        "Customer Name",
        key=f"customer_name_{form_version}"
    )

    customer_phone = st.text_input(
        "Customer Phone",
        key=f"customer_phone_{form_version}"
    )

    st.subheader("Vehicle Information")

    brand_options = ["Select brand"] + list(CAR_DATA.keys())

    brand = st.selectbox(
        "Brand",
        brand_options,
        key=f"brand_{form_version}"
    )

    if brand != "Select brand":
        model_options = ["Select model"] + list(CAR_DATA[brand].keys())
    else:
        model_options = ["Select model"]

    model = st.selectbox(
        "Model",
        model_options,
        key=f"model_{form_version}"
    )

    if brand != "Select brand" and model != "Select model":
        engine_options = ["Select engine"] + CAR_DATA[brand][model]
    else:
        engine_options = ["Select engine"]

    engine = st.selectbox(
        "Engine",
        engine_options,
        key=f"engine_{form_version}"
    )

    st.subheader("Problem Information")

    problem_category = st.selectbox(
        "Expected Problem Category",
        ["Select problem category"] + PROBLEM_CATEGORIES,
        key=f"problem_category_{form_version}"
    )

    problem_description = st.text_area(
        "Problem Description",
        placeholder="Example: Engine noise after cold start...",
        key=f"problem_description_{form_version}"
    )

    estimated_price = st.number_input(
        "Estimated Price (€)",
        min_value=0.0,
        step=10.0,
        key=f"estimated_price_{form_version}"
    )

    if st.button("Create Repair Order"):
        try:
            if brand == "Select brand":
                raise ValueError("Please select vehicle brand.")

            if model == "Select model":
                raise ValueError("Please select vehicle model.")

            if engine == "Select engine":
                raise ValueError("Please select engine.")

            if problem_category == "Select problem category":
                raise ValueError("Please select problem category.")

            create_repair_order(
                data=data,
                customer_name=customer_name,
                customer_phone=customer_phone,
                brand=brand,
                model=model,
                engine=engine,
                problem_category=problem_category,
                problem_description=problem_description,
                estimated_price=estimated_price
            )

            st.session_state["order_created"] = True
            st.session_state["form_version"] += 1
            st.rerun()

        except ValueError as error:
            st.error(str(error))

with tab_orders:
    st.subheader("Existing Repair Orders")

    if not data["repair_orders"]:
        st.info("No repair orders created yet.")
    else:
        for order in data["repair_orders"]:
            current_status = st.session_state.get(
                f"status_{order['id']}",
                order["status"]
            )
            with st.expander(
                f"Order #{order['id']} - {order['brand']} {order['model']} - {order['status']}"
            ):
                st.write(f"Customer: {order['customer_name']}")
                st.write(f"Phone: {order['customer_phone']}")
                st.write(f"Vehicle: {order['brand']} {order['model']} {order['engine']}")
                st.write(f"Problem Category: {order['problem_category']}")
                st.write(f"Description: {order['problem_description']}")
                st.write(f"Estimated Price: €{order['estimated_price']}")
                st.write(f"Created Date: {order['created_date']}")

                new_status = st.selectbox(
                    "Change Status",
                    ORDER_STATUSES,
                    index=ORDER_STATUSES.index(order["status"]),
                    key=f"status_{order['id']}"
                )

                manager_note = st.text_area(
                    "Manager Note",
                    value=order.get("manager_note", ""),
                    placeholder="Example: Call customer on Tuesday, part arrives Wednesday...",
                    key=f"note_{order['id']}"
                )

                if st.button("Update Order", key=f"update_{order['id']}"):
                    order["status"] = new_status
                    order["manager_note"] = manager_note
                    save_data(data)
                    st.success("Order updated successfully.")
                    st.rerun()