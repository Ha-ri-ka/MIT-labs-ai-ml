1. select BDATE,address from employee where fname='John' and minit='B' and lname='Smith';

2. select Pnumber,Dnum,lname,address,Bdate from project,employee where plocation='Starfford' 
   and Ssn=(select mgr_ssn from dept where dnumber=(select dnum from project where plocation='Starfford'));
   
3. select distinct(salary) from employee;
  
4. create view super(fn,ln,id) as select fname,lname,Ssn from employee;
    select fname,lname,fn,ln from employee,super where Super_ssn=id;

5. create view emps (id,lname) as select Ssn,lname from employee where Ssn in (select Essn from works_on);  --all employees that work on SOME project
   select Pno from works_on where Essn in (select id from emps where lname='Smith');

6. select fname,lname from employee where address like '%Houston%';

7. select fname,lname,salary as oldsal,salary*(1.1) as newsal from employee where Ssn in (select Essn from works_on where Pno=(select Pnumber from project where Pname='ProductX'));

8. select fname,minit,lname from employee where dno=5 and salary between 30000 and 40000;

9. coming soon.

10. select fname,lname from employee where super_ssn is null;

11. select fname,lname from employee join dependent on Ssn=Essn where fname=Dependent_name and employee.Sex=Dependent.Sex;

12. select fname,minit,lname from employee where Ssn not in (Select Essn from dependent);

13. create view mgr (mid) as select Mgr_ssn from dept;
    select fname,minit,lname from employee where Ssn in (select mid from mgr) and Ssn in (select Essn from dependent);
 
14. select distinct(Essn) from works_on where Pno in (1,2,3);

15. select sum(salary) as sal_sum,max(salary) as sal_max,min(salary) as sal_min,avg(salary) as sal_avg from employee;

16. select sum(salary) as sal_sum,max(salary) as sal_max,min(salary) as sal_min,avg(salary) as sal_avg from employee where Dno=(select Dnumber from dept where Dname='Research');

17. create view emp_count(projNo,numberOfEmployees) as select pno,count(distinct(Essn)) from works_on group by pno;
    select Pname,projNo,numberOfEmployees from Project,emp_count where Pnumber=projNo;

18. select Pname,projNo,numberOfEmployees from Project,emp_count where Pnumber=projNo and numberOfEmployees>2;

19. create view empNo(dno,empn) as select Dno,count(*) from employee group by Dno having count(*)>4;
    create view emp40(dno,emp40c) as select dno,count(*) from employee where dno in (select dno from empno) and salary>40000 group by dno;
     select emp40.dno,empn,emp40c from emp40 join empno on emp40.dno=empno.dno;
