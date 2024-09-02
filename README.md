
## Steps to Run

To start this project run

```bash
  # Create a virtual environment in the current directory
  python3 -m venv venv

  # Activate the virtual environment (macOS/Linux)
  source venv/bin/activate

  # Activate the virtual environment (Windows)
  venv\Scripts\activate

  # Install packages within the virtual environment
  pip3 install -r requirements.txt

  # create a .env file at the root directory with following values
  PORT='8000'
  HOST='127.0.0.1'

  # Run the app
  uvicorn app.main:app --reload

  # Deactivate the virtual environment when done
  deactivate
```

## Notes
- Images are stored in the images directory
- The scraped data is stored in data/scraped_data.json
- AUTH token used is static, need to use the same (mentioned in /config/settings.py ).

## Usage
- Once the project is started, we can execute the following curl command:
```bash
  curl --location 'http://127.0.0.1:8088/start_scraping/?pages=1' \
--header 'Authorization: Bearer <token>'
```
