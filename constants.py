MAX_CLICKS = 1000
CLICK_INTERVAL = 0.01
ERROR_MESSAGES = {
    'EXCEEDS_MAX_CLICKS': 'Number of clicks exceeds the maximum limit.',
    'INVALID_INTERVAL': 'Click interval must be a positive number.',
    'INVALID_CLICKS': 'Number of clicks must be an integer.',
}

def validate_clicks(clicks):
    if not isinstance(clicks, int):
        raise ValueError(ERROR_MESSAGES['INVALID_CLICKS'])
    if clicks < 1 or clicks > MAX_CLICKS:
        raise ValueError(ERROR_MESSAGES['EXCEEDS_MAX_CLICKS'])


def validate_interval(interval):
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ValueError(ERROR_MESSAGES['INVALID_INTERVAL'])
