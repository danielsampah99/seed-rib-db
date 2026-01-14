import json

from faker import Faker
from faker.generator import random

from gen_data import (
    gen_date,
    gen_phone_number,
    institutions,
    introducers,
    relationship_officers,
)

fake = Faker(local="en_GH")


def gen_individual_customers():
    # generate fake data for individual customers
    output_data = []

    for _ in range(5000):
        individual = {
            "altPhoneNumber": gen_phone_number(),
            "customerType": "individual",
            "dateOfBirth": gen_date(),
            "email": fake.free_email(),
            "firstName": fake.first_name(),
            "ghanaCard": "GHA-123456789-0",
            "institutionId": random.choice(institutions)["id"],
            "introducer": random.choice(introducers),
            "lastName": fake.last_name(),
            "location": fake.street_name(),
            "phoneNumber": gen_phone_number(),
            "relationshipOfficerId": random.choice(relationship_officers)["id"],
        }

        output_data.append(individual)

    with open("individual_customers_output.json", "w") as file:
        json.dump(output_data, file, indent=4)
