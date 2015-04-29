Cloud provider selector based on cost and other requirements
============

Este es el repositorio del proyecto final del alumno **José Alberto Pérez Melián** (`jopeme[AT]inf.upv.es`) para **Servicios en la Nube**, asignatura del **Máster Universitario en Gestión de la Infomación** de la **Universitàt Politècnica de València**.

----------

Main purpose
------------------
The purpose of this project is to develop a cloud instance's provider selector, scrapping the data from the web and making a light app as a first approach.
The app has been written in `Python`, using a `SQLite` database and [`Scrapy`](www.scrapy.org) as crawler/spider.

Files and folders
----------------------


- `/data` contains the data files used in this project (data extracted from Amazon & Google Cloud Platform and data processed)
- `/senspider` contains the Scrapy project and the spiders
- `application.py` contains the main application where to make the data queries
- `insert_data.py` contains how to insert the extracted data to de database
- `sendatabase.sqlite` is the database used in this project

> **Note**
> For more information, please check the task section in PoliformaT.