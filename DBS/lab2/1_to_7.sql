create table EMPLOYEE
   (
    emp_no numeric(10),
    emp_name varchar(10),
    gender char(1) not null,
    salary numeric(10,3) not null,
    address varchar(20) not null,
    d_no numeric(5),
    CONSTRAINT emp_pk PRIMARY KEY (emp_no),
    CHECK (gender in ('M','F'))
);

create table DEPARTMENT
(
 dept_no numeric(5),
dept_name varchar(10),
loc varchar(10),
PRIMARY KEY (dept_no),
UNIQUE (dept_name)
);

alter table EMPLOYEE add (CONSTRAINT dno_fk FOREIGN KEY(d_no) references DEPARTMENT(dept_no));

insert into EMPLOYEE values(210960,'Harika','F',1500,'indralli',2201);
insert into EMPLOYEE values(210961,'name1','F',1500,'manipal',2202);
insert into EMPLOYEE values(210963,'name2','M',1600,'bangalore',2203);
insert into EMPLOYEE values(210964,'name3','F',1700,'delhi',2201);

insert into DEPARTMENT values(2201,'CSE','AB5');
insert into DEPARTMENT values(2202,'ITC','AB3');
insert into DEPARTMENT values(2203,'CIVIL','AB1');

insert into EMPLOYEE values(210964,'name3','t',1600,'bangalore',2203);
insert into EMPLOYEE values(210965,'name4','t',null,'mangalore',2205);
insert into EMPLOYEE values(210961,'name5','M',1700,'vijayawada',2207);

insert into DEPARTMENT values(2201,'IT','AB5');
insert into DEPARTMENT values(2204,'CSE','AB5');


delete from DEPARTMENT where dept_no=2201;

alter table EMPLOYEE drop CONSTRAINT dno_fk;

alter table EMPLOYEE add (CONSTRAINT dno_fk FOREIGN KEY(d_no) references DEPARTMENT(dept_no) on delete cascade);

alter table EMPLOYEE modify(CONSTRAINT salary_ck salary DEFAULT 10000);

insert into EMPLOYEE values(210965,'name4','F',null,'delhi',2201);



