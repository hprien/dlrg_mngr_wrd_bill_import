class Bill_Import:
    def __import_mitglieder(self, mitglieder_path, mitglieder_has_header, mitglieder_seperator):
        mitglieder = []
        with mitglieder_path.open("r", encoding="utf-8") as file:
            csv = file.read()
            for i, line in enumerate(csv.splitlines()):
                if mitglieder_has_header and i == 0:
                    continue

                mitglied = line.split(mitglieder_seperator)
                mitglieder.append({
                    "no": mitglied[0],
                    "first_name": mitglied[5].strip(),
                    "last_name": mitglied[4].strip(),
                })

        return mitglieder
    
    def __import_email_adress(self, email_adress_path, email_adress_has_header, email_adress_seperator):
        email_adress = []
        with email_adress_path.open("r", encoding="utf-8") as file:
            csv = file.read()
            for i, line in enumerate(csv.splitlines()):
                if email_adress_has_header and i == 0:
                    continue

                adress = line.split(email_adress_seperator)
                email_adress.append({
                    "first_name": adress[0].strip(),
                    "last_name": adress[1].strip(),
                    "email": adress[2].strip(),
                })

        return email_adress

    def __init__(self, billing_date, due_days, buchhaltungskonto, sk42_sphaere, mwst_satz, mitglieder_path, mitglieder_has_header, mitglieder_seperator, email_adress_path, email_adress_has_header, email_adress_seperator):
        self.billing_date = billing_date
        self.due_days = due_days
        self.buchhaltungskonto = buchhaltungskonto
        self.sk42_sphaere = sk42_sphaere
        self.mwst_satz = mwst_satz

        self.mitglieder = self.__import_mitglieder(mitglieder_path, mitglieder_has_header, mitglieder_seperator)
        self.email_adress = self.__import_email_adress(email_adress_path, email_adress_has_header, email_adress_seperator)

        self.bills = []

    def add_bill(self, first_name, last_name):
        self.bills.append({
            "first_name": first_name,
            "last_name": last_name,
            "mitglieds_no": next((m["no"] for m in self.mitglieder if m["first_name"] == first_name and m["last_name"] == last_name), None),
            "email": next((e["email"] for e in self.email_adress if e["first_name"] == first_name and e["last_name"] == last_name), None),
            "bill_items": [],
        })

        return len(self.bills) - 1

    def add_bill_item(self, bill_index, product_name, size, price, quantity):
        bill = self.bills[bill_index]
        bill["bill_items"].append({
            "bill_title": f"Wachdienstbekleidung 2025 {bill['first_name']} {bill['last_name']}",
            "item_title": product_name,
            "item_description": f"Größe: {size}" if size else "",
            "quantity": quantity,
            "price": price
        })

    def write_import_file(self, output_path):
        with output_path.open("w", encoding="utf-8") as file:
            for bill_index, bill in enumerate(self.bills):
                for item_index, item in enumerate(bill["bill_items"]):
                    line = f"{bill['mitglieds_no']};{bill_index};{item_index};{item['bill_title']};{self.billing_date};{item['item_title']};{item['item_description']};{item['quantity']};{item['price']:.2f};{self.due_days};{self.buchhaltungskonto};{self.sk42_sphaere};{self.mwst_satz:.2f};{bill['email']}\n"
                    file.write(line)