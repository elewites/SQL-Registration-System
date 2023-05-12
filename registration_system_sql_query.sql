CREATE DATABASE registration_system;

CREATE TABLE registration_system.employees(
    id int,
    name varchar(255),
    phone varchar(255)
);

INSERT INTO registration_system.employees(id, name, phone)
VALUES ('1', 'User#1', '111');

INSERT INTO registration_system.employees(id, name, phone)
VALUES ('2', 'User#2', '222');

INSERT INTO registration_system.employees(id, name, phone)
VALUES ('3', 'User#3', '333');



