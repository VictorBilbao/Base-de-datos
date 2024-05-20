-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 20-05-2024 a las 03:23:32
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `100`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Almacen`
--

CREATE TABLE `Almacen` (
  `Codigo_almacen` int(11) NOT NULL,
  `Sector` varchar(255) NOT NULL,
  `Contenedor` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Herramienta`
--

CREATE TABLE `Herramienta` (
  `Codigo_herramienta` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Marca` text DEFAULT NULL,
  `Estado` varchar(50) NOT NULL DEFAULT 'Disponible',
  `Codigo_almacen` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Responsable`
--

CREATE TABLE `Responsable` (
  `Cedula_responsable` int(11) NOT NULL,
  `Nombre_completo` varchar(255) NOT NULL,
  `Telefono` varchar(20) DEFAULT NULL,
  `Correo` varchar(100) DEFAULT NULL,
  `Fecha_Entrega` date NOT NULL,
  `Fecha_Devolucion` date NOT NULL,
  `Codigo_herramienta` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Almacen`
--
ALTER TABLE `Almacen`
  ADD PRIMARY KEY (`Codigo_almacen`);

--
-- Indices de la tabla `Herramienta`
--
ALTER TABLE `Herramienta`
  ADD PRIMARY KEY (`Codigo_herramienta`),
  ADD KEY `FK_Herramienta_Almacen` (`Codigo_almacen`);

--
-- Indices de la tabla `Responsable`
--
ALTER TABLE `Responsable`
  ADD PRIMARY KEY (`Cedula_responsable`),
  ADD KEY `FK_Herramienta_Responsable` (`Codigo_herramienta`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Almacen`
--
ALTER TABLE `Almacen`
  MODIFY `Codigo_almacen` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Herramienta`
--
ALTER TABLE `Herramienta`
  MODIFY `Codigo_herramienta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Responsable`
--
ALTER TABLE `Responsable`
  MODIFY `Cedula_responsable` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Herramienta`
--
ALTER TABLE `Herramienta`
  ADD CONSTRAINT `FK_Herramienta_Almacen` FOREIGN KEY (`Codigo_almacen`) REFERENCES `Almacen` (`Codigo_almacen`);

--
-- Filtros para la tabla `Responsable`
--
ALTER TABLE `Responsable`
  ADD CONSTRAINT `FK_Herramienta_Responsable` FOREIGN KEY (`Codigo_herramienta`) REFERENCES `Herramienta` (`Codigo_herramienta`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
