# -*- coding: utf-8 -*-
"""
obspy.segy - SEG Y and SU read and write support for ObsPy
==========================================================

The obspy.segy package contains methods in order to read and write seismogram
files in the SEG Y (rev. 1) and SU (Seismic Unix) format.

:copyright:
    The ObsPy Development Team (devs@obspy.org)
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)

Reading
-------
Importing SEG Y or SU files is done similar to reading any other waveform data
format within ObsPy by using the :func:`~obspy.core.stream.read()` method of
the :mod:`obspy.core` module. Examples seismograms files may be found at
http://examples.obspy.org.

>>> from obspy.core import read
>>> st = read("/path/to/00001034.sgy_first_trace")
>>> st #doctest: +ELLIPSIS
<obspy.core.stream.Stream object at 0x...>
>>> print(st)
1 Trace(s) in Stream:
Seq. No. in line:    1 | 2009-06-22T14:47:37.000000Z - 2009-06-22T14:47:41.000000Z | 500.0 Hz, 2001 samples

The file format will be determined automatically. Each trace (multiple channels
are mapped to multiple traces) will have a stats attribute containing the usual
information.

>>> print(st[0].stats) #doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
             network: 
             station: 
            location: 
             channel: 
           starttime: 2009-06-22T14:47:37.000000Z
             endtime: 2009-06-22T14:47:41.000000Z
       sampling_rate: 500.0
               delta: 0.002
                npts: 2001
               calib: 1.0
                segy: AttribDict({'textual_file_header': 'C 1 Instrument:  ...})
             _format: SEGY

The actual data is stored as numpy.ndarray in the data attribute of each trace.

>>> st[0].data #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
array([ -2.84501867e-11,  -5.32782846e-11,  -1.13144355e-10, ...,
        -4.55348870e-10,  -8.47760084e-10,  -7.45420170e-10], dtype=float32)

Writing
-------
Writing is also done in the usual way:

>>> st.write('file.segy', format = 'SEGY') #doctest: +SKIP

or 

>>> st.write('file.su', format = 'SU') #doctest: +SKIP
"""

from obspy.core.util import _getVersionString
from segy import readSEGY as readSEGY
from segy import readSU as readSU


__version__ = _getVersionString("obspy.segy")


if __name__ == '__main__':
    import doctest
    doctest.testmod(exclude_empty=True)
