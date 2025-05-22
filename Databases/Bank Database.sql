create database bank;
use bank;
CREATE TABLE Customer (
    Customer_ID INT PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Date_of_Birth DATE,
    Gender VARCHAR(10),
    Address VARCHAR(255),
    Phone VARCHAR(15),
    Email VARCHAR(100)
);

CREATE TABLE Account (
    Account_Number INT PRIMARY KEY,
    Customer_ID INT,
    Account_Type VARCHAR(20),
    Balance DECIMAL(10,2),
    Branch_Name VARCHAR(100),
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
);

CREATE TABLE Transaction (
    Transaction_ID INT PRIMARY KEY,
    Account_Number INT,
    Transaction_Type VARCHAR(20),
    Amount DECIMAL(10,2),
    Transaction_Date DATE,
    FOREIGN KEY (Account_Number) REFERENCES Account(Account_Number)
);

CREATE TABLE Loan (
    Loan_ID INT PRIMARY KEY,
    Customer_ID INT,
    Loan_Type VARCHAR(20),
    Loan_Amount DECIMAL(10,2),
    Interest_Rate DECIMAL(5,2),
    Loan_Term INT,
    Status VARCHAR(20),
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
);
-- Inserting 10 Customers  
INSERT INTO Customer (Customer_ID, First_Name, Last_Name, Date_of_Birth, Gender, Address, Phone, Email) VALUES  
(1, 'Amit', 'Sharma', '1985-07-15', 'Male', 'Mumbai, Maharashtra', '9876543210', 'amit.sharma@gmail.com'),  
(2, 'Priya', 'Verma', '1990-03-22', 'Female', 'Delhi, Delhi', '9812345678', 'priya.verma@yahoo.com'),  
(3, 'Rahul', 'Gupta', '1988-10-05', 'Male', 'Kolkata, West Bengal', '9876501234', 'rahul.gupta@rediffmail.com'),  
(4, 'Sneha', 'Rao', '1992-12-18', 'Female', 'Bangalore, Karnataka', '9845123456', 'sneha.rao@gmail.com'),  
(5, 'Vikram', 'Singh', '1983-05-30', 'Male', 'Jaipur, Rajasthan', '9789123456', 'vikram.singh@hotmail.com'),  
(6, 'Anjali', 'Nair', '1995-09-09', 'Female', 'Chennai, Tamil Nadu', '9867123456', 'anjali.nair@outlook.com'),  
(7, 'Ravi', 'Patel', '1987-06-25', 'Male', 'Ahmedabad, Gujarat', '9825123456', 'ravi.patel@gmail.com'),  
(8, 'Kiran', 'Yadav', '1991-02-14', 'Female', 'Lucknow, Uttar Pradesh', '9899123456', 'kiran.yadav@yahoo.com'),  
(9, 'Sandeep', 'Mishra', '1989-11-20', 'Male', 'Bhopal, Madhya Pradesh', '9876123456', 'sandeep.mishra@gmail.com'),  
(10, 'Meera', 'Iyer', '1993-08-08', 'Female', 'Hyderabad, Telangana', '9854123456', 'meera.iyer@rediffmail.com');  

INSERT INTO Account (Account_Number, Customer_ID, Account_Type, Balance, Branch_Name) VALUES  
(1001, 1, 'Savings', 50000.00, 'Mumbai Main'),  
(1002, 2, 'Current', 75000.50, 'Delhi South'),  
(1003, 3, 'Savings', 60000.75, 'Kolkata Central'),  
(1004, 4, 'Current', 120000.00, 'Bangalore East'),  
(1005, 5, 'Savings', 45000.25, 'Jaipur West'),  
(1006, 6, 'Current', 90000.00, 'Chennai North'),  
(1007, 7, 'Savings', 30000.00, 'Ahmedabad South'),  
(1008, 8, 'Current', 110000.00, 'Lucknow Central'),  
(1009, 9, 'Savings', 85000.75, 'Bhopal Main'),  
(1010, 10, 'Current', 95000.00, 'Hyderabad West');  


INSERT INTO Transaction (Transaction_ID, Account_Number, Transaction_Type, Amount, Transaction_Date) VALUES  
(1, 1001, 'Deposit', 10000.00, '2024-03-01'),  
(2, 1002, 'Withdrawal', 5000.00, '2024-03-02'),  
(3, 1003, 'Deposit', 15000.50, '2024-03-03'),  
(4, 1004, 'Withdrawal', 20000.00, '2024-03-04'),  
(5, 1005, 'Deposit', 25000.75, '2024-03-05'),  
(6, 1006, 'Withdrawal', 7000.00, '2024-03-06'),  
(7, 1007, 'Deposit', 12000.00, '2024-03-07'),  
(8, 1008, 'Withdrawal', 15000.25, '2024-03-08'),  
(9, 1009, 'Deposit', 20000.50, '2024-03-09'),  
(10, 1010, 'Withdrawal', 30000.00, '2024-03-10');  


INSERT INTO Loan (Loan_ID, Customer_ID, Loan_Type, Loan_Amount, Interest_Rate, Loan_Term, Status) VALUES  
(1, 1, 'Home', 500000.00, 7.5, 15, 'Approved'),  
(2, 2, 'Car', 300000.00, 8.0, 7, 'Approved'),  
(3, 3, 'Personal', 150000.00, 10.0, 5, 'Pending'),  
(4, 4, 'Home', 700000.00, 7.2, 20, 'Approved'),  
(5, 5, 'Car', 250000.00, 7.8, 6, 'Pending'),  
(6, 6, 'Personal', 180000.00, 9.5, 4, 'Approved'),  
(7, 7, 'Home', 550000.00, 7.0, 12, 'Approved'),  
(8, 8, 'Car', 275000.00, 8.2, 5, 'Pending'),  
(9, 9, 'Personal', 220000.00, 9.0, 3, 'Approved'),  
(10, 10, 'Home', 600000.00, 7.3, 18, 'Approved');  


SELECT * FROM Customer;
SELECT * FROM Account;
SELECT * FROM Transaction;
SELECT * FROM Loan;
