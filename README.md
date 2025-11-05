# CI/CD Learning Project - DataFrame Pipeline API

A FastAPI-based project for learning CI/CD practices using GitHub. This project provides a RESTful API for uploading, reading, and filtering data files (CSV, JSON, XLSX) using Polars for efficient dataframe manipulation.

## ?? Features

### Core Functionality

1. **File Upload & Processing**
   - Upload CSV, JSON, or XLSX files via API
   - Automatic file naming with unique identifiers
   - Data validation and processing using Polars dataframes

2. **Data Reading**
   - Read uploaded files and return data in JSON format
   - Support for multiple file formats (CSV, JSON, XLSX)
   - Efficient dataframe operations using Polars

3. **Data Filtering**
   - Filter data based on column values
   - Multiple filter types:
     - `equals`: Exact match
     - `not_equals`: Not equal to value
     - `greater_than`: Greater than value
     - `less_than`: Less than value

4. **Configuration Management**
   - Environment-based configuration using `.alg_env` file
   - Database URL management (PostgreSQL, Redis)
   - Import path configuration
   - Dynamic Python path management

## ?? API Endpoints

### GET `/`
Welcome endpoint that returns a greeting message.

**Response:**
```json
{
  "message": "welcome to the pipeline dataframe project"
}
```

### POST `/read`
Upload and read a data file.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: File upload (CSV, JSON, or XLSX)

**Response:**
```json
{
  "message": "file uploaded successfully",
  "unique_id": "file_0_input_test.csv",
  "data": [
    {
      "name": 1,
      "age": 25,
      "city": "new york"
    },
    ...
  ]
}
```

### POST `/filter`
Filter data from an uploaded file.

**Request:**
- Method: `POST`
- Query Parameter: `unique_id` (e.g., `file_0_input_test.csv`)
- Body (JSON):
```json
{
  "filter_column": "name",
  "filter_value": "1",
  "filter_type": "equals"
}
```

**Response:**
```json
{
  "message": "file uploaded successfully",
  "data": [
    {
      "name": 1,
      "age": 25,
      "city": "new york"
    }
  ]
}
```

## ??? Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ci_cd_learning
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   - Create `api_manager/.alg_env` file with your configuration:
   ```
   db_urls={"postgres_async": ["postgresql://..."], "redis": ["redis://..."]}
   import_paths={"uploads": "uploads/", "inputs": "files/inputs/"}
   ```

4. **Create necessary directories**
   ```bash
   mkdir -p uploads files/inputs files/uploads
   ```

## ?? Testing

The project includes comprehensive test coverage using pytest.

### Running Tests

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_api_manager.py
```

### Test Coverage

- **Root endpoint test**: Validates welcome message
- **Read data test**: Tests file upload and reading functionality
- **Filter data test**: Tests data filtering with various conditions

### Example Test Data

The test suite uses sample CSV files located in `files/inputs/` directory. The tests validate:
- File upload success
- Data parsing accuracy
- Filter functionality correctness
- API response structure

## ?? Project Structure

```
ci_cd_learning/
??? api_manager/
?   ??? __pycache__/
?   ??? config.py          # Configuration management
?   ??? main.py            # FastAPI application and endpoints
??? orchestrator/
?   ??? __pycache__/
?   ??? stream.py          # Data manipulation class (Polars operations)
??? tests/
?   ??? __pycache__/
?   ??? test_api_manager.py    # API endpoint tests
?   ??? decorator_example.py   # Decorator example code
??? files/
?   ??? inputs/            # Input test files
?   ??? uploads/           # Uploaded files storage
??? uploads/               # Additional uploads directory
??? conftest.py           # Pytest configuration
??? requirements.txt      # Python dependencies
??? README.md            # Project documentation
```

## ?? Technical Details

### Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Polars**: Fast dataframe library for data manipulation
- **Pandas**: Data analysis library (used for conversion)
- **Pydantic**: Data validation using Python type annotations
- **Pytest**: Testing framework
- **httpx**: HTTP client for testing
- **python-multipart**: File upload support
- **pyarrow**: Arrow format support for Polars

### Key Components

1. **Manipulation Class** (`orchestrator/stream.py`)
   - Handles file reading for multiple formats
   - Provides filtering functionality with multiple operators
   - Uses Polars for efficient dataframe operations

2. **Config Class** (`api_manager/config.py`)
   - Loads configuration from `.alg_env` file
   - Manages database URLs and import paths
   - Handles Python path management

3. **FastAPI Application** (`api_manager/main.py`)
   - Defines API endpoints
   - Handles file uploads and processing
   - Manages unique file identifiers

## ?? Usage Examples

### Upload and Read a File

```bash
curl -X POST "http://localhost:8000/read" \
  -F "file=@path/to/your/file.csv"
```

### Filter Data

```bash
curl -X POST "http://localhost:8000/filter?unique_id=file_0_input_test.csv" \
  -H "Content-Type: application/json" \
  -d '{
    "filter_column": "age",
    "filter_value": "30",
    "filter_type": "greater_than"
  }'
```

## ?? CI/CD Learning

This project is designed for learning CI/CD practices including:
- Automated testing with GitHub Actions
- Continuous Integration workflows
- Code quality checks
- Automated deployment pipelines

## ?? Notes

- Files are stored with unique identifiers to prevent overwrites
- The system uses Polars for efficient data processing
- All file operations are asynchronous for better performance
- Configuration is managed through environment files

## ?? Contributing

This is a learning project. Feel free to experiment and improve!

## ?? License

[Add your license information here]
