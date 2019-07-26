import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

nc = '../../MONC/dycoms_simulation/mbl_sc_dycoms_dg_7260.0.nc'
DS = xr.open_dataset(nc)

def scalar_plot(obj, name):
    obj.plot()
    plt.title(name, fontsize=12)
    plt.show()

[scalar_plot(obj, name) for (name, obj) in DS.data_vars.items() if len(obj.dims) == 1] 
