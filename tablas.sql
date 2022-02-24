CREATE TABLE provincias(
    provno decimal(4),
    provname varchar(20),
    comunidad_autonoma varchar(20),
    PRIMARY KEY (provno)
);

INSERT INTO provincias VALUES (1,"Sevilla","Andalucía");
INSERT INTO provincias VALUES (2,"Málaga","Andalucía");
INSERT INTO provincias VALUES (3,"Barcelona","Cataluña");
INSERT INTO provincias VALUES (4,"Bilbao","País Vasco");

CREATE TABLE localidades(
    locno decimal(4),
    nombre varchar(40),
    ciudadanos decimal(7),
    cp decimal(5),
    provno decimal(4),
    PRIMARY KEY (locno),
    CONSTRAINT fk_provno
    FOREIGN KEY(provno)
    REFERENCES provincias(provno)
);

INSERT INTO localidades VALUES (1,"Dos Hermanas",100000,41702,1);
INSERT INTO localidades VALUES (2,"Alcalá de Guadaíra",65000,41500,1);
INSERT INTO localidades VALUES (3,"Marbella",141000,29600,2);
INSERT INTO localidades VALUES (4,"Torremolinos",68000,29620,2);
INSERT INTO localidades VALUES (5,"Terrassa",218000,08221,3);
INSERT INTO localidades VALUES (6,"San Sebastián",186000,20001,4);
INSERT INTO localidades VALUES (7,"Santander",172000,39001,4);
