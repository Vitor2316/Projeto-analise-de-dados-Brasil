# DEPLOYMENT GUIDE - STREAMLIT CLOUD

## Prerequisites

1. GitHub repository with the project
2. Streamlit Cloud account (free): https://streamlit.io/cloud

## Steps to Deploy

### 1. Prepare Repository

Ensure your repository has:
- `scripts/dashboard_salarios.py` (the Streamlit app)
- `requirements.txt` (in root directory)
- `dados/` folder with all CSV files

### 2. Create Streamlit Configuration

Create file `.streamlit/config.toml` in root:

```toml
[theme]
primaryColor = "#2E86C1"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
headless = true
port = 8501
enableCORS = false
```

### 3. Update requirements.txt

Ensure it includes:
```
streamlit>=1.28.0
plotly>=5.14.0
pandas>=2.0.0
numpy>=1.24.0
```

### 4. Deploy on Streamlit Cloud

1. Go to: https://share.streamlit.io/
2. Click "New app"
3. Select your GitHub repository
4. Branch: `main` or `master`
5. Main file path: `scripts/dashboard_salarios.py`
6. Click "Deploy!"

### 5. Dashboard will be live at:

```
https://[your-app-name].streamlit.app
```

### 6. Update README.md

Add link to live dashboard:

```markdown
## Interactive Dashboard

**Live Demo:** [View Dashboard](https://your-app-name.streamlit.app)

Or run locally:
```bash
streamlit run scripts/dashboard_salarios.py
```
```

## Troubleshooting

### Error: "File not found"

Solution: Update file paths in `dashboard_salarios.py` to use relative paths:

```python
# Change from:
df = pd.read_csv('../dados/brasil_anual_CORRIGIDO_FINAL.csv')

# To:
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'dados')
df = pd.read_csv(os.path.join(DATA_DIR, 'brasil_anual_CORRIGIDO_FINAL.csv'))
```

### Error: "Module not found"

Solution: Add missing packages to `requirements.txt`

### App crashes on load

Solution: Check Streamlit Cloud logs for detailed error messages

## Custom Domain (Optional)

Streamlit Cloud allows custom domains on Pro plan.

Free tier uses: `https://your-app-name.streamlit.app`

## Updates

Any push to your GitHub repository will automatically redeploy the app.

## Monitoring

- View app usage: Streamlit Cloud dashboard
- Check logs: Click "Manage app" > "Logs"
- Restart app: Click "Reboot app" if needed

