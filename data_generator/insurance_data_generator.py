import csv
import json
import math
import os
import random
from datetime import timedelta, datetime

import numpy as np


class Insured(object):
    def __init__(self, insured_id, risk_score, industry, annual_revenue, years_in_business):
        self.insured_id = insured_id
        self.risk_score = risk_score
        self.industry = industry
        self.annual_revenue = annual_revenue
        self.years_in_business = years_in_business


def generate_insureds(
    output_location_root, number_of_insureds, return_data=True
):
    insureds = []
    with open(
        f"{output_location_root}/insureds.csv", mode="w"
    ) as insureds_file:
        csv_writer = csv.writer(
            insureds_file,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow([
            "insured_id", 
            "risk_score", 
            "business_name",
            "industry", 
            "annual_revenue", 
            "years_in_business", 
            "region", 
            "entity_type"
        ])
        
        # Define specialty insurance client data
        regions = ["North", "Southeast", "South", "London", "West", "International"]
        
        industries = [
            "Technology", "Healthcare", "Financial Services", "Entertainment", 
            "Manufacturing", "Energy", "Transportation", "Construction", 
            "Agriculture", "Hospitality", "Professional Services", "Retail"
        ]
        
        entity_types = ["Ltd", "Corporation", "Partnership", "Sole Trader", "Non-profit"]
        
        # Business name components for generation
        name_prefixes = ["Advanced", "Elite", "Premier", "Global", "Innovative", "Strategic", "Precision", "Integrated", "Dynamic"]
        name_mids = ["Tech", "Med", "Fin", "Energy", "Logistics", "Solutions", "Systems", "Services", "Products"]
        name_suffixes = ["Group", "Associates", "Partners", "Industries", "International", "Incorporated", "Ltd", "Co", "Holdings"]
        
        for pid in range(1, number_of_insureds + 1):
            # Generate risk score (1-10, higher means riskier client)
            risk_score = np.random.randint(low=1, high=11)
            
            # Generate company profile
            industry = random.choice(industries)
            annual_revenue = random.choice([
                random.randint(500000, 5000000),     # Small business
                random.randint(5000001, 25000000),   # Medium business
                random.randint(25000001, 100000000)  # Large business
            ])
            
            years_in_business = np.random.randint(low=1, high=51)  # 1-50 years
            region = random.choice(regions)
            entity_type = random.choice(entity_types)
            
            # Generate a business name
            business_name = f"{random.choice(name_prefixes)} {random.choice(name_mids)} {random.choice(name_suffixes)}"
            
            insured_id = f"IN{pid}"
            csv_writer.writerow([
                insured_id, 
                risk_score, 
                business_name,
                industry, 
                annual_revenue, 
                years_in_business, 
                region, 
                entity_type
            ])
            
            if return_data:
                insureds.append(Insured(
                    insured_id,
                    risk_score,
                    industry,
                    annual_revenue,
                    years_in_business
                ))
                
    return insureds if return_data else None


def generate_specialty_lines(output_location_root, specialty_lines_to_generate):
    line_count_digits = int(
        math.log10(len(sum(specialty_lines_to_generate.values(), []))) + 1
    )

    line_id_lookup = {k: {} for k, v in specialty_lines_to_generate.items()}
    with open(
        f"{output_location_root}/specialty_lines.csv", mode="w"
    ) as lines_file:
        csv_writer = csv.writer(
            lines_file,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow([
            "line_id", 
            "line_description", 
            "line_category", 
            "base_premium", 
            "coverage_limit",
            "deductible",
            "policy_term_months",
            "risk_level"
        ])
        
        item_index = 1
        for category in specialty_lines_to_generate:
            for item in specialty_lines_to_generate[category]:
                line_id = f"SL{str(item_index).zfill(line_count_digits)}"
                
                # Generate base premium based on product category
                if category == "cyber":
                    base_premium = random.randint(5000, 50000)
                    coverage_limit = random.choice([500000, 1000000, 5000000, 10000000, 25000000])
                    deductible = random.choice([10000, 25000, 50000, 100000])
                    policy_term_months = random.choice([12, 24, 36])
                    risk_level = random.choice(["Low", "Medium", "High", "Very High"])
                    
                elif category == "professional_liability":
                    base_premium = random.randint(3000, 40000)
                    coverage_limit = random.choice([1000000, 2000000, 5000000, 10000000])
                    deductible = random.choice([5000, 10000, 25000, 50000])
                    policy_term_months = random.choice([12, 24])
                    risk_level = random.choice(["Low", "Medium", "High"])
                    
                elif category == "directors_officers":
                    base_premium = random.randint(10000, 100000)
                    coverage_limit = random.choice([1000000, 5000000, 10000000, 25000000, 50000000])
                    deductible = random.choice([25000, 50000, 100000, 250000])
                    policy_term_months = random.choice([12, 24])
                    risk_level = random.choice(["Medium", "High", "Very High"])
                    
                elif category == "product_liability":
                    base_premium = random.randint(4000, 60000)
                    coverage_limit = random.choice([1000000, 2000000, 5000000, 10000000])
                    deductible = random.choice([10000, 25000, 50000, 100000])
                    policy_term_months = random.choice([12, 24, 36])
                    risk_level = random.choice(["Medium", "High", "Very High"])
                    
                elif category == "environmental":
                    base_premium = random.randint(8000, 75000)
                    coverage_limit = random.choice([1000000, 5000000, 10000000, 25000000])
                    deductible = random.choice([25000, 50000, 100000, 200000])
                    policy_term_months = random.choice([12, 24, 36])
                    risk_level = random.choice(["High", "Very High"])
                    
                elif category == "medical_malpractice":
                    base_premium = random.randint(15000, 120000)
                    coverage_limit = random.choice([1000000, 3000000, 5000000, 10000000])
                    deductible = random.choice([25000, 50000, 100000, 250000])
                    policy_term_months = random.choice([12, 24])
                    risk_level = random.choice(["High", "Very High"])
                    
                else:  # Special event, fine art, etc.
                    base_premium = random.randint(2000, 30000)
                    coverage_limit = random.choice([500000, 1000000, 2000000, 5000000])
                    deductible = random.choice([5000, 10000, 25000, 50000])
                    policy_term_months = random.choice([6, 12, 24])
                    risk_level = random.choice(["Low", "Medium", "High"])
                
                csv_writer.writerow([
                    line_id, 
                    item, 
                    category, 
                    base_premium, 
                    coverage_limit,
                    deductible,
                    policy_term_months,
                    risk_level
                ])
                
                line_id_lookup[category][item] = {
                    "id": line_id,
                    "base_premium": base_premium,
                    "coverage_limit": coverage_limit,
                    "deductible": deductible,
                    "policy_term_months": policy_term_months,
                    "risk_level": risk_level
                }
                
                item_index += 1
    return line_id_lookup


def generate_policies(
    output_location_root,
    insureds,
    specialty_lines,
    line_id_lookup,
    line_categories_frequency,
    start_datetime,
    end_datetime,
):
    open_files = open_policy_sinks(
        output_location_root, start_datetime, end_datetime
    )
    
    open_claim_files = open_claim_sinks(
        output_location_root, start_datetime, end_datetime
    )
    
    line_cats_count = len(specialty_lines.keys())
    num_days = (end_datetime - start_datetime).days
    all_days = [
        start_datetime + timedelta(days=d) for d in range(0, num_days + 1)
    ]
    
    # Different frequency types for policy purchases (specialty insurance is less frequent)
    insured_frequency_type = [
        int(num_days / 180),  # Very infrequent
        int(num_days / 120),  # Infrequent
        int(num_days / 90),   # Normal
        int(num_days / 60),   # Frequent
    ]
    
    policy_counter = 1
    claim_counter = 1
    
    # Track active policies for claim generation
    active_policies = []
    
    for insured in insureds:
        # Number of policy purchase days for this insured
        num_policy_days = random.choice(insured_frequency_type)
        
        relevant_categories = []
        
        if insured.industry in ["Technology", "Financial Services"]:
            relevant_categories.extend(["cyber", "directors_officers", "professional_liability"])
        
        if insured.industry in ["Healthcare"]:
            relevant_categories.extend(["medical_malpractice", "professional_liability", "cyber"])
        
        if insured.industry in ["Manufacturing", "Energy", "Agriculture"]:
            relevant_categories.extend(["product_liability", "environmental", "specialty_package"])
        
        if insured.industry in ["Entertainment", "Hospitality", "Retail"]:
            relevant_categories.extend(["special_events", "fine_art_collectibles", "product_liability"])
        
        if insured.industry in ["Professional Services"]:
            relevant_categories.extend(["professional_liability", "cyber", "directors_officers"])
        
        if insured.industry in ["Construction", "Transportation"]:
            relevant_categories.extend(["environmental", "product_liability", "specialty_package"])
            
        # Ensure we have at least one category to select from
        if not relevant_categories:
            relevant_categories = random.sample(list(specialty_lines.keys()), 2)
        
        # Remove duplicates
        relevant_categories = list(set(relevant_categories))
        
        # Number of insurance categories this insured buys from (1 to max 3)
        num_cats = min(random.randint(1, 3), len(relevant_categories))
        
        # Select random days for policy purchases
        insured_policy_days = sorted(
            random.sample(all_days, min(num_policy_days, len(all_days)))
        )
        
        # Select insurance categories for this insured based on relevance
        cats = random.sample(relevant_categories, num_cats)
        
        for day in insured_policy_days:
            # Generate policy with a llines from selected categories
            selected_category = random.choice(cats)
            
            # Ensure the category exists in our lines
            if selected_category not in specialty_lines or not specialty_lines[selected_category]:
                continue
                
            selected_line = random.choice(specialty_lines[selected_category])
            line_details = line_id_lookup[selected_category][selected_line]
            
            # Get line information
            line_id = line_details["id"]
            base_premium = line_details["base_premium"]
            policy_term_months = line_details["policy_term_months"]
            
            # Calculate policy details
            policy_start_date = day + timedelta(days=random.randint(7, 30)) 
            policy_end_date = policy_start_date + timedelta(days=30*policy_term_months)
            
            # Calculate premium based on business factors and risk score
            risk_factor = 0.8 + (insured.risk_score * 0.05)  # 0.8 to 1.3 based on risk score
            
            # Revenue factor: larger companies pay more
            if insured.annual_revenue < 5000000:  # Small
                revenue_factor = 0.8
            elif insured.annual_revenue < 25000000:  # Medium
                revenue_factor = 1.0
            else:  # Large
                revenue_factor = 1.3
                
            # Experience factor: newer companies pay more
            if insured.years_in_business < 5:
                experience_factor = 1.2
            elif insured.years_in_business < 10:
                experience_factor = 1.0
            else:
                experience_factor = 0.9
                
            # Risk level adjustment from the product
            risk_level_factor = {
                "Low": 0.9,
                "Medium": 1.0,
                "High": 1.2,
                "Very High": 1.5
            }.get(line_details["risk_level"], 1.0)
            
            final_premium = round(base_premium * risk_factor * revenue_factor * experience_factor * risk_level_factor, 2)
            
            # Generate a policy ID with the specific format used in specialty insurance
            underwriter_code = random.choice(["UW", "SP", "XL", "HL", "BT"])
            year_code = str(policy_start_date.year)[-2:]
            sequence = str(policy_counter).zfill(5)
            policy_id = f"{underwriter_code}{year_code}{sequence}"
            policy_counter += 1
            
            # Create endorsements
            num_endorsements = random.randint(0, 3)
            endorsements = []
            for i in range(num_endorsements):
                endorsement_date = policy_start_date + timedelta(days=random.randint(30, min(policy_term_months * 30 - 30, 365)))
                endorsement_type = random.choice([
                    "Additional Insured", 
                    "Increased Limit", 
                    "Coverage Extension", 
                    "Exclusion Removal", 
                    "Policy Modification"
                ])
                premium_change = random.choice([0, 0, 0, round(random.uniform(0.05, 0.20) * final_premium, 2)])  # Often no premium change
                
                endorsements.append({
                    "endorsement_id": f"{policy_id}-END{i+1}",
                    "endorsement_type": endorsement_type,
                    "effective_date": str(endorsement_date),
                    "premium_change": premium_change
                })
            
            # Adjust final premium for endorsements
            for endorsement in endorsements:
                final_premium += endorsement["premium_change"]
            
            policy = {
                "policy_id": policy_id,
                "insured_id": insured.insured_id,
                "line_id": line_id,
                "line_category": selected_category,
                "premium": final_premium,
                "coverage_limit": line_details["coverage_limit"],
                "deductible": line_details["deductible"],
                "policy_start_date": str(policy_start_date),
                "policy_end_date": str(policy_end_date),
                "payment_frequency": random.choice(["quarterly", "semi-annually", "annually"]),
                "policy_status": "active",
                "date_of_purchase": str(day),
                "underwriting_notes": random.choice([
                    "Standard terms and conditions",
                    "Modified exclusions",
                    "Additional security measures required",
                    "Conditional on quarterly loss runs",
                    "Subject to annual compliance audit"
                ]),
                "broker_id": f"BRK{random.randint(1, 25)}",
                "endorsements": endorsements
            }
            
            # Write policy to appropriate date file
            open_files[to_canonical_date_str(day)].write(
                json.dumps(policy) + "\n"
            )
            
            # Track active policy for claim generation
            active_policies.append({
                "policy_id": policy_id,
                "line_id": line_id,
                "category": selected_category,
                "insured_id": insured.insured_id,
                "risk_score": insured.risk_score,
                "start_date": policy_start_date,
                "end_date": policy_end_date,
                "premium": final_premium,
                "coverage_limit": line_details["coverage_limit"],
                "deductible": line_details["deductible"]
            })
    
# Generate claims for some of the active policies
    print(f"Generating claims for {len(active_policies)} active policies...")
    claims_generated = 0
    skipped_due_to_probability = 0
    skipped_due_to_date_range = 0
    skipped_due_to_short_duration = 0
    
    for policy in active_policies:
        # Determine if this policy will have a claim (based on risk score)
        # Specialty insurance typically has fewer but larger claims
        claim_probability = policy["risk_score"] * 0.05  # Increased from 0.02 to 0.05 (5% to 50% chance)
        
        if random.random() < claim_probability:
            # Generate claim date between policy start and end (or current date if policy still active)
            claim_date_start = policy["start_date"]
            claim_date_end = min(policy["end_date"], end_datetime)
            
            # Only generate claim if there's a valid date range
            if claim_date_start < claim_date_end:
                claim_days = (claim_date_end - claim_date_start).days
                
                # Allow claims after 14 days (reduced from 30)
                if claim_days >= 14:
                    # Generate claim date after a minimum waiting period
                    min_days = min(14, claim_days // 2)  # Wait at least 14 days or half the policy period
                    claim_date = claim_date_start + timedelta(days=random.randint(min_days, claim_days))
                    
                    # Determine claim amount and reason based on specialty insurance category
                    category = policy["category"]
                    
                    if category == "cyber":
                        claim_amount = random.randint(50000, min(1000000, policy["coverage_limit"]))
                        claim_reason = random.choice([
                            "Data breach - unauthorized access",
                            "Ransomware attack",
                            "Business email compromise",
                            "DDoS attack causing business interruption",
                            "Social engineering fraud",
                            "Privacy violation",
                            "Network security failure"
                        ])
                        
                    elif category == "professional_liability":
                        claim_amount = random.randint(25000, min(750000, policy["coverage_limit"]))
                        claim_reason = random.choice([
                            "Error in professional services",
                            "Negligent advice to client",
                            "Failure to deliver contracted services",
                            "Breach of professional duty",
                            "Client financial loss due to advice",
                            "Misrepresentation of services"
                        ])
                        
                    elif category == "directors_officers":
                        claim_amount = random.randint(75000, min(2000000, policy["coverage_limit"]))
                        claim_reason = random.choice([
                            "Breach of fiduciary duty",
                            "Regulatory investigation",
                            "Shareholder lawsuit",
                            "Mismanagement allegation",
                            "Failure to comply with regulations",
                            "Inadequate corporate governance",
                            "Securities class action"
                        ])
                        
                    elif category == "product_liability":
                        claim_amount = random.randint(30000, min(1500000, policy["coverage_limit"]))
                        claim_reason = random.choice([
                            "Product caused bodily injury",
                            "Product design defect",
                            "Manufacturing defect",
                            "Failure to warn",
                            "Product recall expenses",
                            "False advertising claim"
                        ])
                        
                    elif category == "environmental":
                        claim_amount = random.randint(100000, min(3000000, policy["coverage_limit"]))
                        claim_reason = random.choice([
                            "Pollution event",
                            "Contamination cleanup",
                            "Natural resource damages",
                            "Regulatory compliance action",
                            "Third-party property damage",
                            "Toxic tort litigation"
                        ])
                        
                    elif category == "medical_malpractice":
                        claim_amount = random.randint(50000, min(2000000, policy["coverage_limit"]))
                        claim_reason = random.choice([
                            "Surgical error",
                            "Misdiagnosis",
                            "Medication error",
                            "Failure to treat",
                            "Breach of standard of care",
                            "Patient consent issue"
                        ])
                        
                    else:  # special_events, fine_art, specialty_package
                        claim_amount = random.randint(15000, min(500000, policy["coverage_limit"]))
                        claim_reason = random.choice([
                            "Property damage",
                            "Event cancellation",
                            "Third party injury",
                            "Weather-related loss",
                            "Theft or damage of valuable items",
                            "Business interruption"
                        ])
                    
                    legal_representation = random.choice([True, False, False])
                    legal_fees = 0
                    
                    if legal_representation:
                        legal_fees = random.randint(10000, 100000)
                        claim_amount += legal_fees
                    
                    # Apply deductible
                    claim_amount_after_deductible = max(0, claim_amount - policy["deductible"])
                    
                    # Determine claim status
                    days_since_claim = (end_datetime - claim_date).days
                    if days_since_claim < 14:
                        claim_status = "filed"
                    elif days_since_claim < 30:
                        claim_status = "under_review"
                    elif days_since_claim < 90:
                        claim_status = random.choice(["under_review", "needs_information", "investigation"])
                    elif days_since_claim < 180:
                        claim_status = random.choice(["under_review", "approved", "denied", "in_litigation", "negotiation"])
                    else:
                        claim_status = random.choice(["approved", "denied", "settled", "closed", "in_litigation", "appealed"])
                    
                    # If claim approved or settled, calculate payout amount
                    payout_amount = None
                    if claim_status in ["approved", "settled"]:
                        payout_percentage = random.uniform(0.6, 0.95)
                        payout_amount = round(claim_amount_after_deductible * payout_percentage, 2)
                    
                    # Create detailed claim object
                    claim_id = f"CL{policy['category'][:2].upper()}{claim_counter}"
                    claim = {
                        "claim_id": claim_id,
                        "policy_id": policy["policy_id"],
                        "insured_id": policy["insured_id"],
                        "claim_date": str(claim_date),
                        "date_reported": str(claim_date + timedelta(days=random.randint(1, 15))),
                        "claim_amount": claim_amount,
                        "claim_amount_after_deductible": claim_amount_after_deductible,
                        "claim_reason": claim_reason,
                        "claim_description": f"Claim {claim_id} related to {claim_reason.lower()} incident.",
                        "claim_status": claim_status,
                        "legal_representation": legal_representation,
                        "legal_fees": legal_fees if legal_representation else None,
                        "payout_amount": payout_amount,
                        "claim_handler": f"CH{random.randint(1, 15)}",
                        "reserve_amount": round(claim_amount * random.uniform(0.8, 1.2), 2),
                        "subrogation_potential": random.choice([True, False, False, False]),
                        "third_party_involved": random.choice([True, False]),
                        "litigation_status": "Active" if legal_representation and random.random() < 0.7 else None
                    }
                    
                    claim_counter += 1
                    claims_generated += 1
                    
                    # Write claim to appropriate date file
                    claim_file_date = to_canonical_date_str(claim_date)
                    if claim_file_date in open_claim_files:
                        open_claim_files[claim_file_date].write(
                            json.dumps(claim) + "\n"
                        )
                else:
                    skipped_due_to_short_duration += 1
            else:
                skipped_due_to_date_range += 1
        else:
            skipped_due_to_probability += 1

    print(f"Claims generation results:")
    print(f"  - Generated {claims_generated} claims")
    print(f"  - Skipped {skipped_due_to_probability} policies based on claim probability")
    print(f"  - Skipped {skipped_due_to_date_range} policies due to invalid date range")
    print(f"  - Skipped {skipped_due_to_short_duration} policies due to short duration")

    # Close all open files
    for f in open_files.values():
        f.close()
    
    for f in open_claim_files.values():
        f.close()


def to_canonical_date_str(date_to_transform):
    return date_to_transform.strftime("%Y-%m-%d")


def open_policy_sinks(output_location_root, start_datetime, end_datetime):
    root_policies_dir = f"{output_location_root}/policies/"
    open_files = {}
    days_to_generate = (end_datetime - start_datetime).days
    for next_day_offset in range(0, days_to_generate + 1):
        next_day = to_canonical_date_str(
            start_datetime + timedelta(days=next_day_offset)
        )
        day_directory = f"{root_policies_dir}/d={next_day}"
        os.makedirs(day_directory, exist_ok=True)
        open_files[next_day] = open(
            f"{day_directory}/policies.json", mode="w"
        )
    return open_files


def open_claim_sinks(output_location_root, start_datetime, end_datetime):
    root_claims_dir = f"{output_location_root}/claims/"
    open_files = {}
    days_to_generate = (end_datetime - start_datetime).days
    for next_day_offset in range(0, days_to_generate + 1):
        next_day = to_canonical_date_str(
            start_datetime + timedelta(days=next_day_offset)
        )
        day_directory = f"{root_claims_dir}/d={next_day}"
        os.makedirs(day_directory, exist_ok=True)
        open_files[next_day] = open(
            f"{day_directory}/claims.json", mode="w"
        )
    return open_files


def generate_premium_payments(
    output_location_root,
    start_datetime,
    end_datetime,
):
    """
    Generate premium payments based on policies
    This reads the created policies and generates appropriate payment records
    """
    # Implementation would go here - read policies and create payment records
    # For simplicity, lets skip this example!
    pass


def generate_reinsurance_data(
    output_location_root, 
    line_categories
):
    """
    Generate reinsurance treaties and cessions data
    """
    # Create reinsurance treaties file
    with open(f"{output_location_root}/reinsurance_treaties.csv", mode="w") as treaties_file:
        csv_writer = csv.writer(
            treaties_file,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        
        csv_writer.writerow([
            "treaty_id",
            "treaty_name",
            "treaty_type",
            "reinsurer",
            "effective_date",
            "expiration_date",
            "covered_categories",
            "retention",
            "limit",
            "premium_rate"
        ])
        
        # Create different treaty types for different line categories
        reinsurers = ["Munich Re", "Swiss Re", "Hannover Re", "SCOR", "Syndicate 1984", 
                      "Brit", "Everest Re", "Beazley", "Axis Capital", "Renaissance Re"]
        
        treaty_types = ["Quota Share", "Excess of Loss", "Surplus", "Facultative Obligatory", "Catastrophe XL"]
        
        # Generate 10-15 reinsurance treaties
        for i in range(1, random.randint(10, 15) + 1):
            treaty_id = f"RT{i}"
            treaty_name = f"Treaty {i} - {random.choice(treaty_types)}"
            treaty_type = random.choice(treaty_types)
            reinsurer = random.choice(reinsurers)
            
            # Set dates for treaty
            effective_year = random.randint(2020, 2024)
            effective_month = random.randint(1, 12)
            effective_day = random.randint(1, 28)
            effective_date = datetime(effective_year, effective_month, effective_day)
            expiration_date = effective_date + timedelta(days=365)  # One year treaties
            
            # Set covered categories (randomly select 1-3 categories)
            covered_cats = random.sample(line_categories, random.randint(1, min(3, len(line_categories))))
            covered_categories = "|".join(covered_cats)
            
            # Set financial terms
            if treaty_type == "Quota Share":
                retention = f"{random.randint(30, 70)}%"  # Percentage retention
                limit = "N/A"
                premium_rate = f"{random.randint(5, 30)}%"  # Percentage of premium ceded
            elif treaty_type == "Excess of Loss":
                retention = f"{random.randint(250, 1000) * 1000}"  # £250k to $1M
                limit = f"{random.randint(1, 10) * 1000000}"  # £1M to $10M
                premium_rate = f"{random.randint(3, 15)}%"
            elif treaty_type == "Catastrophe XL":
                retention = f"{random.randint(1, 5) * 1000000}"  # £1M to $5M
                limit = f"{random.randint(10, 50) * 1000000}"  # £10M to $50M
                premium_rate = f"{random.randint(5, 20)}%"
            else:
                retention = f"{random.randint(100, 500) * 1000}"  # £100k to $500k
                limit = f"{random.randint(1, 10) * 1000000}"  # £1M to $10M
                premium_rate = f"{random.randint(5, 25)}%"
            
            csv_writer.writerow([
                treaty_id,
                treaty_name,
                treaty_type, 
                reinsurer,
                effective_date.strftime("%Y-%m-%d"),
                expiration_date.strftime("%Y-%m-%d"),
                covered_categories,
                retention,
                limit,
                premium_rate
            ])
    
    # In a full implementation, would also generate cession records for policies
    # showing how much of each policy is ceded to reinsurance treaties