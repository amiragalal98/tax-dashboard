CREATE TABLE IF NOT EXISTS taxes
( 
    id INT AUTO_INCREMENT PRIMARY KEY,
    taxpayer VARCHAR(255),
    tax_paid FLOAT
);
INSERT INTO taxes (taxpayer, tax_paid) VALUES
('Alice', 1500.00),
('Bob', 2000.00),
('Charlie', 2500.00);