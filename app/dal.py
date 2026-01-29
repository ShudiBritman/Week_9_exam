from typing import List, Dict, Any
from db import get_db_connection
import json

def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute(
    '''select customername, creditlimit
    from customers
    where creditlimit < 10000 or creditlimit > 100000
    ''')
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    json_data = json.dumps(result)
    return json_data

def get_orders_with_null_comments():
    """Return orders that have null comments."""
    pass

def get_first_5_customers():
    """Return the first 5 customers."""
    pass

def get_payments_total_and_average():
    """Return total and average payment amounts."""
    pass

def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    pass

def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    pass

def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    pass

def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    """Return customers and payments for last names matching pattern."""
    pass
