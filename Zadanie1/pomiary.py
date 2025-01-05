# pomiary.py

def c_to_f(celsius):
    """Konwertuje temperaturę z Celsjusza na Fahrenheita."""
    return (celsius * 9 / 5) + 32

def predkosc_wiatru(mps):
    """Konwertuje prędkość wiatru z m/s na km/h."""
    return mps * 3.6

def cisnienie_atmosferyczne(hpa):
    """Konwertuje ciśnienie atmosferyczne z hPa na mmHg."""
    return hpa / 1.333
