L3_18)create view all_courses as
    select course_id,sec_id,building,room_number from section
    where course_id in (select course_id from course where dept_name='Comp. Sci.')
    and semester='Fall' and year=2009;

L3_19)select all_courses.course_id,course.title from all_courses join course on 	all_courses.course_id=course.course_id;

L3_20) create view department_total_salary (department_name,total) as
  	 select dept_name,sum(salary) from instructor group by dept_name;

1) select course_id,count(ID) from takes group by course_id;

2) create view COUNT_OF_STUDENTS (d,c) as
   select dept_name,count(ID) from takes join course on course.course_id=takes.course_id group by       dept_name;

select d,c from count_of_students where c>10;

3) select dept_name,count(course_id) from course group by dept_name;
 
4) select dept_name,avg(salary) from instructor group by dept_name having avg(salary)>42000;

5)select sec_id,count(id) from takes where semester='Spring' and year=2009 group by sec_id;

6)select course_id from prereq order by course_id;

7)select id,name,dept_name,salary from instructor
  order by salary desc;

8) select dept_name,sum(salary) from instructor group by dept_name having sum(salary)=(select    max(sum(salary)) from instructor group by dept_name);

9)

10)select count(distinct(id)),sec_id from takes where semester='Spring' and year=2010 
	group by sec_id having count(distinct(id))=(select max(count(distinct(id))) from takes 	where semester='Spring' and year=2010 group by sec_id);

11) SELECT DISTINCT name FROM teaches, instructor WHERE teaches.id = instructor.id AND course_id IN (SELECT DISTINCT course_id FROM takes,student WHERE dept_name='Comp. Sci.' AND student.id = takes.id);

12)select avg(salary) from instructor group by dept_name having avg(salary)>50000 and 	dept_name=(select dept_name from instructor group by dept_name having 	count(distinct(id))>2);

13)

14)

17)

18)
