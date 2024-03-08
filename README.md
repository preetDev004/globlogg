## 1. Project Title and Description
    - Title: GloBlogg
    - Description: GloBlogg is a blogging platform where users can explore and create blogs across various categories. 
                   After creating an account, users can not only view blogs but also create, edit, and delete their own blog posts. 
                   The platform provides a personalized dashboard where users can manage their blogs, enhancing their engagement
                   with the content.

## 2. Installation
    - Dependencies: 
        + Python 3.8 or higher (we used Python 3.10)
        + PostgreSQL (we used neon.tech serverless postgreSQL)
        + asgiref==3.7.2
        + Django==5.0.2
        + psycopg2-binary==2.9.9
        + python-dotenv==1.0.1
        + sqlparse==0.4.4
        + typing_extensions==4.9.0

    - Installation Instructions: 
        1. Clone the repository: git clone https://github.com/BTP405/project-1-group-12.git globlogg-project
        2. Navigate to the project directory: cd globlogg-project
        3. (optional) Start the virtual environment: source tst/bin/activate 
        4. Install Python dependencies: pip install -r requirements.txt
        5. Create and configure database: settings.py
        6. Set up the database by running migrations: python manage.py migrate
        7. Start the development server: python manage.py runserver
        
## 3. Usage
    - Examples: 
        a. To create a new blog post, first login/signup then navigate to Create Blog and fill out the form.
        b. To edit an existing blog post, navigate to Profile and choose the blog you want to edit and update the form.
        c. To search a blog post, navigate to home and type the title in search bar and click on search.

    - Configuration: 
        1. Ensure your database settings in settings.py are correctly configured.
        2. Customize the CATEGORIES list in constants.py to add or remove blog categories.

## 4. Features
    - List of Features: 
        + User Authentication: Secure login and signup processes.
        + Blog Management: Create, edit, and delete blog posts.
        + Category Filtering: View blogs by category and search within categories.
        + Search: Find the blogs by title.

## 5. Contributing
    - Guidelines: 
        Fork the repository and create a pull request for your contributions.
        Ensure your code adheres to the project's style guide.

    - Code Style: If applicable, provide guidelines or references to your code style.

### 6. Credits

    - Authors: 
        1. Preet Dineshkumar Patel
        2. Madhav Rajpal
        3. Aastha Kalpeshkumar Patel

    - Acknowledgments: 
        Special thanks to the Django community for Django Docs  which helped in this project.


## 7. License
    - License Information:
        Specify the license under which your project is distributed.
    
## 8. Additional Sections (Optional)
    - NOTE:
        1. You need to create a .env file and add your database credentials in it.
        2. The 'tst' is a virtual environment folder which is not necessary to have.

