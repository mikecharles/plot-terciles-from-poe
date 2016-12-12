import numpy as np
from cpc.stats.stats import poe_to_terciles
from cpc.stats.stats import put_terciles_in_one_array
from cpc.geogrids import Geogrid
from cpc.geoplot import Geomap, Geofield
from cpc.geoplot.colors import tmean_terciles, precip_terciles

# List of ptiles found in POE file
ptiles = [1, 2, 5, 10, 15, 20, 25, 33, 40, 50, 60, 67, 75, 80, 85, 90, 95, 98, 99]

# Create a Geogrid
geogrid = Geogrid('1deg-global')

# Read in the data and reshape to ptiles x gridpoints
poe = np.fromfile(
    'data.bin', dtype='float32'
).reshape(len(ptiles),geogrid.num_x * geogrid.num_y)

# Extract B, N, and A from POE
B, N, A = poe_to_terciles(poe, ptiles)

# Combine into a single array for plotting, where:
#   - probabilities of below are values between 0 and -100
#   - probabilities of above are values between 0 and 100
#   - values of near are set to 0
data = 100 * put_terciles_in_one_array(B, N, A)

# Create a Geomap
geomap = Geomap(cbar_type='tercile')

# Create a Geofield
levels = [-90, -80, -70, -60, -50, -40, -33, 33, 40, 50, 60, 70, 80, 90]
geofield = Geofield(data, geogrid, levels=levels, fill_colors=tmean_terciles)

# Plot the data
geomap.plot(geofield)

# Save the plot as an image
geomap.save('plot.png', dpi=200)
