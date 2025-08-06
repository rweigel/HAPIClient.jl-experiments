# Python 2.7 and 3 compatible
# Report software bugs/issues/feature requests at
# https://github.com/hapi-server/client-python/issues
# Report data server issues to rweigel@gmu.edu

# Install latest hapiclient package from https://pypi.org/project/hapiclient/
# Only needs to be executed once.
import os; print(os.popen('pip install hapiclient --upgrade').read())

from hapiclient import hapi

server     = 'https://hapi-server.org/servers/TestData2.0/hapi'
dataset    = 'dataset1'
# Notes:
# 1. Use parameters='' to request all parameters from dataset1.
# 2. Multiple parameters can be requested using a comma-separated
#    list, e.g., parameters='scalar,scalarint'
parameters = 'scalar'
start      = '1970-01-01T00:00:00Z' # min 1970-01-01Z
stop       = '1970-01-01T00:00:30Z' # max 2016-12-31Z

data, meta = hapi(server, dataset, parameters, start, stop)

import pdb; pdb.set_trace()  # Set a breakpoint to inspect data and meta
print(meta)
print(data['Time'])
#import os; print(os.popen('pip install hapiplot --upgrade').read())
#from hapiplot import hapiplot
#hapiplot(data, meta)

# Notes:
# 1. To convert ISO 8601 strings the primary time parameter to Python
#    datetimes, use
#      from hapiclient import hapitime2datetime
#      time_name = meta["parameters"][0]["name"] # Primary time parameter is always first.
#      Time = hapitime2datetime(data[time_name])
# 2. Details about the data and metadata structures `data`
#    and `meta` are given at 
#    https://github.com/hapi-server/client-python-notebooks/blob/master/hapi_demo.ipynb
# 3. Many examples for using `data` and `meta` with other
#    Python libraries (e.g., Pandas, Numpy, Astropy) are given
#    in above-referenced notebook.