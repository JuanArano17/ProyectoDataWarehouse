# Bank Data Warehouse Project

## Table of Contents
- [Introduction](#introduction)
- [Architecture](#architecture)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Data Model](#data-model)
  - [Fact Tables](#fact-tables)
  - [Dimension Tables](#dimension-tables)
- [ETL Process](#etl-process)
- [CUBE Process](#cube-process)
- [Reporting](#reporting)
- [Built With](#built-with)
- [Authors](#authors)
- [License](#license)

## Introduction

The Bank Data Warehouse Project is a comprehensive solution designed to centralize banking data into a single repository, supporting advanced data analytics and reporting capabilities. This repository outlines the process of creating a robust Data Warehouse that consists of two fact tables, a minimum of five dimension tables, and an automated reporting system with dynamic charts (five charts per fact table).

## Architecture

This project adopts a traditional data warehouse architecture, with a focus on scalability and reliability for banking analytics needs. The architecture encompasses:

- Data extraction, transformation, and loading (ETL) processes
- Data storage in SQL Server
- A cube for data analysis
- Automated reporting in Excel

## Features

- **Data Integration:** Consolidates various data sources into a unified data warehouse.
- **Fact Tables:** Two central fact tables for transactional and balance-related analytics.
- **Dimensional Modelling:** At least five dimensions for comprehensive analytical slicing.
- **Automated Reporting:** 10 dynamic Excel charts driven by the data warehouse.
- **OLAP Cube:** SQL Server Analysis Services (SSAS) cube for multi-dimensional analysis.

## Getting Started

Follow these instructions to get your Data Warehouse and reporting system up and running.

### Prerequisites

- SQL Sqerver Developer Edition
- SQL Server Management Studio (SSMS)
- Visual Studio 2022 with SQL Server Data Tools (SSDT)
- Microsoft Excel

### Steps
1. Set Database model in SSMS wit sql script
2. Configure ETL to your XML PATH and DB connection
3. Execute ETL and confirm that the data has been inserted into the data warehouse
4. Repeat step 2 with the CUBE and execute it

## Data Model

### Fact Tables

1. `FactTransactions`: Stores transactional data of the bank.
2. `FactBalances`: Maintains daily balance data for accounts.

### Dimension Tables

- `DimCustomer`: Customer-related attributes.
- `DimAccount`: Account-specific details.
- `DimDate`: Time-related attributes for analysis.
- `DimBranches`: Bank branches details.
- `DimTransactionType`: Defines transaction type descriptions
- `DimProductType`: Defines product type descriptions

## ETL Process

## CUBE Process

## Reporting

Description of the automated reporting system with details on the Excel charts that visualize data from the fact tables.

## Built With

- [SQL Server](https://www.microsoft.com/sql-server) - The database used for data warehousing.
- [SQL Server Integration Services (SSIS)](https://docs.microsoft.com/en-us/sql/integration-services/sql-server-integration-services) - Used for the ETL process.
- [SQL Server Analysis Services (SSAS)](https://docs.microsoft.com/en-us/sql/analysis-services/sql-server-analysis-services) - Used to create the OLAP cube.
- [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) - Used for reporting and data visualization.

## Authors

- **Juan Pablo Arano** - *Programmer - Designer - Tester* - [Juan Arano](https://github.com/JuanArano17)
- **Sofia Alejandra Prieto** - *Designer - Tester - SCRUM master* - [Sofia Prieto](https://github.com/sofipp)

See also the list of [contributors](https://github.com/JuanArano17/BankDataWarehouse/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
