-- Active: 1682690935689@@database-1.csjkcoguajzu.us-west-2.rds.amazonaws.com@3306@db_luminis


CREATE TABLE tb_blog (
  blog_id INT(11) NOT NULL AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  sub_title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  image VARCHAR(255) NOT NULL,
  author VARCHAR(255) NOT NULL,
  active INT(1) NOT NULL,
  category VARCHAR(255) NOT NULL,
  registration_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (blog_id)
);

CREATE TABLE tb_question (
  question_id INT(11) NOT NULL AUTO_INCREMENT,
  question TEXT NOT NULL,
  question_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  active INT(1) NOT NULL,
  blog_id INT(11) NOT NULL,
  PRIMARY KEY (question_id),
  FOREIGN KEY (blog_id) REFERENCES tb_blog(blog_id)
);

CREATE TABLE tb_answer (
  answer_id INT(11) NOT NULL AUTO_INCREMENT,
  answer TEXT NOT NULL,
  answer_timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  active INT(1) NOT NULL,
  question_id INT(11) NOT NULL,
  PRIMARY KEY (answer_id),
  FOREIGN KEY (question_id) REFERENCES tb_question(question_id)
);

-- ROLES
CREATE TABLE tb_role (
  id INT(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description VARCHAR(255) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- PROFILE PHOTO
CREATE TABLE tb_profile_photo (
  id INT(11) NOT NULL AUTO_INCREMENT,
  photo_name VARCHAR(255) NOT NULL,
  photo_url text NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- USERS
CREATE TABLE tb_user (
  id INT(11) NOT NULL AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  midlename VARCHAR(255) NOT NULL,
  lastname VARCHAR(255) NOT NULL,
  birthdate DATE NOT NULL,
  phone VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  old_password VARCHAR(255) NOT NULL,
  is_activate INT(1) NOT NULL DEFAULT 1,
  role_id INT(11) NOT NULL,
  photo_id INT(11) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (role_id) REFERENCES tb_role(id),
  FOREIGN KEY (photo_id) REFERENCES tb_profile_photo(id)
);


--delete table profile photo
DROP TABLE tb_profile_photo;
--eliminar la coLUMNA USER ID DE LA TABLA PROFILE PHOTO
ALTER TABLE tb_profile_photo DROP COLUMN user_id;
--Delete table users
DROP TABLE tb_user;
--adicional la columna is_activate y que por defecto sea 1, dentro de la tabla tb_profile_photo y que este despues del photo_url
ALTER TABLE tb_profile_photo ADD is_activate INT(1) NOT NULL DEFAULT 1 AFTER photo_url;