import os
import numpy as np

from datetime import datetime
from dateutil.relativedelta import relativedelta

from insurance_data_generator import (
    generate_insureds,
    generate_specialty_lines,
    generate_policies,
    generate_reinsurance_data,
)

if __name__ == "__main__":
    np.random.seed(seed=42)

    specialty_lines_data = {
        "cyber": [
            "Data Breach Coverage",
            "Cyber Extortion Protection",
            "Business Interruption - Cyber",
            "Network Security Liability",
            "Privacy Liability",
            "Media Liability",
            "Regulatory Defense & Penalties",
            "Social Engineering Fraud"
        ],
        "professional_liability": [
            "Errors & Omissions - Technology",
            "Errors & Omissions - Financial",
            "Errors & Omissions - Legal",
            "Errors & Omissions - Architects & Engineers",
            "Errors & Omissions - Real Estate",
            "Errors & Omissions - Insurance Brokers",
            "Errors & Omissions - Consultants",
            "Professional Indemnity"
        ],
        "directors_officers": [
            "D&O Liability - Private Companies",
            "D&O Liability - Public Companies",
            "D&O Liability - Non-Profits",
            "Side A DIC Coverage",
            "Employment Practices Liability",
            "Fiduciary Liability",
            "Crime Coverage",
            "Kidnap & Ransom"
        ],
        "product_liability": [
            "Life Sciences Product Liability",
            "Consumer Products Liability",
            "Component Parts Liability",
            "Medical Device Liability",
            "Pharmaceutical Liability",
            "Chemical Product Liability",
            "Product Recall Coverage",
            "Product Guarantee"
        ],
        "environmental": [
            "Pollution Legal Liability",
            "Contractors Pollution Liability",
            "Site Specific Pollution Liability",
            "Environmental Remediation Cost Cap",
            "Underground Storage Tank Liability",
            "Transportation Pollution Liability",
            "Contaminated Properties",
            "Natural Resource Damages"
        ],
        "medical_malpractice": [
            "Physician Professional Liability",
            "Hospital Professional Liability",
            "Allied Healthcare Liability",
            "Long-term Care Facility Liability",
            "Clinical Trials Coverage",
            "Telemedicine Liability",
            "Medical Director Liability",
            "Surgical Centers Liability"
        ],
        "specialty_package": [
            "Aviation Insurance",
            "Marine Cargo Coverage",
            "Political Risk Insurance",
            "Crop Insurance",
            "Weather/Parametric Insurance",
            "Space & Satellite Insurance",
            "Trade Credit Insurance",
            "Terrorism Risk Insurance"
        ],
        "special_events": [
            "Event Cancellation Insurance",
            "Event Liability Coverage",
            "Film Production Insurance",
            "Concert & Tour Insurance",
            "Wedding Insurance",
            "Sports Event Coverage",
            "Convention Insurance",
            "Prize Indemnity Insurance"
        ],
        "fine_art_collectibles": [
            "Fine Art Insurance",
            "Jewelry Dealers Coverage",
            "Museum Collection Insurance",
            "Rare Coin & Stamp Coverage",
            "Wine Collection Insurance",
            "Classic Car Insurance",
            "Antiques Dealer Coverage",
            "High-Value Home Contents"
        ]
    }
    
    # Weight line categories based on frequency in specialty market
    line_categories_frequency = (
        ["cyber"] * 25
        + ["professional_liability"] * 30
        + ["directors_officers"] * 20
        + ["product_liability"] * 15
        + ["environmental"] * 10
        + ["medical_malpractice"] * 20
        + ["specialty_package"] * 10
        + ["special_events"] * 5
        + ["fine_art_collectibles"] * 5
    )

    gen_id = "specialty_insurance_data"
    output_location = f"./input_data/{gen_id}"
    os.makedirs(output_location, exist_ok=True)

    # Generate 150 business insureds for specialty insurance
    print("Generating insureds...")
    gen_insureds = generate_insureds(output_location, 150)
    
    # Generate specialty insurance lines
    print("Generating specialty lines...")
    line_id_lookup = generate_specialty_lines(output_location, specialty_lines_data)

    # Generate data for the last 24 months (specialty insurance tends to have longer policy terms)
    print("Setting up date range for policy generation...")
    end_date = datetime.today()
    delta = relativedelta(months=24)
    start_date = end_date - delta

    # Generate policies and claims
    print("Generating policies and claims...")
    generate_policies(
        output_location,
        gen_insureds,
        specialty_lines_data,
        line_id_lookup,
        line_categories_frequency,
        start_date,
        end_date,
    )
    
    # Generate reinsurance data
    print("Generating reinsurance data...")
    generate_reinsurance_data(
        output_location,
        list(specialty_lines_data.keys())
    )
    
    print(f"Specialty insurance data generation complete. Data saved to {output_location}")
    print("\nData model includes:")
    print("- Business insureds with industry, revenue, and risk profiles")
    print("- Specialty lines across 9 categories")
    print("- Policies with underwriting notes, endorsements, and detailed terms")
    print("- Claims with litigation status, reserves, and complex resolution paths")
    print("- Reinsurance treaties and coverage details")