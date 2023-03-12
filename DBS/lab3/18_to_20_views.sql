18)create view all_courses as
    select course_id,sec_id,building,room_number from section
    where course_id in (select course_id from course where dept_name='Comp. Sci.')
    and semester='Fall' and year=2009;

19)select all_courses.course_id,course.title from all_courses join course on all_courses.course_id=course.course_id;

20) create view department_total_salary (department_name,total) as
  	 select dept_name,sum(salary) from instructor group by dept_name;
