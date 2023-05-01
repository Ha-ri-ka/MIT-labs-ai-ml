create table salary_raise(inst_id varchar(5),raise_date date,raise_amnt numeric(8,2),foreign key (inst_id) references instructor(id));
--potentially wrong,please note.
SET SERVEROUTPUT ON;
DECLARE
    cursor instsal(dname instructor.dept_name%type) is select * from instructor where dept_name=dname for update;
    raisedate date;
    prevsal instructor.salary%type;
BEGIN
    for rw in instsal('Comp. Sci.') LOOP
    raisedate:=sysdate;
    prevsal:=rw.salary;
    update instructor set salary=salary*1.05 where current of instsal;
    insert into salary_raise values(rw.id,raisedate,rw.salary*0.05);
    END LOOP;
END;
/
