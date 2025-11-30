from pathlib import Path
from typing import Any

FILENAME = "Bekleidung25.csv"
HAS_HEADER = True

def normalize_price(price: str) -> float:
    price = price.replace(",", ".")
    price = price.replace("€", "")
    price = price.replace("\"", "").strip()
    
    return float(price)

def extract_bill_item(bill_item: list[str]) -> dict[str, Any]:
    return {
        "first_name": bill_item[0],
        "last_name": bill_item[1],
        "product_number": bill_item[2],
        "product_name": bill_item[3],
        "size": bill_item[8],
        "price": normalize_price(bill_item[6]),
        "quantity": int(bill_item[7])
    }

def add_discount(bills: dict[tuple, list[dict[str: Any]]], name: str, amount: float) -> None:
    for bill_key in bills:
        bills[bill_key].append({
            "first_name": bill_key[0],
            "last_name": bill_key[1],
            "product_number": "",
            "product_name": name,
            "size": "",
            "price": -amount,
            "quantity": 1,
        })

def import_bills(file_path: Path) -> dict[tuple, list[dict[str: Any]]]:
    bills: dict[tuple, list[dict[str: Any]]] = {}

    with file_path.open("r", encoding="utf-8") as file:
        csv = file.read()
        for i, line in enumerate(csv.splitlines()):
            if HAS_HEADER and i == 0:
                continue

            bill_item = line.split(";")
            bill_item = extract_bill_item(bill_item)

            if (bill_item["first_name"], bill_item["last_name"]) not in bills:
                bills[(bill_item["first_name"], bill_item["last_name"])] = []

            bills[(bill_item["first_name"], bill_item["last_name"])].append(bill_item)

    return bills

def export_bill(bill_items: list[dict[str: Any]]) -> None:
    first_name = bill_items[0]['first_name']
    last_name = bill_items[0]['last_name']
    print(f"Rechnung für {first_name} {last_name}:")
    print("-" * 40)
    for item in bill_items:
        product_name = item['product_name']
        size = item['size']
        price = item['price']
        quantity = item['quantity']
        total_price = price * quantity
        size_str = f" (Größe: {size})" if size else ""
        print(f"{product_name}{size_str}: {quantity} x {price:.2f} € = {total_price:.2f} €")
    print("-" * 40)
    total_sum = sum(item['price'] * item['quantity'] for item in bill_items)
    print(f"Gesamtsumme: {total_sum:.2f} €")


import_path = Path.cwd() / FILENAME
bills: dict[tuple, list[dict[str: Any]]] = import_bills(import_path)

add_discount(bills, "Zuschuss Wachdienst Bekleidung", 40.0)

for bill_key, bill_items in bills.items():
    total = sum(item['price'] * item['quantity'] for item in bill_items)

    if total <= 0.0:
        continue

    export_bill(bill_items)
    print()