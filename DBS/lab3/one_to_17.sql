1.select course_id from takes where semester='Fall' and year=2009 UNION select course_id from takes where semester='Spring' and year=2010;

2.select course_id from takes where semester='Fall' and year=2009 INTERSECT select course_id from takes where semester='Spring' and year=2010; 

3.select course_id from takes where semester='Fall' and year=2009 MINUS select course_id from takes where semester='Spring' and year=2010;

4.select course.title,course.course_id from course where course.course_id not in (select takes.course_id from takes); 

5. select course_id from takes where semester='Fall' and year='2009'and course_id in (select course_id from takes where semester='Spring' and year='2010');

6.select count(ID) as count from takes where course_id in (select course_id from teaches where id=10101); 

7. select course_id from takes where semester in ('Fall') and year in ('2009') and semester not in ('Spring') and year not in (2010);

8.select name from student where name in (select name from instructor); 

9.select name from instructor where salary > some (select salary from instructor where dept_name='Biology');

10.select name from instructor where salary >all (select salary from instructor where dept_name='Biology'); 

11. select dept_name,avg(salary) from instructor group by dept_name having avg(salary)>= all (select avg(salary) from instructor group by dept_name); 

12. select dept_name from department where budget < all(select avg(salary) from instructor); 

13. SELECT course_id FROM section S1 WHERE semester = 'Fall' AND year = 2009 AND EXISTS
    (SELECT course_id FROM section S2 WHERE semester = 'Spring' and year = 2010 and S1.course_id=S2.course_id);
    
14.SELECT DISTINCT S.ID, S.name FROM student S WHERE NOT EXISTS((SELECT course_id FROM course WHERE dept_name = 'Biology') 
EXCEPT(SELECT T.course_id FROM takes T WHERE S.ID = T.ID));

15.SELECT course.course_id from course WHERE UNIQUE(SELECT section.course_id FROM section WHERE course.course_id = section.course_id AND section.year = 2009);

16.SELECT takes.ID FROM takes WHERE 1<(SELECT COUNT(course.course_id) FROM course WHERE course.course_id = takes.course_id AND course.dept_name = 'Comp. Sci')

17.SELECT dept_name, avg_salary FROM (SELECT dept_name, AVG(salary) avg_salary FROM instructor GROUP BY dept_name) WHERE avg_salary > 42000;
