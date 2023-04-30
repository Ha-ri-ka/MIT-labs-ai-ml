1. select BDATE,address from employee where fname='John' and minit='B' and lname='Smith';

2. select Pnumber,Dnum,lname,address,Bdate from project,employee where plocation='Starfford' 
   and Ssn=(select mgr_ssn from dept where dnumber=(select dnum from project where plocation='Starfford'));
