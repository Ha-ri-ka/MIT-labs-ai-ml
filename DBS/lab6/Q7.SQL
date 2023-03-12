set SERVEROUTPUT on;
DECLARE
    g studenttable.GPA%type;
BEGIN
    for i in 1..5 loop
    select GPA into g from studenttable where rollno=i;
    if g>=0 and g<=4 then
		goto GRF;
	ELSIF g>4 and g<=5 then
		goto GRE;
	ELSIF g>5 and g<=6 then
		goto GRD;
	ELSIF g>6 and g<=7 then
		goto GRC;
	ELSIF g>7 and g<=8 then
		goto GRB;
	ELSIF g>8 and g<=9 then
		goto GRA;
	ELSIF g>9 and g<=10 then
		goto GRAA;
	ELSE
		dbms_output.put_line('student has invalid gpa');
	end if;
    end loop;
    <<GRF>>
    dbms_output.put_line('F GRADE');
    <<GRE>>
    dbms_output.put_line('E GRADE');
    <<GRD>>
    dbms_output.put_line('D GRADE');
    <<GRC>>
    dbms_output.put_line('C GRADE');
    <<GRB>>
    dbms_output.put_line('B GRADE');
    <<GRA>>
    dbms_output.put_line('A GRADE');
    <<GRAA>>
    dbms_output.put_line('A+ GRADE');
    END;
    /

