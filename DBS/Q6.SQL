set SERVEROUTPUT on;
    DECLARE
        g studenttable.GPA%type;
        mx studenttable.GPA%type;
    BEGIN
        select gpa into mx from studenttable where rollno=1;
        for i in 2..5 loop            
            select gpa into g from studenttable where rollno=i;
            if g>mx then
            mx:=g;
            end if;
        end loop;        
        dbms_output.put_line('max gpa is:'||mx);
    END;
    /

