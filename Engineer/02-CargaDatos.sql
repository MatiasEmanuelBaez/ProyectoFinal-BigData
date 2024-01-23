use proyecto_final;

#################### CARGA DE ESTADOS
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.2\\Uploads\\estados.csv'
REPLACE INTO TABLE estados
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

#################### CARGA DE PLATAFORMAS
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.2\\Uploads\\plataformas.csv'
IGNORE INTO TABLE plataformas
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

#################### CARGA DE USUARIOS
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.2\\Uploads\\usuarios.csv'
REPLACE INTO TABLE usuarios
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id_usuario, id_plataforma, identificador_usuario, nombre, reviews_count, @fans_count, @avg_stars, @compliment_count, @cool_count, @funny_count);

#################### CARGA DE CIUDADES
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.2\\Uploads\\ciudades.csv'
IGNORE INTO TABLE ciudades
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

#################### CARGA DE RESTAURANTES
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.2\\Uploads\\restaurantes.csv'
REPLACE INTO TABLE restaurantes
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

#################### CARGA DE CATEGORIAS
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.2\\Uploads\\categorias.csv'
IGNORE INTO TABLE categorias
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

#################### CARGA DE CATEGORIASRESTAURANTES
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.2\\Uploads\\categoriasrestaurantes.csv'
IGNORE INTO TABLE categoriasrestaurantes
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

#################### CARGA DE REVIEWS
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.2\\Uploads\\reviews.csv'
IGNORE INTO TABLE reviews
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

#################### CARGA DE CONSEJOS
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.2\\Uploads\\consejos.csv'
IGNORE INTO TABLE consejos
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

