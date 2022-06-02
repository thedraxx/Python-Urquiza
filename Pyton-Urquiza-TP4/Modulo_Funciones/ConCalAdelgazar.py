def consumo_calorias_recomendado_para_adelgazar(TMB):
    Tmbmin = (TMB * 80) / 100
    Tmbmax = (TMB * 85) / 100

    return 'Para adelgazar es recomendado que consumas entre', round(Tmbmin), ' y ', round(Tmbmax), 'calorias'
