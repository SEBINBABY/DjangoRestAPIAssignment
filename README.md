# Django Vendor Management System:

A Vendor Management System (VMS) built using Django and Django REST Framework. This system manages vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Table of Contents

* Features

* Technical Requirements

* Installation

* Usage

* API Documentation

## Features

### 1. Vendor Profile Management:

* Create, retrieve, update, and delete vendor profiles.
  
* Calculate and display vendor performance metrics.

### 2. Purchase Order Tracking:

* Create, retrieve, update, and delete purchase orders.
  
* Track delivery status, items, quantity, and other details.

### 3. Vendor Performance Evaluation:

* Calculate performance metrics, including on-time delivery rate, quality rating average, average response time, and fulfillment rate.

* Historical performance tracking for trend analysis.

## Technical Requirements

* Django (latest stable version)

* Django REST Framework (latest stable version)

* Token-based authentication

* PEP 8 compliant code

* Comprehensive data validations

* Django ORM for database interactions

## Installation

#### 1.Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate

#### 2. Install dependencies:

pip install Django==5.0.4

pip install -U djangorestframework (Version : 3.15.1 is used here)

#### 3. Run migrations:

python manage.py makemigrations

python manage.py migrate

#### 4. Run:

python manage.py runserver

## API

```bash

http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/api/vendors/

http://127.0.0.1:8000/api/vendors/<int:vendor_id>/

http://127.0.0.1:8000/api/purchase_orders/

http://127.0.0.1:8000/api/purchase_orders/<int:po_id>/

http://127.0.0.1:8000/api/historical_performance/

http://127.0.0.1:8000/api/vendors/<int:vendor_id>/performance/

http://127.0.0.1:8000/api/purchase_orders/<int:pk>/acknowledge/

## API Documentation

Detailed API documentation is available in the API Documentation file. Please refer to this documentation for detailed information about each API endpoint, including input parameters, authentication requirements, and response formats.

Sample JSON for Creating a New Vendor
{
"name": "Sample Vendor name",

"contact_details": "1112223334",

"address": "Lane No, City",

"vendor_code": "VEN123",

"on_time_delivery_rate": 90.0,

"quality_rating_avg": 4.0,

"average_response_time": 3.5,

"fulfillment_rate": 85.0
}

## Vendor Endpoints

### 1.Create a new vendor:

URL: POST /api/vendors/ Payload Example:

    json

    {

        "name": "Vendor Name",

        "contact_details": "Contact Information",

        "address": "Vendor Address",

        "vendor_code": "VEN123"

    }

*Authentication: Token-based authentication required.

### 2. List all vendors:

URL: GET /api/vendors/

Authentication: Token-based authentication required.

Retrieve a specific vendor's details:

URL: GET /api/vendors/{vendor_id}/

Authentication: Token-based authentication required.

Update a vendor's details:

URL: PUT /api/vendors/{vendor_id}/

Payload Example:

json
 
{

"name": "Updated Vendor Name",

"contact_details": "Updated Contact Information",

"address": "Updated Vendor Address",

"vendor_code": "VEN123"

}

*Authentication: Token-based authentication required.

### 3. Delete a vendor:

URL: DELETE /api/vendors/{vendor_id}/

Authentication: Token-based authentication required.

Retrieve a vendor's performance metrics:

URL: GET /api/vendors/{vendor_id}/performance/

Authentication: Token-based authentication required.

## Purchase Order Endpoints

### 1. Create a new purchase order:

URL: POST /api/purchase_orders/

Payload Example:
json

{

"po_number": "PO123",

"vendor": 1,

"delivery_date": "2024-05-10T10:00:0,

"acknowledgment_date": "2024-05-01T10:00:00",

"items": ["item1","item2"],

"quantity": 10,

"status": "pending"
}

*Authentication: Token-based authentication required.

### 2. List all purchase orders:

URL: GET /api/purchase_orders/

Authentication: Token-based authentication required.

### 3. Retrieve details of a specific purchase order:

URL: GET /api/purchase_orders/{po_id}/

Authentication: Token-based authentication required.

Update a purchase order:

URL: PUT /api/purchase_orders/{po_id}/

Payload Example:

json

{

"status": "completed"

}

*Authentication: Token-based authentication required.

### 4. Delete a purchase order:

URL: DELETE /api/purchase_orders/{po_id}/

*Authentication: Token-based authentication required.

Acknowledge Purchase Order Endpoint

### 5. Acknowledge a purchase order:

URL: PATCH /api/purchase_orders/{po_id}/acknowledge/

Acknowledgement date wii be updated with the current date and time

*Authentication: Token-based authentication required. Please note that you should replace {vendor_id} and {po_id} in the URLs with the actual vendor and purchase order IDs you want to interact with.

Ensure you have the appropriate authentication token and include it in the request headers for endpoints that require authentication. Also, adjust the payload examples based on the actual structure and requirements of your Django application.

