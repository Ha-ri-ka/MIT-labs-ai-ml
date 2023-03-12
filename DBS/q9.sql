SET SERVEROUTPUT ON;
declare
invalid_gpa EXCEPTION;
score numeric(2,1);
grade varchar(2);
i integer:=1;
begin
while i<=5 loop
 select gpa into score from studenttable where ROLLNO=i;
 if score<=4 then
 grade:='F';
 elsif score<=5 then
grade:='E';
elsif score<=6 then
grade:='D';
elsif score<=7 then
grade:='C';
elsif score<=8 then
grade:='B';
elsif score<=9 then
grade:='A';
elsif score<=10 then
grade:='A+';
else
RAISE invalid_gpa;
end if;
update studenttable set lettergrade=grade where rollno=i;
i:=i+1;
end loop;
EXCEPTION when invalid_gpa then
dbms_output.put_line('student has invalid gpa in record');
end;
/