# Clone Social API

A FastAPI-based social media API clone with modern architecture and best practices.

## Features

- User authentication and authorization
- Social media features (posts, comments, likes)
- RESTful API design
- Database migrations with Alembic
- API documentation with Swagger UI

## Tech Stack

- **FastAPI**: High-performance web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **Alembic**: Database migration tool
- **Pydantic**: Data validation and settings management
- **PostgreSQL**: Database (recommended for production)

## Getting Started

### Prerequisites

- Python 3.8+
- Pip package manager
- Virtual environment tool

### Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd clone-social-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   # Create a .env file in the root directory with the following variables
   DATABASE_URL=postgresql://user:password@localhost/db_name
   SECRET_KEY=your_secret_key
   ```

5. Run database migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the application:
   ```bash
   uvicorn app.main:app --reload
   ```

7. Access the API documentation:
   ```
   http://localhost:8000/docs
   ```

## Project Structure

```
clone-social-api/
├── alembic/                # Database migrations
├── app/                    # Application code
│   ├── api/                # API routes
│   ├── core/               # Core functionality
│   ├── crud/               # CRUD operations
│   ├── db/                 # Database models and config
│   ├── schemas/            # Pydantic models
│   └── main.py             # FastAPI application
├── static/                 # Static files
├── .env                    # Environment variables
├── alembic.ini             # Alembic configuration
└── requirements.txt        # Python dependencies
```

## API Documentation

The API documentation is automatically generated using Swagger UI.
Once the application is running, you can access it at:

```
http://localhost:8000/docs
```

## Database Management

This project uses Alembic for database migrations.

### Creating a New Migration

```bash
alembic revision --autogenerate -m "Description of changes"
```

### Applying Migrations

```bash
alembic upgrade head
```

## Development

### Adding Dependencies

1. Add the package to `requirements.txt`
2. Run `pip install -r requirements.txt`

### Testing

```bash
pytest
```

## Deployment

For production deployment:

1. Set up a production database
2. Configure environment variables for production
3. Use a production ASGI server like Uvicorn with Gunicorn

## License

[MIT License](LICENSE) 