# GloBlogg

## 1. Project Title and Description
- **Title:** GloBlogg
- **Description:** GloBlogg is a blogging platform where users can explore and create blogs across various categories. After creating an account, users can not only view blogs but also create, edit, and delete their own blog posts. The platform provides a personalized dashboard where users can manage their blogs, enhancing their engagement with the content.

## 2. Installation
- **Dependencies:**
 - Python 3.8 or higher
 - Django 3.2 or higher
 - PostgreSQL (or any other supported database)
- **Installation Instructions:**
  1. Clone the repository: `git clone <repository_url>`
  2. Navigate to the project directory: `cd globlogg-project`
  3. Install Python dependencies: `pip install -r requirements.txt`
  4. Create and configure database: `settings.py`
  4. Set up the database by running migrations: `python manage.py migrate`
  5. Start the development server: `python manage.py runserver`

## 3. Usage
- **Examples:**
 - To create a new blog post, first login/signup then navigate to `Create Blog` and fill out the form.
 - To edit an existing blog post, navigate to `Profile` and choose the blog you want to `edit` and update the form.
 - To search a blog post, navigate to `home` and type the title in search bar and click on `search`.
- **Configuration:**
 - Ensure your database settings in `settings.py` are correctly configured.
 - Customize the `CATEGORIES` list in `constants.py` to add or remove blog categories.

## 4. Features
- **User Authentication:** Secure login and signup processes.
- **Blog Management:** Create, edit, and delete blog posts.
- **Category Filtering:** View blogs by category and search within categories.
- **Personalized Profile:** Manage your own blog posts.

## 5. Contributing
- **Guidelines:**
 - Fork the repository and create a pull request for your contributions.
 - Ensure your code adheres to the project's style guide.
- **Code Style:**
 - Follow PEP 8 for Python code.
 - Use Django's best practices for web development.

## 6. Credits
- **Authors:** Preet Dineshkumar Patel, Madhav Rajpal, Aastha Kalpeshkumar Patel
- **Acknowledgments:** Special thanks to the `Django community` and `Newton school` (https://www.youtube.com/playlist?list=PLVBKjEIdL9bvCdI4l1Emvbezv10GjUaLk) that guided this project.

## 7. License
- **License Information:** This project is licensed under the MIT License.

## 8. Additional Sections (Optional)
- **Troubleshooting:**
 - If you encounter any issues during installation, ensure all dependencies are correctly installed and your database is properly configured.
