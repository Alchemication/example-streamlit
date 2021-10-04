from app.libs.streamlit_multi_view_app import StreamlitMultiViewApp, View
from app.views import header, home, data  # Import new view modules here
from app.config import Config

app = StreamlitMultiViewApp()
app_config = Config()

# Display header view first
app.add_header(View(title=app_config.APP_NAME, func=header.view))

# Display all views below
app.add_view(View(title="Home", func=home.view))
app.add_view(View(title="Data", func=data.view))

# The main app
app.run()
