import datetime
import json
import random

import pandas as pd

#  data prep
df_companies = pd.read_csv("company_customers.csv")

print(df_companies.head())
print(df_companies.info())

# Relationship Officers
relationship_officers = [
    {"id": "019bb22d-7b0d-75b2-bc66-2dda2d88a8c7", "full_name": "Fatima Abdul"},
    {"id": "019bb22c-9306-7cf5-b1bb-7c5f6d456dd7", "full_name": "Emmanuel Tetteh"},
    {"id": "019bb22b-af58-7b63-9bc8-5e768dffabbe", "full_name": "Abena Frimpong"},
    {"id": "019bb22a-ce3a-7314-abaa-c95fbccaf234", "full_name": "Mohammed Issah"},
    {"id": "019bb229-f65c-7086-8813-64c21ce35281", "full_name": "Gladys Oppong"},
    {"id": "019bb228-7b29-7f09-8ab5-6f4e8dcda62e", "full_name": "Mavis Kwarteng"},
    {"id": "019bb227-2a93-74e5-8252-5f0e0f484fa6", "full_name": "Richard Baah"},
    {"id": "019bb226-17b0-7cf6-87a8-9ac078914213", "full_name": "Hannah Nyarko"},
    {"id": "019bb224-e954-7074-b704-ec148e8f1197", "full_name": "Ibrahim Sule"},
    {"id": "019bb223-fe53-731e-b145-6c71cfdb40ee", "full_name": "Adjoa Darko"},
    {"id": "019bb223-054e-7550-84b6-3c223ca751ed", "full_name": "Samuel Ofori"},
    {"id": "019bb222-00bc-74bd-810e-e4798f0540dd", "full_name": "Patricia Lamptey"},
    {"id": "019bb220-c4c1-71d0-b750-5b46cdeb8bff", "full_name": "Daniel Agyeman"},
    {"id": "019bb21f-4b85-7412-b058-1346447082a2", "full_name": "Esi Quaye"},
    {"id": "019bb21e-305d-70ea-b751-f1d6cf573cde", "full_name": "Kofi Appiah"},
    {"id": "019bb21d-4552-7029-b30b-570d9bceb701", "full_name": "Akosua Asante"},
    {"id": "019bb21b-5b92-7f05-b34a-6373121ead83", "full_name": "Yaw Owusu"},
    {"id": "019bb21a-07b8-7469-a021-e2b1e66b89b3", "full_name": "Ama Boateng"},
    {"id": "019bb218-b9a5-78d7-85fb-285579b52b45", "full_name": "Kwame Mensah"},
]

