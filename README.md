# Delhi High Court Case Status Checker

A web application that fetches case details from the Delhi High Court website using browser automation.

## Features

- Search for cases by case type, number, and filing year
- View case metadata including parties, hearing dates, and orders/judgments
- Download PDFs of orders/judgments when available
- Query history logging with MongoDB
- Clean, responsive web interface
- Browser automation with Chrome/Firefox fallback

## Technical Approach

1. **Browser Automation**: Uses Selenium WebDriver with Chrome (fallback to Firefox) for handling dynamic content and CAPTCHA solving.

2. **CAPTCHA Handling**: Automatically reads and solves text-based CAPTCHAs from the court website.

3. **Data Extraction**: Parses HTML responses using BeautifulSoup to extract case information and PDF links.

4. **Database**: MongoDB is used to log all queries and responses for future reference and analytics.

5. **Error Handling**: Comprehensive error handling with user-friendly messages for various failure scenarios.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirement.txt
   ```

2. **Install MongoDB**:
   - Download and install MongoDB Community Server
   - Or use MongoDB Atlas (cloud database)

3. **Setup Database**:
   ```bash
   python setup_mongodb.py
   ```

4. **Install Chrome Browser**:
   - The application requires Chrome or Firefox browser for automation
   - Chrome is automatically detected in standard installation paths

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   - Open `http://localhost:5000` in your browser
   - View search history at `http://localhost:5000/queries`

## Database Migration

If upgrading from MySQL to MongoDB, run the migration script:
```bash
python migrate_to_mongodb.py
```

## Limitations

- Depends on the Delhi High Court website's HTML structure remaining consistent
- Requires a modern browser (Chrome/Firefox) for automation
- CAPTCHA solving may occasionally fail with complex CAPTCHAs
- Some case types might have different form structures
- Network connectivity required for real-time court website access

## File Structure

```
court_data_fetcher/
├── app.py                 # Main Flask application
├── scraper.py            # Web scraping logic with browser automation
├── database.py           # MongoDB operations
├── config.py             # Configuration settings
├── setup_mongodb.py      # Database setup script
├── requirement.txt       # Python dependencies
├── templates/
│   ├── index.html        # Search form
│   ├── results.html      # Results display
│   └── queries.html      # Search history
└── static/
    └── style.css         # Additional styles (optional)
```

🔒 CAPTCHA Strategy
The Delhi High Court case status page uses a numeric text CAPTCHA.
Our script automatically handles this by:
Locating the <span> element with the numeric CAPTCHA using:
captcha_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'captcha') or contains(@id,'captcha')]"))
)
captcha_text = captcha_element.text.strip()
Extracting the numeric CAPTCHA text directly from the DOM.
Filling it programmatically into the form using:
driver.find_element(By.XPATH, "//input[contains(@id,'captcha')]").send_keys(captcha_text)
No manual input or external OCR service is needed, since the CAPTCHA is already plain text.
Note:
If the Delhi High Court changes the CAPTCHA to image-based, the following strategies can be used:

OCR with Tesseract to extract text from the image
Or manual token input through the web form
