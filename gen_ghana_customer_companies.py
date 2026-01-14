import json
import random
import pandas as pd

from gen_data import cities, gen_date, gen_phone_number, generate_tin_number, institutions, introducers, relationship_officers

df_ghana_companies = pd.read_json("nigerian_customers_company.json")


def gen_ghanaian_company_customers():
	# generate ghanaian company customers.
	output_data = []
	
	for index, row in df_ghana_companies.iterrows():
		company = {
			"altPhoneNumber": gen_phone_number(),
            "companyName": row["Company Name"],
            "companyRegistrationDate": gen_date(),
            "companyRegistrationNumber": row["Ein"],
            "customerType": "company",
            "email": row["Company Email"],
            "institutionId": random.choice(institutions)["id"],
            "introducer": random.choice(introducers),
            "location": random.choice(cities),
            "phoneNumber": gen_phone_number(),
            "relationshipOfficerId": random.choice(relationship_officers)["id"],
            "tinNumber": generate_tin_number(),
		}
		
		output_data.append(company)
		
	# save the data to json
	with open("nigerian_customers_company_output.json", "w") as file:
		json.dump(output_data, file, indent=4)