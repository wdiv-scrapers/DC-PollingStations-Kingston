from dc_base_scrapers.arcgis_scraper import ArcGisScraper


stations_url = "http://www6.kingston.gov.uk/ArcGISServer/rest/services/polling/polling_Districts_Stations/MapServer/0/query?geometry=&geometryType=esriGeometryPoint&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&objectIds=&where=OBJECTID+LIKE+%27%25%27&time=&returnCountOnly=false&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&orderByFields=OBJECTID&outSR=4326&outFields=*&f=pjson"
districts_url = "http://www6.kingston.gov.uk/ArcGISServer/rest/services/polling/polling_Districts_Stations/MapServer/1/query?text=&geometry=&geometryType=esriGeometryPolygon&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&objectIds=&where=OBJECTID+LIKE+%27%25%27&time=&returnCountOnly=false&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&orderByFields=OBJECTID&outSR=4326&outFields=*&f=pjson"
council_id = 'E09000021'


stations_scraper = ArcGisScraper(stations_url, council_id, 'latin-1', 'stations')
stations_scraper.scrape()
districts_scraper = ArcGisScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
