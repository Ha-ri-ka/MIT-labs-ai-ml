8. coming soon

9. select name,dept_name from student;

10.  select name from instructor
     where dept_name='Comp. Sci.';

11. select title from course where credits=3 and dept_name='Comp. Sci.';

12.select course.course_ID,course.title from course 
join takes on course.course_id=takes.course_id where takes.id=12345;

13. select * from instructor where salary between 40000 and 90000;

14. select id,name from instructor where ID not in (select id from teaches);

15. coming soon

16. select student.name,takes.course_id from student
    join takes on student.id=takes.id where takes.year=2010;

17.  select * from instructor where
     salary > any (select salary from instructor where dept_name='Comp. Sci.');

18. select name from instructor where dept_name like '%si%';

19. select name, length(name) len from student;

20.  select substr(dept_name,3,3) from department ;

21. select UPPER(name)name from instructor;

22. coming soon

23. select salary,ROUND(salary/3) from instructor;

24. update EMPLOYEE set DOB='20-sep-2003' where emp_name='Harika';
	  select TO_DATE(DOB,'DD-MON-YYYY') from employee;

25. select emp_name,TO_CHAR(DOB,'YEAR') from employee;
	  select emp_name,initcap(TO_CHAR(DOB,'YEAR')) from employee;
	  select emp_name,LOWER(TO_CHAR(DOB,'YEAR')) from employee;

26. select to_char(DOB,'DAY') from employee;

27.select to_char(DOB,'month') from employee;

28.select LAST_DAY(DOB),to_char(LAST_DAY(DOB),'DAY') from employee;

29. select round((sysdate-to_date(DOB))/365,-1)as age from employee;
