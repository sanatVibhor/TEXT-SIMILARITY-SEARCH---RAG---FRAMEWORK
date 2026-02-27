import csv
import random
from datetime import datetime, timedelta

# -------------------------------
# Configuration
# -------------------------------

NUM_RECORDS = 100
OUTPUT_FILE = "incidents_semantic.csv"

projects = ["EmployeePortal", "Payments", "HRSystems", "InternalTools"]
categories = {
    "Access": ["Login Failure", "Password Reset"],
    "Performance": ["Slow Page Load", "Timeout"],
    "Payments": ["Transaction Failure", "Refund Delay"],
}
services = {
    "Access": "AuthService",
    "Performance": "WebGateway",
    "Payments": "PaymentService",
}

impacts = ["Low", "Medium", "High"]
urgencies = ["Low", "Medium", "High"]

# -------------------------------
# Helper functions
# -------------------------------

def random_date(start_days_ago=30):
    return datetime.now() - timedelta(days=random.randint(0, start_days_ago))


def build_semantic_text(title, issue_type):
    return f"""Title: {title}

User Context:
Employee attempting to perform an action on an internal enterprise system.

Issue Description:
The user encounters an issue related to {issue_type.lower()} while using the system.

Steps to Reproduce:
1. Open the application
2. Perform the intended action
3. Observe the system behavior

Observed Behavior:
The system does not behave as expected and prevents successful completion.

Expected Behavior:
The system should allow the user to complete the action without errors.
"""


# -------------------------------
# CSV generation
# -------------------------------

with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow([
        "ticket_id",
        "created_date",
        "project",
        "category",
        "subcategory",
        "impact",
        "urgency",
        "affected_service",
        "semantic_text",
        "source_system"
    ])

    for i in range(1, NUM_RECORDS + 1):
        category = random.choice(list(categories.keys()))
        subcategory = random.choice(categories[category])

        ticket_id = f"INC{100000 + i}"
        created_date = random_date().strftime("%Y-%m-%d")
        project = random.choice(projects)
        impact = random.choice(impacts)
        urgency = random.choice(urgencies)
        service = services[category]

        semantic_text = build_semantic_text(subcategory, category)

        writer.writerow([
            ticket_id,
            created_date,
            project,
            category,
            subcategory,
            impact,
            urgency,
            service,
            semantic_text.strip(),
            "ServiceNow"
        ])

print(f"CSV generated successfully: {OUTPUT_FILE}")
