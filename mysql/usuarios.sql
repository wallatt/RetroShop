-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema usuarios
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema usuarios
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `usuarios` DEFAULT CHARACTER SET utf8 ;
USE `usuarios` ;

-- -----------------------------------------------------
-- Table `mydb`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `usuarios`.`usuario` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `dni` INT NULL,
  `mail` VARCHAR(45) NULL,
  `username` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `usuarios`.`sesion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `usuarios`.`sesion` (
  `idsesion` INT NOT NULL,
  `iniciosesion` DATETIME NULL,
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`idsesion`, `usuario_id`),
  INDEX `fk_sesion_usuario_idx` (`usuario_id` ASC),
  CONSTRAINT `fk_sesion_usuario`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `usuarios`.`usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
