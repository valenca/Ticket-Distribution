-- -----------------------------------------------------
-- Schema creator
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tms` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `tms` ;

-- -----------------------------------------------------
-- Table `tms`.`tickets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`tickets` (
  `ticket_id` INT NOT NULL AUTO_INCREMENT,
  `person` TEXT NOT NULL,
  `date` DATETIME NOT NULL,
  `store` TEXT NOT NULL,
  `trips` INT NOT NULL,
  `comment` TEXT NOT NULL,
  PRIMARY KEY (`ticket_id`),
  UNIQUE INDEX `ticket_id_UNIQUE` (`ticket_id` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `tms`.`deposits`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`deposits` (
  `deposit_id` INT NOT NULL AUTO_INCREMENT,
  `ticket_id` INT NOT NULL,
  `date` DATETIME NOT NULL,
  `location` TEXT NOT NULL,
  `trips` INT NOT NULL,
  `value` FLOAT NOT NULL,
  PRIMARY KEY (`deposit_id`),
  UNIQUE INDEX `idDeposits_UNIQUE` (`deposit_id` ASC),
  INDEX `fk_Deposits_Tickets_idx` (`ticket_id` ASC),
  CONSTRAINT `fk_Deposits_Tickets`
    FOREIGN KEY (`ticket_id`)
    REFERENCES `tms`.`tickets` (`ticket_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `tms`.`validations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tms`.`validations` (
  `validation_id` INT NOT NULL AUTO_INCREMENT,
  `ticket_id` INT NOT NULL,
  `date` DATETIME NOT NULL,
  `location` TEXT NOT NULL,
  `transport` TEXT NOT NULL,
  PRIMARY KEY (`validation_id`),
  INDEX `fk_Validations_Tickets1_idx` (`ticket_id` ASC),
  CONSTRAINT `fk_Validations_Tickets1`
    FOREIGN KEY (`ticket_id`)
    REFERENCES `tms`.`tickets` (`ticket_id`)
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
