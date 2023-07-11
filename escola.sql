CREATE DATABASE escola;
USE escola;
CREATE TABLE usuario(
codigo INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
senha VARCHAR(100) NOT NULL,
acesso INT);


INSERT INTO usuario VALUES 
(1, "Abel", MD5("legal"), 1);

INSERT INTO usuario VALUES
(2, "Ana", MD5("bolo"), 2);

INSERT INTO usuario VALUES
(3, "Maeldson", MD5("onepiece"), 3);