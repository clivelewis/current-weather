
## Current Weather Info Script

A very simple script that I wrote for myself to check the current weather in different locations without leaving Terminal window.
Feel free to change it for your personal needs. Should be pretty interesting to play around for beginners.

<img src="https://s4.gifyu.com/images/preview3cba14d120442f23.gif" width="600">


## How to use

#### Dependency
You only need [requests](https://pypi.org/project/requests/)
 library to run this script.
```bash
pip install requests
```
#### Setup
1. Get your API key from https://openweathermap.org/api
2. Open **weather.py** script, find WeatherApi class and replace placeholder **API_KEY** value with your actual API key.
3. (Optional) Set alias for easy execution. Replace path with real one.
``` bash
alias weather="python3 /path/to/weather.py"
```

### Usage
Show current weather in Athens, Greece
```bash
weather athens
```
Multiple cities at once. Use quotes for locations with more than 1 word
```bash
weather riga athens 'buenos aires' barcelona
```
Usage without 'weather' alias.
```bash
python3 /path/to/weather.py barcelona
```
