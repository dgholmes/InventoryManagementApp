import sqlite3

CREATE_PRODUCT_INFO_TABLE = """
    CREATE TABLE IF NOT EXISTS product_information(
        serial TEXT PRIMARY KEY, 
        name TEXT,
        year TEXT, 
        version TEXT,
        category TEXT,
        entry_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        owner TEXT, 
        user TEXT, 
        status TEXT
    );
    """

CREATE_CUSTOMER_TABLE = """
    CREATE TABLE IF NOT EXISTS customer_information(
        org_name TEXT,
        staff_name TEXT PRIMARY KEY,
        phone_number TEXT,
        email TEXT
    );
    """

CREATE_PURCHASE_DETAILS_TABLE = """
    CREATE TABLE IF NOT EXISTS purchase_details(
        id INTEGER,
        customer_id TEXT,
        staff_id TEXT,
        purchase_date TEXT
    );
    """

CREATE_PURCHASED_ITEMS_TABLE = """
    CREATE TABLE IF NOT EXISTS purchase_details(
        purchase_id INTEGER,
        product_id TEXT
    );
    """

CREATE_RENT_DETAILS_TABLE = """
    CREATE TABLE IF NOT EXISTS purchase_details(
        id INTEGER,
        customer_id TEXT,
        staff_id TEXT,
        rent_date TEXT,
        notes TEXT,
        status TEXT
    );
    """

CREATE_RENTED_ITEMS_TABLE1 = """
    CREATE TABLE IF NOT EXISTS purchase_details(
        rent_id INTEGER,
        product_id TEXT
        rented_on TEXT,
        returned TEXT,
        status TEXT
    );
    """

CREATE_USIM_INFO_TABLE = """
    CREATE TABLE IF NOT EXISTS usim_information(
        owner TEXT,
        serial TEXT PRIMARY KEY, 
        device TEXT, 
        phone_number TEXT,
        period TEXT, 
        start_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        end_date TEXT,
        status TEXT
    );
    """

CREATE_CUSTOMER_TABLE2 = """
    CREATE TABLE IF NOT EXISTS customer_information(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        org_name TEXT,
        staff_name TEXT PRIMARY KEY,
        phone_number TEXT,
        email TEXT
    );
    """

CREATE_RENTAL_INFO_TABLE = """
    CREATE TABLE IF NOT EXISTS rental_information(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        staff_id INTEGER,    
        customer_id INTEGER NOT NULL,
        rented_on TEXT,
        returned TEXT,
        status TEXT,
        notes TEXT, 
        items_id INTEGER NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customer_information (id), 
        FOREIGN KEY (items_id) REFERENCES rented_items (id)
    );
    """

CREATE_RENTED_ITEMS_TABLE = """
    CREATE TABLE IF NOT EXISTS rented_items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rental_id INTEGER NOT NULL,
        product_id TEXT,
        rented_on TEXT,
        returned TEXT,
        status TEXT,
        FOREIGN KEY (rental_id) REFERENCES rental_information (id)
    );
    """

INSERT_PRODUCT = "INSERT OR IGNORE INTO product_information VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);"

GET_ALL_PRODUCTS = "SELECT * FROM product_information;"

GET_PRODUCTS_BY_NAME = "SELECT * FROM product_information WHERE name = ?;"

GET_PRODUCT_BY_SERIAL = "SELECT * FROM product_information WHERE serial = ?;"

GET_NO_OF_PRODUCTS = "SELECT category, COUNT(*) FROM product_information GROUP BY category;"

GET_NO_OF_PRODUCTS_HOME = "SELECT COUNT(ALL) FROM product_information WHERE category = ?;"

GET_NO_OF_PRODUCTS_HOME2 = "SELECT COUNT(ALL) FROM product_information WHERE category = ?, ?, ?, ?, ?, ?;"

INSERT_CUSTOMER = "INSERT INTO customer_information VALUES(?, ?, ?, ?);"

GET_ALL_CUSTOMERS = "SELECT * FROM customer_information;"

GET_CUSTOMER_BY_NAME = "SELECT * FROM customer_information WHERE staff_name = ?;"

