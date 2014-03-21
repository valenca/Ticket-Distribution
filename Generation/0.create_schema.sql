-- -----------------------------------------------------
-- Schema creator
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tms` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `tms` ;

-- -----------------------------------------------------
-- Table `tms`.`tickets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`tickets` (
  `t_id` INT NOT NULL AUTO_INCREMENT,
  `t_type` TEXT NOT NULL,
  `t_person` TEXT NOT NULL,
  `t_date` DATETIME NOT NULL,
  `t_store` TEXT NOT NULL,
  `t_trips` INT NOT NULL,
  PRIMARY KEY (`t_id`),
  UNIQUE INDEX `t_id_UNIQUE` (`t_id` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `tms`.`deposits`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`deposits` (
  `d_id` INT NOT NULL AUTO_INCREMENT,
  `d_t_id` INT NOT NULL,
  `d_date` DATETIME NOT NULL,
  `d_location` TEXT NOT NULL,
  `d_trips` INT NOT NULL,
  `d_value` FLOAT NOT NULL,
  PRIMARY KEY (`d_id`),
  UNIQUE INDEX `d_id_UNIQUE` (`d_id` ASC),
  INDEX `fk_deposits_tickets_idx` (`d_t_id` ASC),
  CONSTRAINT `fk_deposits_tickets`
    FOREIGN KEY (`d_t_id`)
    REFERENCES `tms`.`tickets` (`t_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `tms`.`validations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`validations` (
  `v_id` INT NOT NULL AUTO_INCREMENT,
  `v_t_id` INT NOT NULL,
  `v_date` DATETIME NOT NULL,
  `v_location` TEXT NOT NULL,
  `v_transport` TEXT NOT NULL,
  `v_company` TEXT NOT NULL,
  PRIMARY KEY (`v_id`),
  INDEX `fk_validations_tickets_idx` (`v_t_id` ASC),
  CONSTRAINT `fk_validations_tickets`
    FOREIGN KEY (`v_t_id`)
    REFERENCES `tms`.`tickets` (`t_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- System variables
-- -----------------------------------------------------
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
