import pandas as pd
import os
import numpy as np

vec=[
'Year',
'T2M_1',
'WD2M_1',
'WS2M_1',
'PS_1',
'QV2M_1',
'PRECTOTCORR_1',
'ALLSKY_SFC_SW_DWN_1',
'EVPTRNS_1',
'GWETPROF_1',
'SNODP_1',
'T2MDEW_1',
'CLOUD_AMT_1',
'EVLAND_1',
'T2MWET_1',
'FRSNO_1',
'ALLSKY_SFC_LW_DWN_1',
'ALLSKY_SFC_PAR_TOT_1',
'ALLSKY_SRF_ALB_1',
'PW_1',
'Z0M_1',
'RHOA_1',
'RH2M_1',
'CDD18_3_1',
'HDD18_3_1',
'TO3_1',
'AOD_55_1',
'VAP_1',
'VPD_1',
'ET0_1'
]

def AgruparMatrizFinal(matriz):
    anios_unicos = np.unique(matriz[:, 0])
    resultados = []
    for anio in anios_unicos:
        filas_del_anio = matriz[matriz[:, 0] == anio]
        promedio = filas_del_anio[:, 1:].mean(axis=0)
        resultados.append(np.insert(promedio, 0, anio))
    
    return np.array(resultados)


matriz_general = np.empty((0, len(vec)))
for i in range(1,12):
    if (os.path.exists(f'./data/southamerica_{i}_regional_monthly.csv')):
        df=pd.read_csv(f'./data/southamerica_{i}_regional_monthly.csv')
        informacion=df[(df['lat']>=-41.08) & (df['lat']<=-33.04) & (df['lng']>=-63.37) & (df['lng']<=-55.82)]
        informacion=informacion[vec]
        if (informacion.shape[0]>0):
            matriz_general = np.vstack([matriz_general, informacion.to_numpy()])
matriz_general=AgruparMatrizFinal(matriz_general)
print(f'cantidad de datos finales: {matriz_general.shape[0]}')
np.savetxt('./data/informacion_filtrada.csv', matriz_general, delimiter=',', header=",".join(vec), comments='', fmt='%f')
