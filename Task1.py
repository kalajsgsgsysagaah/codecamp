import requests
import matplotlib.pyplot as plt
import seaborn as sns
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# OpenWeatherMap API details
API_KEY = "your_api_key_here"
CITY = "New York"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch weather data
response = requests.get(URL)
data = response.json()

# Check if data is valid
if 'list' in data:
    times = [entry['dt_txt'] for entry in data['list']]
    temps = [entry['main']['temp'] for entry in data['list']]
    print(times, temps)  # Debugging check
else:
    print("Error fetching data:", data)
    times, temps = [], []

# Create visualization using Matplotlib and Seaborn
plt.figure(figsize=(10, 5))
sns.lineplot(x=times, y=temps, marker="o", linestyle="-", color="b")
plt.xticks(times[::5], rotation=45)
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title(f"Temperature Trend for {CITY}")
plt.tight_layout()
plt.show()

# Dash dashboard
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(f"Weather Forecast for {CITY}"),
    dcc.Graph(id='temp-graph'),
    dcc.Interval(id='interval-component', interval=60000, n_intervals=0)
])

@app.callback(Output('temp-graph', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph(n):
    response = requests.get(URL)
    data = response.json()
    
    if 'list' in data:
        times = [entry['dt_txt'] for entry in data['list']]
        temps = [entry['main']['temp'] for entry in data['list']]
        print(times, temps)  # Debugging check
    else:
        print("Error fetching data:", data)
        times, temps = [], []
    
    fig = {
        'data': [{'x': times, 'y': temps, 'type': 'line', 'name': 'Temperature'}],
        'layout': {'title': f'Temperature Trend for {CITY}', 'xaxis': {'title': 'Time'}, 'yaxis': {'title': 'Temperature (°C)'}}
    }
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
