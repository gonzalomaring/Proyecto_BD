CREATE TABLE departamentos(
    deptno decimal(11),
    dname varchar(20),
    localizacion varchar(20),
    PRIMARY KEY (deptno)
);

INSERT INTO departamentos VALUES (1,"Marketing","Dos Hermanas");
INSERT INTO departamentos VALUES (2,"Contabilidad","Alcalá de Guadaíra");
INSERT INTO departamentos VALUES (3,"Recursos humanos","Madrid");
INSERT INTO departamentos VALUES (4,"Compras","Dos Hermanas");

CREATE TABLE empleados(
    empno decimal(11),
    nombre varchar(20),
    puesto varchar(20),
    ano_alta varchar(4),
    salario decimal(11),
    deptno decimal(11),
    PRIMARY KEY (empno),
    CONSTRAINT fk_dpto
    FOREIGN KEY(deptno)
    REFERENCES departamentos(deptno)
);

INSERT INTO empleados VALUES (1,"Francisco","Editor","2018","1200",1);
INSERT INTO empleados VALUES (2,"Manuel","Encargado","2010","1800",1);
INSERT INTO empleados VALUES (3,"Gonzalo","Contable","2017","1100",2);
INSERT INTO empleados VALUES (4,"Alfonso","Contable","2022","1100",2);
INSERT INTO empleados VALUES (5,"Fabio","Encargado","2021","1900",3);
INSERT INTO empleados VALUES (6,"Fernando","Gerente","2010","2100",4);
INSERT INTO empleados VALUES (7,"Felipe","Secretario","2018","1100",4);
