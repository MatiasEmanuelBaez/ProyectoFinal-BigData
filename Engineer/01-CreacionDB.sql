CREATE database proyecto_final;
USE proyecto_final;


CREATE TABLE IF NOT EXISTS estados (
    id_estado int,
    
	estado varchar (50),
	avg_pop float,
	avg_pop_growth float,
	per_capita_income float,
    
    primary key (id_estado)
);

CREATE TABLE IF NOT EXISTS plataformas (
    id_plataforma int,
	plataforma varchar (25),
    
    primary key (id_plataforma)
);

CREATE TABLE IF NOT EXISTS usuarios (
	id_usuario bigint,
    id_plataforma int,
    
    identificador_usuario varchar (100),
	nombre varchar (200),
	reviews_count int,
    fans_count int,
	avg_stars float,
    
    compliment_count int,
    cool_count int,
    funny_count int,
	
    primary key (id_usuario),
	foreign key (id_plataforma) references plataformas(id_plataforma)
);


CREATE TABLE IF NOT EXISTS ciudades (
	id_ciudad int,
    id_estado int,
    
	ciudad varchar (50),
    
    primary key (id_ciudad),
    foreign key (id_estado) references estados(id_estado)
);


CREATE TABLE IF NOT EXISTS restaurantes (
	id_restaurante int,
    id_ciudad int,
    
	identificador_yelp varchar (50),
    identificador_google varchar (50),
	nombre varchar (200),
    direccion varchar (150),
	latitud float,
    longitud float,
    avg_rating float,
	reviews_count int,
    estado varchar(50),
    
    primary key (id_restaurante),
    foreign key (id_ciudad) references ciudades(id_ciudad)
);


CREATE TABLE IF NOT EXISTS categorias (
    id_categoria int,
	categoria varchar (50),
    
    primary key (id_categoria)
);


CREATE TABLE IF NOT EXISTS servicios (
    id_servicio int,
	servicio varchar (50),
    
    primary key (id_servicio)
);


CREATE TABLE IF NOT EXISTS categoriasrestaurantes (
    id_categoria_restaurante int,
    id_categoria int,
    id_restaurante int,
    
    primary key (id_categoria_restaurante),
    foreign key (id_categoria) references categorias(id_categoria),
	foreign key (id_restaurante) references restaurantes(id_restaurante)
);


CREATE TABLE IF NOT EXISTS serviciosrestaurantes (
    id_servicio_restaurante int,
	id_servicio int,
    id_restaurante int,
    
    primary key (id_servicio_restaurante),
	foreign key (id_servicio) references servicios(id_servicio),
    foreign key (id_restaurante) references restaurantes(id_restaurante)
);


CREATE TABLE IF NOT EXISTS reviews (
    id_review bigint,
	id_restaurante int,
    id_usuario bigint,
    
    identificador_plataforma varchar (50),
	raiting float,
	review varchar (500),
    fecha_hora datetime,
	useful int,
    funny int,
    cool int,    
    
    primary key (id_review),
	foreign key (id_restaurante) references restaurantes(id_restaurante),
    foreign key (id_usuario) references usuarios(id_usuario)    
);


CREATE TABLE IF NOT EXISTS consejos (
    id_consejo bigint,
	id_restaurante int,
    id_usuario bigint,
    
	consejo varchar (500),
    fecha datetime,
    compliment_count int,
    
    primary key (id_consejo),
	foreign key (id_restaurante) references restaurantes(id_restaurante),
    foreign key (id_usuario) references usuarios(id_usuario)
);