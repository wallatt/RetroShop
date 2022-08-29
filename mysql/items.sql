-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema items
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema items
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `items` DEFAULT CHARACTER SET utf8 ;
USE `items` ;

-- -----------------------------------------------------
-- Table `items`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `items`.`categoria` (
  `idcategoria` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idcategoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `items`.`seller`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `items`.`seller` (
  `id` INT NOT NULL,
  `vendedor_id` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `items`.`itemsventa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `items`.`itemsventa` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `descripcion` VARCHAR(150) NULL,
  `precio` DOUBLE NULL,
  `cantidad` INT NULL,
  `fecha_fabricacion` DATETIME NULL,
  `categoria_idcategoria` INT NOT NULL,
  `seller_id` INT NOT NULL,
  PRIMARY KEY (`id`, `categoria_idcategoria`, `seller_id`),
  INDEX `fk_itemsventa_categoria_idx` (`categoria_idcategoria` ASC) ,
  INDEX `fk_itemsventa_seller1_idx` (`seller_id` ASC) ,
  CONSTRAINT `fk_itemsventa_categoria`
    FOREIGN KEY (`categoria_idcategoria`)
    REFERENCES `items`.`categoria` (`idcategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_itemsventa_seller1`
    FOREIGN KEY (`seller_id`)
    REFERENCES `items`.`seller` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `items`.`buyer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `items`.`buyer` (
  `id` INT NOT NULL,
  `id_comprador` INT NULL,
  `cantidad` INT NULL,
  `itemsventa_id` INT NOT NULL,
  PRIMARY KEY (`id`, `itemsventa_id`),
  INDEX `fk_buyer_itemsventa1_idx` (`itemsventa_id` ASC) ,
  CONSTRAINT `fk_buyer_itemsventa1`
    FOREIGN KEY (`itemsventa_id`)
    REFERENCES `items`.`itemsventa` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `items`.`fotos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `items`.`fotos` (
  `id` INT NOT NULL,
  `ruta` VARCHAR(100) NULL,
  `itemsventa_id` INT NOT NULL,
  PRIMARY KEY (`id`, `itemsventa_id`),
  INDEX `fk_fotos_itemsventa1_idx` (`itemsventa_id` ASC) ,
  CONSTRAINT `fk_fotos_itemsventa1`
    FOREIGN KEY (`itemsventa_id`)
    REFERENCES `items`.`itemsventa` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
