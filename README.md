# Asset API Flask

## Overview
A simple REST API built with Python Flask for managing and searching ICT assets.

## Features
- View all assets
- Search assets by status
- Search assets by type
- Asset summary reporting
- CSV-based asset storage

## Technologies
- Python
- Flask
- CSV
- REST API

## API Endpoints

### Get all assets
GET /assets

### Get asset summary
GET /summary

### Search by status
GET /assets/search?status=Assigned

### Search by type
GET /assets/search?type=Laptop

## Note
This is a demo project created for portfolio and learning purposes.
