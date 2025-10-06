# Doggoscope

I point my Pi at dog pics, and it tells me stats.

## Setup

1. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run Web Server:

   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 src.app:app or flask --app src.app  run
   ```

4. Open your browser to `http://localhost:8000` and upload a dog picture to see the stats!
