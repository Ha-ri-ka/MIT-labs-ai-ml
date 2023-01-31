create table EMPLOYEE(
emp_no numeric(5),
emp_name varchar(10),
emp_address varchar(20) );

insert into EMPLOYEE values(21096,'harika','manipal');
insert into EMPLOYEE values(21097,'name1','udupi');
insert into EMPLOYEE values(21098,'name2','mangalore');
insert into EMPLOYEE values(21099,'name3','bangalore');
insert into EMPLOYEE values(21090,'name4','hyderabad');

select emp_name from EMPLOYEE;
select emp_name,emp_no from EMPLOYEE where emp_address='manipal';

alter table EMPLOYEE add(salary numeric(10));

update EMPLOYEE set salary=1500 where emp_name='harika';
update EMPLOYEE set salary=100000 where emp_name='name1';
update EMPLOYEE set salary=150000 where emp_name='name2';
update EMPLOYEE set salary=80000 where emp_name='name3';
update EMPLOYEE set salary=10000 where emp_name='name4';

desc EMPLOYEE;
delete from EMPLOYEE where emp_addree='mangalore';

rename EMPLOYEE to EMPLOYEE1;

drop table EMPLOYEE1;
