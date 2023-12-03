# DjangoArtistryAPI
Enabling token-based authentication in Django REST Framework involves initial steps such as installing Django and Django REST Framework via pip, setting up a new project and app, and configuring Django settings to include token authentication. Additionally, a customized user model should be created within the app, accompanied by the development of serializers for both user registration and token retrieval. Subsequently, views need to be established for user registration, login, and token retrieval, followed by URL configuration for these specific endpoints. Lastly, running migrations and starting the development server completes the process. This comprehensive approach ensures that users can successfully register, log in, and acquire tokens for secure API operations within your Django REST Framework project

### Getting Started  

Follw below steps , these instructions will help you set up and run the Django Artist API locally for development and testing purposes.

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- Postgres (or another database of your choice)

### Installation

1. Clone the repository:

   ```bash
   - git clone https://github.com/yourusername/django-artist-api.git
   or
   Can download the files manually
   
2. Navigate to the project directory:

   cd django-artist-api  #check your downloaded file path before this
   
4. Create a virtual environment

   python -m venv venv
   
6. Activte the VM (in Windows OS)
   venv\Scripts\activate
   
7. Install the Requirement Libraries
   - pip install djangorestframework
     
8. To set-up database
   python manage.py migrate
   
9. Create superuser account
   python manage.py createsuperuser

8.Run the server
   python manage.py runserver
   

### API Endpoints and methods
You can use the Postman tool to Test Endpoint or can be done through in terminal

   - User Registration:
       Endpoint: /api/register/
       Method: POST
       Requires providing a unique username, email, and password.
       
   - List and Create Work
       Endpoint: /api/works/
       Method: GET (List all works) and POST (Create a new work)
       Authorization : "Authorization: Token <your-access-token>"

   - Filter Works by Work Type:
       Endpoint: /api/works?work_type=YT/ or /api/works?work_type=IG/
       Method: GET
     
   - Search Works by Artist Name:
       Endpoint: /api/works?artist=[Artist Name]/
       Method: GET

   - Obtain Authentication Token:
       Endpoint: /api/token/
       Method: POST
       Requires username and password in the request body
           eg : {
                    "username": "newuser",
                    "password": "securepassword"
                }
       Requires providing a registered username and password in the request body.
       The obtained token should be included in the Authorization header for authenticated requests.


User Registration and Authentication:

Users initiate the registration process by sending a POST request to the /api/register/ endpoint, providing a unique username, email, and password. Subsequently, token-based authentication is employed. Upon successful registration, users acquire an authentication token by issuing a POST request to the /api/token/ endpoint, supplying their credentials. This token becomes essential for subsequent authenticated requests, ensuring secure access to the API.

Artist and Work Management:

Authenticated users gain the ability to seamlessly manage artists and works through an array of API endpoints. These endpoints include /api/works/ for listing and creating works, /api/works?work_type=YT/ for filtering works by work type, and /api/works?artist=[Artist Name]/ for searching works by artist name. This flexible management system empowers users to efficiently organize and retrieve artistic content based on various criteria.

Testing and Development:

To facilitate testing and development, developers can utilize tools like Postman. A dedicated Postman collection is provided, streamlining the testing process. Developers are encouraged to interact with the API, ensuring its functionality and identifying potential areas for improvement. This collaborative approach enhances the robustness and reliability of the Django Artist API.