INSERT_USIM = "INSERT OR IGNORE INTO usim_information VALUES(?, ?, ?, ?, ?, ?, ?, ?);"

GET_ALL_USIMS = "SELECT * FROM usim_information;"

GET_USIM_BY_SERIAL = "SELECT * FROM usim_information WHERE serial = ?;"

GET_USIM_BY_NAME = "SELECT * FROM customer_information WHERE owner = ?;"


def connect():
    return sqlite3.connect("toppdata.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_PRODUCT_INFO_TABLE)
        connection.execute(CREATE_CUSTOMER_TABLE)
        connection.execute(CREATE_USIM_INFO_TABLE)


# Products
def add_product(connection, serial, name, year, version, category, entry_date, owner, user, status):
    with connection:
        connection.execute(INSERT_PRODUCT, (serial, name, year, version, category, entry_date, owner, user, status))

    added_product = connection.execute(GET_PRODUCT_BY_SERIAL, (serial,)).fetchall()
    return added_product[-1]


def get_all_products(connection):
    with connection:
        return connection.execute(GET_ALL_PRODUCTS).fetchall()


def get_all_products_by_name(connection, name):
    with connection:
        return connection.execute(GET_PRODUCTS_BY_NAME, (name,)).fetchall()


def get_product_by_serial(connection, serial):
    with connection:
        product = connection.execute(GET_PRODUCT_BY_SERIAL, (serial,)).fetchall()
        return product[-1]


def search_by_serial(connection, serial):
    with connection:
        product = connection.execute(GET_PRODUCT_BY_SERIAL, (serial,)).fetchall()
        return product


def get_no_of_products(connection):
    with connection:
        summary = connection.execute(GET_NO_OF_PRODUCTS).fetchall()
        return summary


def get_no_of_products_home(connection, category):
    with connection:
        summary = connection.execute(GET_NO_OF_PRODUCTS_HOME, (category,)).fetchall()
        return summary[-1]


def get_no_of_products_home1(connection, spray_drone, survey_drone, battery, rover, charger, controller):
    with connection:
        summary = connection.execute(GET_NO_OF_PRODUCTS_HOME,
                                     (spray_drone, survey_drone, battery, rover, charger, controller)).fetchall()
        return summary


# Customers
def add_customer(connection, org_name, name, phone_number, email):
    with connection:
        connection.execute(INSERT_CUSTOMER, (org_name, name, phone_number, email))

    added_customer = connection.execute(GET_CUSTOMER_BY_NAME, (name,)).fetchall()
    return added_customer[-1]


def get_all_customers(connection):
    with connection:
        return connection.execute(GET_ALL_CUSTOMERS).fetchall()


def get_customer_by_name(connection, staff_name):
    with connection:
        customer_info = connection.execute(GET_CUSTOMER_BY_NAME, (staff_name,)).fetchall()
        if customer_info:
            return customer_info[-1]  # this returns only one item, last item on the list
        else:
            return None


def search_customer_by_name(connection, staff_name):
    with connection:
        customer = connection.execute(GET_CUSTOMER_BY_NAME, (staff_name,)).fetchall()
        return customer  # this returns the whole list with multiple items if available


# USIM
def add_usim(connection, owner, serial, device, phone_number, period, start_date, end_date, status):
    with connection:
        connection.execute(INSERT_USIM, (owner, serial, device, phone_number, period, start_date, end_date, status))

    added_usim = connection.execute(GET_USIM_BY_SERIAL, (serial,)).fetchall()
    return added_usim[-1]


def get_all_usims(connection):
    with connection:
        return connection.execute(GET_ALL_USIMS).fetchall()


def get_usim_by_serial(connection, serial):
    with connection:
        usim = connection.execute(GET_USIM_BY_SERIAL, (serial,)).fetchall()
        return usim[-1]


def search_usim_by_serial(connection, serial):
    with connection:
        usim = connection.execute(GET_USIM_BY_SERIAL, (serial,)).fetchall()
        return usim


def get_all_usim_by_name(connection, owner):
    with connection:
        return connection.execute(GET_USIM_BY_NAME, (owner,)).fetchall()
