# Created by: Ms.Aye Theingi Thwin

import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# -----------------------------
# 1. Generate Stores
# -----------------------------

regions = [
    "Kuala Lumpur",
    "Selangor",
    "Penang",
    "Johor",
    "Perak"
]

store_sizes = ["Small", "Medium", "Large"]

stores = []

for i in range(1, 51):

    store_id = f"S{i:03d}"

    region = np.random.choice(regions)

    store_size = np.random.choice(
        store_sizes,
        p=[0.3, 0.45, 0.25]
    )

    if store_size == "Small":
        capacity = np.random.randint(1500, 2500)

    elif store_size == "Medium":
        capacity = np.random.randint(2500, 4000)

    else:
        capacity = np.random.randint(4000, 6000)

    stores.append([
        store_id,
        f"Store {store_id}",
        region,
        store_size,
        capacity
    ])

stores = pd.DataFrame(
    stores,
    columns=[
        "store_id",
        "store_name",
        "region",
        "store_size",
        "capacity"
    ]
)

print("Stores created:", len(stores))

# -----------------------------
# 2. Generate Products
# -----------------------------

product_names = [
    "Screwdriver Set",
    "Storage Box",
    "LED Bulb",
    "Extension Cable",
    "Cleaning Brush",
    "Plastic Container",
    "Hammer",
    "Measuring Tape",
    "Kitchen Organizer",
    "Microfiber Cloth",
    "Power Strip",
    "Wall Hook",
    "Door Stopper",
    "Paint Brush",
    "Utility Knife",
    "Cable Tie",
    "Laundry Basket",
    "Food Container",
    "Tool Box",
    "Torch Light",
    "Gloves",
    "Dustpan",
    "Mop Head",
    "Broom",
    "Hanger",
    "Sponge",
    "Shelf Organizer",
    "Water Bottle",
    "Small Fan",
    "Storage Rack"
]

categories = [
    "Hardware",
    "Storage",
    "Electrical",
    "Electrical",
    "Household",
    "Storage",
    "Hardware",
    "Hardware",
    "Kitchen",
    "Household",
    "Electrical",
    "Hardware",
    "Hardware",
    "Hardware",
    "Hardware",
    "Electrical",
    "Household",
    "Kitchen",
    "Hardware",
    "Electrical",
    "Hardware",
    "Household",
    "Household",
    "Household",
    "Household",
    "Household",
    "Storage",
    "Kitchen",
    "Electrical",
    "Storage"
]

products = []

for i in range(30):

    product_id = f"P{i+1:03d}"

    price = round(
        np.random.uniform(5, 50),
        2
    )

    cost = round(
        price * np.random.uniform(0.40, 0.70),
        2
    )

    products.append([
        product_id,
        product_names[i],
        categories[i],
        price,
        cost
    ])

products = pd.DataFrame(
    products,
    columns=[
        "product_id",
        "product_name",
        "category",
        "price",
        "cost"
    ]
)

print("Products created:", len(products))

# -----------------------------
# 3. Generate Sales
# -----------------------------

dates = pd.date_range(
    start="2025-08-01",
    end="2026-07-31",
    freq="D"
)

sales = []

for date in dates:

    # Seasonal factor
    month = date.month

    if month in [11, 12]:
        seasonal_factor = 1.25

    elif month in [3, 4]:
        seasonal_factor = 1.10

    else:
        seasonal_factor = 1.00

    for _, store in stores.iterrows():

        # Store size influences demand
        if store["store_size"] == "Small":
            store_factor = 0.75

        elif store["store_size"] == "Medium":
            store_factor = 1.00

        else:
            store_factor = 1.35

        for _, product in products.iterrows():

            # Base demand
            base_demand = np.random.uniform(5, 40)

            quantity = (
                base_demand
                * store_factor
                * seasonal_factor
                * np.random.uniform(0.7, 1.3)
            )

            quantity = max(
                0,
                int(round(quantity))
            )

            if quantity > 0:

                sales.append([
                    date,
                    store["store_id"],
                    product["product_id"],
                    quantity,
                    product["price"]
                ])

sales = pd.DataFrame(
    sales,
    columns=[
        "sale_date",
        "store_id",
        "product_id",
        "quantity",
        "unit_price"
    ]
)

print("Sales records:", len(sales))

print(sales.head())

print("\nSales shape:")
print(sales.shape)

print("\nMissing values:")
print(sales.isnull().sum())

sales["revenue"] = (sales["quantity"] * sales["unit_price"])
print(sales[
    ["sale_date",
     "store_id",
     "product_id",
     "quantity",
     "unit_price",]
].head()
)

# -----------------------------
# 4. Generate Inventory
# -----------------------------

inventory = []

for _, store in stores.iterrows():

    for _, product in products.iterrows():

        stock_on_hand = np.random.randint(
            20,
            500
        )

        reorder_point = np.random.randint(
            30,
            200
        )

        inventory.append([
            store["store_id"],
            product["product_id"],
            stock_on_hand,
            reorder_point,
            "2026-07-31"
        ])

inventory = pd.DataFrame(
    inventory,
    columns=[
        "store_id",
        "product_id",
        "stock_on_hand",
        "reorder_point",
        "last_updated"
    ]
)

print("Inventory records:", len(inventory))

stores.to_csv(
    "stores.csv",
    index=False
)

products.to_csv(
    "products.csv",
    index=False
)

sales.to_csv(
    "sales.csv",
    index=False
)

inventory.to_csv(
    "inventory.csv",
    index=False
)

print("All datasets saved successfully!")

"""

# Write each data frames to a single Excel file with different sheets
with pd.ExcelWriter('generate.xlsx', engine='openpyxl') as writer:
    stores.to_excel(writer, sheet_name='Stores', index=False)
    products.to_excel(writer, sheet_name='Products', index=False)
    sales.to_excel(writer, sheet_name='Sales', index=False)
    inventory.to_excel(writer, sheet_name='Inventory', index=False) 

print("Excel file created successfully!")



print(stores.shape)
print(products.shape)
print(sales.shape)
print(inventory.shape)

"""
