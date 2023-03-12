set SERVEROUTPUT on;
DECLARE
	issue DATE;
	ret DATE;
	d numeric(2);
    fine numeric(5,2);
BEGIN
	issue:= '&i';
	ret:= '&r';
	d:=ret-issue;
	if d<=7 then
		dbms_output.put_line('no fine!');
	elsif d>=8 and d<=15 then
        dbms_output.put_line('fine amount:'||d);
    elsif d>=16 and d<=30 then
        fine:=d*2;
        dbms_output.put_line('fine amount:'||fine);
    elsif d>30 then
        fine:=d*5;
        dbms_output.put_line('fine amount:'||fine);
    end if;
END;
/