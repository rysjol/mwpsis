L.mapbox.accessToken = 'pk.eyJ1Ijoicnlzam9sIiwiYSI6ImNqcHJ5NzFjNDE2eTY0Mm8xMDduOHdueGkifQ.6tKMymWRw5IweYpqMLXKag' ;
var map = L.mapbox.map('map', 'mapbox.streets')
  .setView([52.03, 19.27], 6);

var id;
var startId = -1;
var stopId = -1;
var transitIDs = [];
var loadSize = 0;
var cities = L.mapbox.featureLayer()
  .loadURL('/js/cities.geojson')
  .on('ready', function() {
    map.fitBounds(cities.getBounds());
  })
  .addTo(map);

var links = L.mapbox.featureLayer();

cities.on('click',function(e) {
  id = e.layer.feature.properties.id;
  e.layer.bindPopup(e.layer.feature.properties.popupContent
    + '<button class="start">Ustaw jako punkt startowy</button>'
    + '<button class="transit">Ustaw jako punkt tranzytowy</button>'
    + '<button class="stop">Ustaw jako punkt końcowy</button>'
    );
  return id;
});

$('#map').on('click', '.start', id, function() {
  startId = id;
  if(startId == stopId) {
    stopId = -1;
    document.getElementById('stop_city').innerHTML = '';
  }; 
  if(transitIDs.indexOf(startId) > -1) {
    transitIDs.splice(transitIDs.indexOf(startId), 1);
    document.getElementById('transit_cities').innerHTML = transitIDs;
  };
  document.getElementById('start_city').innerHTML = startId;
});

$('#map').on('click', '.stop', id, function() {
  stopId = id;
  if(stopId == startId) {
    startId = -1;
    document.getElementById('start_city').innerHTML = '';
  }; 
  if(transitIDs.indexOf(stopId) > -1) {
    transitIDs.splice(transitIDs.indexOf(stopId), 1);
    document.getElementById('transit_cities').innerHTML = transitIDs;
  };
  document.getElementById('stop_city').innerHTML = stopId;
});

$('#map').on('click', '.transit', id, function() {
  if(id == startId) {
    startId = -1;
    document.getElementById('start_city').innerHTML = '';
  };   
  if(id == stopId) {
    stopId = -1;
    document.getElementById('stop_city').innerHTML = '';
  }; 
  if(transitIDs.indexOf(id) > -1) {
    transitIDs.splice(transitIDs.indexOf(id), 1);
    document.getElementById('transit_cities').innerHTML = transitIDs;
  };
  transitIDs.push(id);
  document.getElementById('transit_cities').innerHTML = transitIDs;
});

document.getElementById('reset').onclick = reset;
document.getElementById('optimize').onclick = optimize;

function reset() {
  startId = -1;
  stopId = -1;
  loadSize = -1;
  transitIDs = [];
  document.getElementById('start_city').innerHTML = '';
  document.getElementById('stop_city').innerHTML = '';
  document.getElementById('transit_cities').innerHTML = '';
  document.getElementById('load_size').value = '';
  if (map.hasLayer(links)) {
    map.removeLayer(links);
  }
};

function optimize() {
  if(startId > -1 && stopId > -1 /*&& transitIDs != ''*/) {
    loadSize = document.getElementById('load_size').value;
    if (loadSize > 0 && loadSize != '') {
    // alert('start: ' + startId + ', stop: ' + stopId/* +', transit: ' + transitIDs*/);
      $.ajax({
        url: "getids.cgi?start=" + startId + "&stop=" + stopId + "&load=" + loadSize,
        success: function(response) {
          alert(response);
          links.loadURL('/js/links.geojson')
          .on('ready', function() {
            map.fitBounds(links.getBounds());
          })
          .addTo(map);
        }
      });
    } else {
      alert("Podaj wielkość ładunku.");  
    }
  } else {
    alert("Wybierz przynajmniej jeden punkt początkowy i końcowy.")
  }
};