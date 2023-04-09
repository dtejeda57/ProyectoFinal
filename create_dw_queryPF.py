CREATE_DW =  '''

truncate table dimorders;
truncate table dimproducts;
truncate table factorderitems;


create table if not exists dimorders(
    order_id int primary key,
    order_date date,
    customer_id int,
    total_amount double,
    first_name varchar(100),
    last_name varchar(100),
    city varchar(100),
    country varchar(100),
    phone varchar(50)
);
    
create table if not exists dimproducts(
    product_id int primary key,
    product_name varchar(35),
    supplier_id int,
    unit_price double,
    package varchar(100),
    is_discontinued INT,
    company_name varchar(50),
    contact_name varchar (50),
    city varchar(50),
    country varchar(50),
    phone varchar(50),
    fax varchar(50)
);

create table if not exists factorderitems(
    order_item_id INT,
    order_id int,
    product_id int,
    unit_price double,
    quantity int,

    constraint fk_order_id
        foreign key (order_id)
            references dimorders(order_id),
    
    constraint fk_product_id
        foreign key (product_id)
            references dimproducts(product_id)

);
 '''