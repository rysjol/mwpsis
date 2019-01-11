L.mapbox.accessToken = 'pk.eyJ1Ijoicnlzam9sIiwiYSI6ImNqcHJ5NzFjNDE2eTY0Mm8xMDduOHdueGkifQ.6tKMymWRw5IweYpqMLXKag' ;
var map = L.mapbox.map('map', 'mapbox.streets')
  .setView([52.03, 19.27], 6);

var id;
var startId = -1;
var stopId = -1;
var transitIDs = [];
var cities = L.mapbox.featureLayer()
  .loadURL('/js/cities.geojson')
  .on('ready', function() {
    map.fitBounds(cities.getBounds());
  })
  .addTo(map);

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
  transitIDs = [];
  document.getElementById('start_city').innerHTML = '';
  document.getElementById('stop_city').innerHTML = '';
  document.getElementById('transit_cities').innerHTML = '';
};

function optimize() {
  if(startId > -1 && stopId > -1 /*&& transitIDs != ''*/) {
    // alert('start: ' + startId + ', stop: ' + stopId/* +', transit: ' + transitIDs*/);
    $.ajax({
      url: "index.cgi?start=startId&stop=stopId",
    });
  } else {
    alert("Wybierz przynajmniej jeden punkt początkowy i końcowy.")
  }
};



  //var gdansk = L.marker([54.348590, 18.653259]).addTo(map);
  //var bydgoszcz = L.marker([53.121994, 18.000434]).addTo(map);
  //var kolobrzeg = L.marker([54.1762177, 15.574454]).addTo(map);
  //var katowice = L.marker([50.2590427, 19.0195338]).addTo(map);
  //var krakow = L.marker([50.0615991, 19.9351372]).addTo(map);
  //var bialystok = L.marker([53.1322542, 23.1585387]).addTo(map);
  //var lodz = L.marker([51.7811939, 19.452173]).addTo(map);
  //var poznan = L.marker([52.4082542, 16.9314281]).addTo(map);
  //var rzeszow = L.marker([50.037221,22.0033492]).addTo(map);
  //var szczecin = L.marker([53.4243505, 14.5576182]).addTo(map);
  //var warszawa = L.marker([52.2497413, 21.0100477]).addTo(map);
  //var wroclaw = L.marker([51.1106992, 17.0301722]).addTo(map);


//   gdansk.bindPopup("<b>Gdansk</b><br>Miasto o ID: 0").openPopup();
//   bydgoszcz.bindPopup("<b>Bydgoszcz</b><br>Miasto o ID: 1").openPopup();
//   kolobrzeg.bindPopup("<b>Kolobrzeg</b><br>Miasto o ID: 2").openPopup();
//   katowice.bindPopup("<b>Katowice</b><br>Miasto o ID: 3").openPopup();
//   krakow.bindPopup("<b>Krakow</b><br>Miasto o ID: 4").openPopup();
//   bialystok.bindPopup("<b>Bialystok</b><br>Miasto o ID: 5").openPopup();
//   lodz.bindPopup("<b>Lodz</b><br>Miasto o ID: 6").openPopup();
//   poznan.bindPopup("<b>Poznan</b><br>Miasto o ID: 7").openPopup();
//   rzeszow.bindPopup("<b>Rzeszow</b><br>Miasto o ID: 8").openPopup();
//   szczecin.bindPopup("<b>Szczecin</b><br>Miasto o ID: 9").openPopup();
//   warszawa.bindPopup("<b>Warszawa</b><br>Miasto o ID: 10").openPopup();
//   wroclaw.bindPopup("<b>Wroclaw</b><br>Miasto o ID: 11").openPopup();

// [19.9351372, 50.0615991] Krakow
// [23.1585387, 53.1322542] Bialystok
// [19.452173, 51.7811939] Lodz
// [16.9314281, 52.4082542] Poznan
// [22.0033492, 50.037221] Rzeszow
// [14.5576182, 53.4243505] Szczecin
// [21.0100477, 52.2497413] Warszawa
// [17.0301722, 51.1106992] Wroclaw