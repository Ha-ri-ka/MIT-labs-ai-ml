create table Doctor
(
DID numeriC(3),
dname varchar(10),
dept varchar(15),
salary numeric(10) DEFAULT 10000,
PRIMARY KEY (DID));


create table Patient
(
PID numeric(4),
name varchar(10),
gender char(1),
blood_group varchar(3),
DID numeric(3),
PRIMARY KEY (PID),
CHECK (GENDER IN ('M','F','O')),
FOREIGN KEY (DID) REFERENCES Doctor(DID));

insert into Doctor values(405,'Anish','Optometry',35000);
insert into Doctor values(407,'Jyeshta','Optometry',60000);
insert into Doctor values(411,'Rehman','Neurology',80000);
insert into Doctor values(419,'Ketan','Ortho',60000);

insert into Patient values(2298,'Pranshu','M','O+',405);
insert into Patient values(2299,'Vaidehi','F','A+',407);
insert into Patient values(2301,'Virat','M','AB+',419);
insert into Patient values(2302,'Shri','F','O-',411);

select PID,name from Patient where blood_group='O+' or blood_group='O-';

select DNAME,salary from Doctor where salary=(select max(salary) from Doctor);
