Getting Started
===============
In order to get started with GeoScanner, you'll need the following prerequites.


.. code:: python

    >>> import GeoScanner
    >>> gi = GeoScanner.GeoIP('GeoIP.dat')
    >>> gi.country_name_by_addr('64.233.161.99')
    'United States'

Country Lookup
--------------

.. code:: python

    >>> gi = GeoScanner.GeoIP('GeoIP.dat')
    >>> gi.country_code_by_name('google.com')
    'US'
    >>> gi.country_code_by_addr('64.233.161.99')
    'US'
    >>> gi.country_name_by_addr('64.233.161.99')
    'United States'

.. code:: python

    >>> gi = GeoScanner.GeoIP('GeoIPv6.dat')
    >>> gi.country_code_by_addr('2a00:1450:400f:802::1006')
    'IE'

Region Lookup
-------------

.. code:: python

    >>> gi = GeoScanner.GeoIP('GeoIPRegion.dat')
    >>> gi.region_by_name('apple.com')
    {'region_code': 'CA', 'country_code': 'US'}

City Lookup
-----------

.. code:: python

    >>> gi = GeoScanner.GeoIP('GeoIPCity.dat')
    >>> gi.record_by_addr('64.233.161.99')
    {
        'city': u'Mountain View',
        'region_code': u'CA',
        'area_code': 650,
        'time_zone': 'America/Los_Angeles',
        'dma_code': 807,
        'metro_code': 'San Francisco, CA',
        'country_code3': 'USA',
        'latitude': 37.41919999999999,
        'postal_code': u'94043',
        'longitude': -122.0574,
        'country_code': 'US',
        'country_name': 'United States',
        'continent': 'NA'
    }
    >>> gi.time_zone_by_addr('64.233.161.99')
    'America/Los_Angeles'

Organization Lookup
-------------------

.. code:: python

    >>> gi = GeoScanner.GeoIP('GeoIPOrg.dat')
    >>> gi.org_by_name('dell.com')
    'Dell Computer Corporation'

ISP Lookup
----------

.. code:: python

    >>> gi = GeoScanner.GeoIP('GeoIPISP.dat')
    >>> gi.isp_by_name('cnn.com')
    'Turner Broadcasting System'

ASN Lookup
----------

.. code:: python

    >>> gi = GeoScanner.GeoIP('GeoIPASNum.dat')
    >>> gi.asn_by_name('cnn.com')
    'AS5662 Turner Broadcasting'
