# Bank Data Warehouse Project

## Table of Contents
- [Introduction](#introduction)
- [Architecture](#architecture)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Data Model](#data-model)
  - [Fact Tables](#fact-tables)
  - [Dimension Tables](#dimension-tables)
- [ETL Process](#etl-process)
- [Reporting](#reporting)
- [Built With](#built-with)
- [Contributing](#contributing)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

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

- SQL Server Management Studio (SSMS)
- Visual Studio 2022 with SQL Server Data Tools (SSDT)
- Microsoft Excel

### Installation

Detailed steps to initialize the database and deploy the solution:

```
Provide code blocks for the setup procedures and commands
```

## Data Model

### Fact Tables

1. `FactTransactions`: Stores transactional data of the bank.
2. `FactBalances`: Maintains daily balance data for accounts.

### Dimension Tables

- `DimCustomers`: Customer-related attributes.
- `DimAccounts`: Account-specific details.
- `DimTime`: Time-related attributes for analysis.
- `DimBranches`: Bank branches details.
- `DimEmployees`: Employee attributes relevant to transactions and balances.

## ETL Process

Outline of the ETL process designed for data extraction from source systems, data cleansing, transformation, and loading into the Data Warehouse.

## Reporting

Description of the automated reporting system with details on the Excel charts that visualize data from the fact tables.

## Built With

- [SQL Server](https://www.microsoft.com/sql-server) - The database used for data warehousing.
- [SQL Server Integration Services (SSIS)](https://docs.microsoft.com/en-us/sql/integration-services/sql-server-integration-services) - Used for the ETL process.
- [SQL Server Analysis Services (SSAS)](https://docs.microsoft.com/en-us/sql/analysis-services/sql-server-analysis-services) - Used to create the OLAP cube.
- [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) - Used for reporting and data visualization.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/JuanArano17/BankDataWarehouse/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/JuanArano17/BankDataWarehouse/tags).

## Authors

- **Juan Pablo Arano** - *Programmer - Designer - Tester* - [ProfileLink](https://github.com/JuanArano17)
- **Sofia Alejandra Prieto** - *Designer - Tester - SCRUM master* - [ProfileLink](https://github.com/sofipp)

See also the list of [contributors](https://github.com/JuanArano17/BankDataWarehouse/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Recognition of any third-party assets or code used.
- Inspiration or research papers.
- Any other support.
