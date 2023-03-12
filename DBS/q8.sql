SET SERVEROUTPUT ON;
DECLARE
    nme instructor.name%type;
    ident instructor.id%type;
    dname instructor.dept_name%type;
BEGIN
    nme:= '&proff_name';
    select ID,dept_name into ident,dname FROM instructor where NAME=nme;
     dbms_output.put_line('name:'||nme||',id:'||ident||',department:'||dname);
     EXCEPTION
     WHEN TOO_MANY_ROWS then
     dbms_output.put_line('multiple instructors have the same name');
     WHEN NO_DATA_FOUND then
     dbms_output.put_line('instructor with entered name doesnt exist.');
     END;
     /
