SET SERVEROUTPUT ON;
DECLARE
	roll StudentTable.ROLLNO%Type;
	g StudentTable.GPA%Type;
BEGIN

	roll:= &r;	
	select GPA into g from StudentTable where ROLLNO=roll;
	if g=NULL then
		RAISE NO_DATA_FOUND;
		
	else
	dbms_output.put_line('gpa is '|| g);
	if g>=0 and g<=4 then
		dbms_output.put_line('F GRADE');
	ELSIF g>4 and g<=5 then
		dbms_output.put_line('E GRADE');
	ELSIF g>5 and g<=6 then
		dbms_output.put_line('D GRADE');
	ELSIF g>6 and g<=7 then
		dbms_output.put_line('C GRADE');
	ELSIF g>7 and g<=8 then
		dbms_output.put_line('B GRADE');
	ELSIF g>8 and g<=9 then
		dbms_output.put_line('A GRADE');
	ELSIF g>9 and g<=10 then
		dbms_output.put_line('A+ GRADE');
	ELSE
		dbms_output.put_line('student has invalid gpa');
	end if;
END IF;

EXCEPTION
	when NO_DATA_FOUND then
		dbms_output.put_line('roll number doesnt exist');
END;
/	