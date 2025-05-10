# Specialty Insurance Data Generator

This project generates synthetic specialty insurance data for use in data analysis exercises, training, and testing. 

The data simulates a specialty insurance company that focuses on complex, high-value risks.

## Data Model

The generator creates the following data:

### Insureds
- **insured_id**: Unique identifier (e.g., IN1, IN2)
- **risk_score**: Score from 1-10 indicating risk level (higher = riskier)
- **business_name**: Name of the business/organization
- **industry**: Business sector (Technology, Healthcare, Financial Services, etc.)
- **annual_revenue**: Annual revenue in GBP
- **years_in_business**: Number of years the business has been operating
- **region**: Geographic region
- **entity_type**: Legal structure (Ltd, Corporation, Partnership, etc.)

### Specialty Lines
- **line_id**: Unique identifier (e.g., SL001)
- **line_description**: Description of the specialty insurance line
- **line_category**: Category of specialty insurance:
  - Cyber
  - Professional Liability (E&O)
  - Directors & Officers (D&O)
  - Product Liability
  - Environmental
  - Medical Malpractice
  - Specialty Package
  - Special Events
  - Fine Art & Collectibles
- **base_premium**: Base annual premium amount for the line
- **coverage_limit**: Maximum coverage amount
- **deductible**: Amount the insured must pay before coverage begins
- **policy_term_months**: Standard term length in months
- **risk_level**: Relative risk classification (Low, Medium, High, Very High)

### Policies
- **policy_id**: Unique identifier with underwriter code (e.g., UW23-00001)
- **insured_id**: Reference to the insured
- **line_id**: Reference to the specialty line
- **premium**: Calculated premium based on risk factors
- **coverage_limit**: Coverage limit for this specific policy
- **deductible**: Deductible amount for this specific policy
- **policy_start_date**: When the policy begins
- **policy_end_date**: When the policy expires
- **payment_frequency**: How often premiums are paid (quarterly, semi-annually, annually)
- **policy_status**: Current status of the policy
- **date_of_purchase**: When the policy was purchased
- **underwriting_notes**: Special conditions or notes on the policy
- **broker_id**: ID of the broker who placed the business
- **endorsements**: List of policy endorsements/modifications:
  - **endorsement_id**: Unique identifier for the endorsement
  - **endorsement_type**: Type of policy modification
  - **effective_date**: When the endorsement takes effect
  - **premium_change**: Additional premium, if any

### Claims
- **claim_id**: Unique identifier with category code (e.g., CLCY001)
- **policy_id**: Reference to the associated policy
- **insured_id**: Reference to the insured
- **claim_date**: When the claim event occurred
- **date_reported**: When the claim was reported to the insurer
- **claim_amount**: Total amount claimed by the insured
- **claim_amount_after_deductible**: Amount after applying the policy deductible
- **claim_reason**: Reason for the claim
- **claim_description**: Detailed description of the claim
- **claim_status**: Status of the claim (filed, under_review, approved, denied, settled, closed)
- **legal_representation**: Whether legal counsel is involved
- **legal_fees**: Amount of legal fees incurred
- **payout_amount**: Amount paid out (if approved/settled)
- **claim_handler**: Reference to claim examiner
- **reserve_amount**: Amount reserved for the claim
- **subrogation_potential**: Whether recovery from third parties is possible
- **third_party_involved**: Whether third parties are involved
- **litigation_status**: Status of any litigation related to the claim

### Reinsurance
- **treaty_id**: Unique identifier for reinsurance treaty
- **treaty_name**: Name of the reinsurance treaty
- **treaty_type**: Type of reinsurance arrangement (Quota Share, Excess of Loss, etc.)
- **reinsurer**: Reinsurance company name
- **effective_date**: When the treaty begins
- **expiration_date**: When the treaty ends
- **covered_categories**: Specialty lines covered by the treaty
- **retention**: Amount or percentage retained by the insurer
- **limit**: Maximum coverage provided by the reinsurer
- **premium_rate**: Rate applied to calculate reinsurance premium

## File Structure

The generator creates the following files:

```
input_data/specialty_insurance_data/
├── insureds.csv
├── specialty_lines.csv
├── policies/
│   └── d=YYYY-MM-DD/
│       └── policies.json
├── claims/
│   └── d=YYYY-MM-DD/
│       └── claims.json
└── reinsurance_treaties.csv
```

Policies and claims are organized by date for easier analysis of time-based trends.

## Usage

1. Ensure you have the required dependencies:
```
pip install numpy python-dateutil
```

2. Run the main generator script:
```
python main_specialty_insurance_generator.py
```

3. The data will be generated in the `./input_data/specialty_insurance_data/` directory.

## Example Analysis Questions

This data can be used to address various specialty insurance business questions:

1. What is the loss ratio by specialty line category?
2. How do claim frequencies and severities vary across different industries?
3. What is the correlation between insured risk score and claim likelihood?
4. What is the average time to settle claims for each specialty line?
5. What is the effectiveness of reinsurance programs in managing large losses?
6. Which endorsements most frequently lead to claims?
7. How do legal expenses impact overall claim costs?
8. What policy characteristics can predict future claims?
9. How do retention levels affect profitability by line of business?

## Customization

You can customize the data generation by modifying:

- Number of insureds
- Specialty line categories and specific offerings
- Time period for data generation
- Risk and premium calculation logic
- Claim frequency and severity parameters

Simply edit the parameters in `main_specialty_insurance_generator.py` before running.