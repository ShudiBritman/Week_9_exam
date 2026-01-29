from typing import List, Dict, Any
from db import get_db_connection
import json

def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute(
    "select customername, creditlimit from customers where creditlimit < 10000 or creditlimit > 100000")
    r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    json_data = json.dumps(r)
    cnx.close()
    cursor.close()
    return json_data

def get_orders_with_null_comments():
    """Return orders that have null comments."""
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute("select ordernumber, orderdate, comments from orders where comments is null order by orderdate desc")
    r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    json_data = json.dumps(r)
    cnx.close()
    cursor.close()
    return json_data

def get_first_5_customers():
    """Return the first 5 customers."""
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute("select customername, contactlastname, contactfirstname from customers order by contactlastname limit 5")
    r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    json_data = json.dumps(r)
    cnx.close()
    cursor.close()
    return json_data

def get_payments_total_and_average():
    """Return total and average payment amounts."""
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute("select sum(amount), min(amount), max(amount), avg(amount) from payments")
    r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    json_data = json.dumps(r)
    cnx.close()
    cursor.close()
    return json_data


def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute("select e.firstname, e.lastname, o.phone ofiicePhone from employees e join offices o on o.officecode = e.officecode")
    r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    json_data = json.dumps(r)
    cnx.close()
    cursor.close()
    return json_data


def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute("select c.customername, o.orderdate from customers c left join orders o on o.customernumber = o.customernumber")
    r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    json_data = json.dumps(r)
    cnx.close()
    cursor.close()
    return json_data

def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute("select c.customername, od.quantityordered from orders o join customers c on o.customernumber = o.customernumber join orderdetails od on od.ordernumber = o.ordernumber order by c.customername")
    r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    json_data = json.dumps(r)
    cnx.close()
    cursor.close()
    return json_data

def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    """Return customers and payments for last names matching pattern."""
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute('''select c.customername, concat(e.firstname, " ", e.lastname) salesemployee, sum(p.amount) amount
                    from customers c
                    join employees e on
                    c.salesrepemployeenumber = e.employeenumber
                    join payments p on 
                    c.customernumber = p.customernumber
                    where c.contactfirstname in ('%ly%', '%Mu%')
                    group by c.customername, concat(e.firstname, " ", e.lastname)
                    order by amount desc''')
    r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    json_data = json.dumps(r)
    cnx.close()
    cursor.close()
    return json_data
