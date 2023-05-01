SET SERVEROUTPUT ON;
DECLARE
    CURSOR StuCred is select name,tot_cred from student order by tot_cred;
BEGIN
    for stu in StuCred LOOP
    exit when StuCred%ROWCOUNT>10;
    dbms_output.put_line('name:'||stu.name||'-----credits:'||stu.tot_cred);
    END LOOP;
END;
/
