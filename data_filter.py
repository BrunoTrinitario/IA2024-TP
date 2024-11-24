import pandas as pd
import os
import numpy as np

matriz_general = np.empty((0, 8))

for i in range(1,12):
    if (os.path.exists(f'./data/southamerica_{i}_regional_monthly.csv')):
        df=pd.read_csv(f'./data/southamerica_{i}_regional_monthly.csv')
        informacion=df[(df['Year']>=1999.0) & (df['lat']>=-41.08) & (df['lat']<=-33.04) & (df['lng']>=-63.37) & (df['lng']<=-55.82)]
        informacion=informacion[['Year','lat','lng','T2M_1','T2M_MAX_1','T2M_MIN_1','PS_1','PW_1']]
        if (informacion.shape[0]>0):
            #print(f"archivo: {i}\n", informacion)
            matriz_general = np.vstack([matriz_general, informacion.to_numpy()])

print(f'cantidad de datos finales: {matriz_general.shape[0]}')
np.savetxt('./data/informacion_filtrada.csv', matriz_general, delimiter=',', header="Year,lat,lng,T2M_1,T2M_MAX_1,T2M_MIN_1,PS_1,PW_1", comments='', fmt='%f')
