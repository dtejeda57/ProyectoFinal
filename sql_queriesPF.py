DDL_QUERY =  '''
CREATE TABLE IF NOT EXISTS Customers(
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    city VARCHAR(100),
    country VARCHAR(100),
    phone VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Orders(
    order_id INT PRIMARY KEY,
    order_date VARCHAR(50),
    customer_id INT,
    total_amount DOUBLE precision,
    
    CONSTRAINT fk_customer_id
        FOREIGN KEY (customer_id)
            REFERENCES Customers(customer_id)
);


CREATE TABLE IF NOT EXISTS Suppliers(
    supplier_id INT PRIMARY KEY,
    company_name VARCHAR(50),
    contact_name VARCHAR (50),
    city VARCHAR(50),
    country VARCHAR(50),
	phone VARCHAR(50),
	fax VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Products(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(35),
    supplier_id INT,
    unit_price DOUBLE precision,
    package VARCHAR(100),
    is_discontinued int,
    
    CONSTRAINT fk_supplier_id
        FOREIGN KEY (supplier_id)
            REFERENCES Suppliers(supplier_id)

);

CREATE TABLE IF NOT EXISTS OrderItems(
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    unit_price DOUBLE PRECISION,
    quantity INT,

    CONSTRAINT fk_order_id
        FOREIGN KEY (order_id)
            REFERENCES Orders(order_id),

    CONSTRAINT fk_product_id
        FOREIGN KEY (product_id)
            REFERENCES Products(product_id)
);
 '''