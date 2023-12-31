# Invoice_API

This is a Django project implementing an API for managing invoices and associated details using Django Rest Framework.

# Installations

1. Clone the repository:
   
    Command : 1. git clone https://github.com/aashishporwal1/Invoice_API.git
			  2. cd django-invoice-project

2. Create virtual environment (optional but recommended):

    Command - python -m venv venv

3. Activate virtual environment:

	On Windows: $.\venv\Scripts\activate
	On macOS/Linux: $source venv/bin/activate

4. Install dependencies:

	Command: pip install -r requirements.txt

5. Apply migrations:

	Command: python manage.py migrate

6. Run the development server:

	Command: python manage.py runserver

The API will be available at http://localhost:8000/api/.

API Endpoints
/api/invoices/: List and create invoices.
/api/invoices/<int:pk>/: Retrieve, update, and delete a specific invoice.
/api/invoice_details/: List and create invoice details.
/api/invoice_details/<int:pk>/: Retrieve, update, and delete a specific invoice detail.