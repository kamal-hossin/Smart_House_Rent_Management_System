# House Rent Management System

A comprehensive web application built with Django and Django REST Framework for managing house rentals. This system allows users to post advertisements for rental properties, manage user profiles, handle rental requests, and leave reviews.

## Features

- **User Management**: Registration, authentication, and profile management using JWT tokens
- **Advertisements**: Post, view, and manage rental property listings
- **Rental Requests**: Users can submit rental requests for properties
- **Reviews**: Leave and view reviews for properties and users
- **Favorites**: Save favorite properties for quick access

## Tech Stack

- **Backend**: Django 6.0.1
- **API Framework**: Django REST Framework 3.16.1
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: SQLite (configurable to PostgreSQL)
- **Styling**: Tailwind CSS
- **Other Libraries**: django-filter, psycopg2-binary, Pillow

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd house-rent-management-system
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database:**
   - The default database is SQLite (db.sqlite3)
   - For production, configure PostgreSQL in `house_rent/settings.py`

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication
- `POST /api/auth/login/` - User login
- `POST /api/auth/register/` - User registration
- `POST /api/auth/token/refresh/` - Refresh JWT token

### Users
- `GET /api/users/` - List users
- `GET /api/users/{id}/` - Retrieve user details
- `PUT /api/users/{id}/` - Update user profile
- `DELETE /api/users/{id}/` - Delete user

### Advertisements
- `GET /api/advertisements/` - List advertisements
- `POST /api/advertisements/` - Create new advertisement
- `GET /api/advertisements/{id}/` - Retrieve advertisement details
- `PUT /api/advertisements/{id}/` - Update advertisement
- `DELETE /api/advertisements/{id}/` - Delete advertisement

### Requests
- `GET /api/requests/` - List rental requests
- `POST /api/requests/` - Create rental request
- `GET /api/requests/{id}/` - Retrieve request details
- `PUT /api/requests/{id}/` - Update request
- `DELETE /api/requests/{id}/` - Delete request

### Reviews
- `GET /api/reviews/` - List reviews
- `POST /api/reviews/` - Create review
- `GET /api/reviews/{id}/` - Retrieve review details
- `PUT /api/reviews/{id}/` - Update review
- `DELETE /api/reviews/{id}/` - Delete review

### Favorites
- `GET /api/favorites/` - List user favorites
- `POST /api/favorites/` - Add to favorites
- `DELETE /api/favorites/{id}/` - Remove from favorites

## Usage

1. Register a new user account or login with existing credentials
2. Browse available rental advertisements
3. Submit rental requests for properties of interest
4. Leave reviews for properties or other users
5. Save favorite properties for quick access

## Deployment to Vercel

This project is configured for deployment on Vercel.

### Prerequisites
- Vercel account
- Git repository

### Deployment Steps

1. **Push your code to GitHub/GitLab:**
   ```bash
   git add .
   git commit -m "Prepare for Vercel deployment"
   git push origin main
   ```

2. **Connect to Vercel:**
   - Go to [vercel.com](https://vercel.com) and sign in
   - Click "New Project"
   - Import your repository

3. **Configure Environment Variables:**
   In the Vercel dashboard, add the following environment variables:
   - `SECRET_KEY`: A secure random key (generate with `python -c "import secrets; print(secrets.token_urlsafe(50))"`)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Your Vercel app URL (e.g., `your-app.vercel.app`)

   Optional:
   - `DATABASE_URL`: For PostgreSQL (recommended for production)
   - Email settings for production

4. **Deploy:**
   - Vercel will automatically detect the `vercel.json` and deploy
   - The app will be available at `https://your-app.vercel.app`

### Notes
- SQLite is used by default but not recommended for production due to Vercel's serverless nature
- For production database, use PostgreSQL and set `DATABASE_URL`
- Static files are handled by WhiteNoise

## Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/` using superuser credentials to manage users, advertisements, requests, and reviews.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, email support@houserentsystem.com or join our Slack channel.