# Institutions
institutions = [
    {
        "id": "019bb21d-0299-7cd7-b58c-c560c19b3575",
        "name": "National Communications Authority (NCA)",
    },
    {
        "id": "019bb21c-d586-7181-b993-8c53553a58f2",
        "name": "G4S Security Services Ghana",
    },
    {
        "id": "019bb21c-ac61-7c3c-8474-9f5dd39352dd",
        "name": "Universal Merchant Bank (UMB)",
    },
    {
        "id": "019bb21c-85a9-7b3c-aa4d-9c6ac060ed01",
        "name": "Ghana Ports and Harbours Authority (GPHA)",
    },
    {
        "id": "019bb21c-50bd-7835-85e5-347bcc1291c0",
        "name": "Guinness Ghana Breweries PLC",
    },
    {"id": "019bb21c-27ad-7eef-8a1e-3aef2c382a60", "name": "MTN Ghana (Scancom PLC)"},
    {
        "id": "019bb21c-0219-7a5d-833b-987f09443a78",
        "name": "Kempinski Hotel Gold Coast City",
    },
    {
        "id": "019bb21b-dad8-71c4-871d-f58ac2637684",
        "name": "Ghana Highway Authority (GHA)",
    },
    {
        "id": "019bb21b-b395-7dfa-bf60-be06d95e4038",
        "name": "Newmont Ghana Gold Limited",
    },
    {
        "id": "019bb21b-8662-7861-b61a-4bb96c9b1e47",
        "name": "Ghana National Petroleum Corporation (GNPC)",
    },
    {
        "id": "019bb21b-6470-7ddb-91bd-0710fe38a1c5",
        "name": "Jospong Group of Companies",
    },
    {
        "id": "019bb21b-3f05-7b01-ae7f-ce4cab24fdd4",
        "name": "Intercity STC Coaching Limited",
    },
    {
        "id": "019bb21b-1396-7dca-8398-bcca502218ab",
        "name": "Electricity Company of Ghana (ECG)",
    },
    {
        "id": "019bb21a-edc3-73da-aa0b-6cfbbc3effd0",
        "name": "Volta River Authority (VRA)",
    },
    {
        "id": "019bb21a-bfaf-765f-a34c-9f8e94351166",
        "name": "AngloGold Ashanti (Ghana) Limited",
    },
    {
        "id": "019bb219-8340-7701-904d-1e5adf24b3e0",
        "name": "Ghana Broadcasting Corporation (GBC)",
    },
    {
        "id": "019bb219-5bfd-715c-b69d-8053109422b3",
        "name": "National Identification Authority (NIA)",
    },
    {
        "id": "019bb219-3952-7a65-8d51-d2a1b0de4c5d",
        "name": "Accra Metropolitan Assembly (AMA)",
    },
    {
        "id": "019bb219-1788-7720-ab4d-31611763e64d",
        "name": "Ghana Insurers Association (GIA)",
    },
    {
        "id": "019bb218-ee77-7f32-a0e7-bcf174eb445e",
        "name": "Ghana Police Service (Headquarters)",
    },
    {
        "id": "019bb218-c8fe-77fb-bf95-29527b8d92df",
        "name": "National Disaster Management Organisation (NADMO)",
    },
    {
        "id": "019bb218-a39d-74e4-bb9f-f005d3b5ef37",
        "name": "Ghana National Association of Teachers (GNAT)",
    },
    {"id": "019bb218-1f7d-7aa6-a471-af0186f53ff4", "name": "Ghana Oil Company (GOIL)"},
    {
        "id": "019bb217-f843-7832-ae91-8181961c04fb",
        "name": "Ghana Grid Company (GRIDCo)",
    },
    {
        "id": "019bb217-edbe-7372-959a-cbf4945f4774",
        "name": "Ghana Private Road Transport Union (GPRTU)",
    },
    {
        "id": "019bb217-c1ad-7213-9aee-e42913864c4b",
        "name": "Christian Council of Ghana",
    },
    {
        "id": "019bb217-945d-7b75-9512-192493fb35b9",
        "name": "National Catholic Secretariat",
    },
    {
        "id": "019bb217-4631-736e-a5ff-6dff0b94c499",
        "name": "Komfo Anokye Teaching Hospital (KATH)",
    },
    {
        "id": "019bb217-1c81-7e0d-a992-8eb320d0e132",
        "name": "Korle Bu Teaching Hospital (KBTH)",
    },
    {
        "id": "019bb216-ec23-70e3-acb9-0bfdf09015eb",
        "name": "Kwame Nkrumah University of Science and Technology (KNUST)",
    },
    {"id": "019bb216-bfd1-786f-be32-247ffa4505c4", "name": "University of Ghana (UG)"},
    {
        "id": "019bb216-8cda-72f8-b45c-62b92cca82f2",
        "name": "Ghana Revenue Authority (GRA)",
    },
    {"id": "019bb216-4910-7085-a31f-30b2155c4214", "name": "Bank of Ghana (BoG)"},
    {
        "id": "019bb216-1b0e-7878-8e7c-afd1edba8899",
        "name": "Social Security and National Insurance Trust (SSNIT)",
    },
    {
        "id": "019bb215-e09c-74b3-a5ba-af6948e9295b",
        "name": "Driver and Vehicle Licensing Authority (DVLA)",
    },
    {
        "id": "019bb215-b5c1-7a7a-99cf-f9660d30a43e",
        "name": "National Insurance Commission (NIC)",
    },
]

# introducers
introducers = [
    "Shawn Carter", "Mr. Sandman", "Miss Robelle", "Nii Torto", "Yaw Owusu",
    "Abena Dankwa", "Kojo Antwi", "Esi Mansa", "Kwesi Appiah", "Afia Amankwaa",
    "John Mahama", "Nana Akufo", "Theresa Kufuor", "Jerry Rawlings", "Atta Mills",
    "Rebecca Akufo-Addo", "Samira Bawumia", "Lordina Mahama", "Fulera Limann", "Naadu Mills"
]

# Cities
cities = [
    "Accra",
    "Kumasi",
    "Tamale",
    "Takoradi",
    "Tema",
    "Cape Coast",
    "Koforidua",
    "Sunyani",
    "Ho",
    "Bolgatanga",
    "Wa",
    "Obuasi",
    "Teshie",
    "Nungua",
    "Madina",
    "Ashaiman",
    "Techiman",
    "Winneba",
    "Agona Swedru",
]


def gen_phone_number() -> str:
    # generate international phone numbers with format: +233234545323
    prefixes: list[str] = ["20", "24", "50", "54", "25", "55", "23", "25", "59"]
    prefix = random.choice(prefixes)

    number = "".join([str(random.randint(0, 9)) for _ in range(7)])

    return f"+233{prefix}{number}"


def generate_tin_number() -> str:
    # tin is usually a 10 digit alphanumeric code that starts with P
    numbers = "".join([str(random.randint(0, 9)) for _ in range(10)])
    return f"P{numbers}"


def gen_date() -> str:
    # generate random dates
    start_date = datetime.date(1970, 1, 1)
    end_date = datetime.date(2025, 12, 31)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date.strftime("%Y-%m-%dT00:00:00Z")


def gen_company_customers():
    # generate customers that are of type company
    output_data = []

    for index, row in df_companies.iterrows():
        company = {
            "altPhoneNumber": gen_phone_number(),
            "companyName": row["fake-company-name"],
            "companyRegistrationDate": gen_date(),
            "companyRegistrationNumber": row["ein"],
            "customerType": "company",
            "email": row["company-email"],
            "institutionId": random.choice(institutions)["id"],
            "introducer": random.choice(introducers),
            "location": random.choice(cities),
            "phoneNumber": gen_phone_number(),
            "relationshipOfficerId": random.choice(relationship_officers)["id"],
            "tinNumber": generate_tin_number(),
        }

        output_data.append(company)

    #  save data to json
    with open("customer_companies.json", "w") as f:
        json.dump(output_data, f, indent=4)
