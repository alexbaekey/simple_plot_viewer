import numpy as np
import pandas as pd

x = np.linspace(0, 2 * np.pi, 100)

sine_values = np.sin(x)
cosine_values = np.cos(x)

df = pd.DataFrame({
    'x': x,
    'Sine': sine_values,
    'Cosine': cosine_values
})

df.to_csv(f'data/sample_csv.csv')
