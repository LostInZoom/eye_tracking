document.getElementById("E1").onclick = function() {debut1()};
document.getElementById("E2").onclick = function() {debut2()};

var but = document.getElementById("but");
var map;
var div_image = document.getElementById("div_image");
var raster_g = new olgm.layer.Google();
var raster = new ol.layer.Tile({
  source: new ol.source.OSM(),
  visible: false
});
var numero_enquete;
var etape;
var etat_couche_g_osm;
/* Déclaration des couches*/
var couches = [raster,raster_g]; 
var zoom_couche = 19;  
var interval;
var tab= [];
/* Déclaration de la carte */
var olGM;
var etat_carte = 0;
function toggle() {
  if(numero_enquete ==2 && etape ==1 ){
    raster_g.setVisible(!raster_g.getVisible());
    // raster.setVisible(!raster.getVisible());
  }
  raster_g.setVisible(!raster_g.getVisible());
  raster.setVisible(!raster.getVisible());
};

function visible(event){
  if (event.code === 'Space'){
    if(etat_couche_g_osm[0]== true){
      raster_g.setVisible(!raster_g.getVisible());
      if(document.getElementById("image").style.visibility == 'hidden'){
        document.getElementById("image").style.visibility = 'visible';
        etat_carte = 1;
      }else{
        document.getElementById("image").style.visibility = 'hidden';
        etat_carte = 0;
      }
    }else{
      raster.setVisible(!raster.getVisible());
      if(document.getElementById("image").style.visibility == 'hidden'){
        document.getElementById("image").style.visibility = 'visible';
        etat_carte = 1;
      }else{
        document.getElementById("image").style.visibility = 'hidden';
        etat_carte = 0;
      }
    }

  }
}


// function visible(event){
//   if (event.code === 'Space'){

//     if(document.getElementById("image").style.visibility == 'hidden'){
//       document.getElementById("image").style.visibility = 'visible';
//       document.getElementById("map").style.visibility = 'hidden';

//       etat_carte = 1;
//     }else{
//       document.getElementById("image").style.visibility = 'hidden';
//       document.getElementById("map").style.visibility = 'visible';

//       etat_carte = 0;
//     }
//   }

  
// }

var l1 = new ol.layer.Vector({
  source: new ol.source.Vector({
      features: [
          new ol.Feature({
              geometry: new ol.geom.Point(ol.proj.fromLonLat([2.3383,48.8848]))
          })
      ]
  })
});
var l2 = new ol.layer.Vector({
  source: new ol.source.Vector({
      features: [
          new ol.Feature({
              geometry: new ol.geom.Point(ol.proj.fromLonLat([2.3325,48.8339]))
          })
      ]
  })
});
var l3 = new ol.layer.Vector({
  source: new ol.source.Vector({
      features: [
          new ol.Feature({
              geometry: new ol.geom.Point(ol.proj.fromLonLat([2.45797955479584,48.857993414174246]))
          })
      ]
  })
});
var l3bis = new ol.layer.Vector({
  source: new ol.source.Vector({
      features: [
          new ol.Feature({
              geometry: new ol.geom.Point(ol.proj.fromLonLat([2.3016,48.8878]))
          })
      ]
  })
});

function fin(){
  clearInterval(interval);

  let csvContent = "data:text/csv;charset=utf-8," +"time,zoom,xmin,ymin,xmax,ymax,etape,etat_carte\n"
    + tab.map(e => e.join(",")).join("\n");
  var encodedUri = encodeURI(csvContent);
  var link = document.createElement("a");
  link.setAttribute("href", encodedUri);
  let nom = "resultat_carte_" + numero_enquete +".csv"
  link.setAttribute("download", nom);
  document.body.appendChild(link); 
  link.click();
}
function etape10(){
  if(etat_carte == 0){
    but.removeChild(document.getElementById("etape10"));
    document.removeEventListener("keyup",visible)

    if(etat_couche_g_osm[0] == true){
      raster_g.setVisible(true);
    }else{
      raster.setVisible(true);
    }
    toggle();
    etat_couche_g_osm = [raster_g.getVisible(),raster.getVisible()]
    etat_carte = 1;
    etape +=1;
    map.getView().setCenter(ol.proj.fromLonLat([4.854357788402092,45.776679470458475]));
    map.getView().setZoom(10);
    div_image.removeChild(document.getElementById("image"));
    var im= $('<img src="image/lyon_bis.PNG" id="image">');
    var r= $('<button id="fin" onclick="fin()">fin</button>');
    $("#but").append(r);
    $("#div_image").append(im)


    document.getElementById("image").style.visibility == 'visible';
    if(raster_g.getVisible()== true){
      raster_g.setVisible(false);
    }else{
      raster.setVisible(false);
    }
    document.addEventListener('keyup',visible)  ;
  }
}
function etape9(){
  but.removeChild(document.getElementById("etape9"));
  toggle();
  etat_couche_g_osm = [raster_g.getVisible(),raster.getVisible()]
  etat_carte = 1;
  etape +=1;
  map.getView().setCenter(ol.proj.fromLonLat([2.1264,49.4565]));
  map.getView().setZoom(10);

  var im= $('<img src="image/beauvais.PNG" id="image">');
  var r= $('<button id="etape10" onclick="etape10()">etape 10</button>');
  $("#but").append(r);
  $("#div_image").append(im);


  //On ajoute un evenement afin de cacher la carte lorsqu'on regarde l'image
  document.getElementById("image").style.visibility == 'visible';
  if(raster_g.getVisible()== true){
    raster_g.setVisible(false);
  }else{
    raster.setVisible(false);
  }
  document.addEventListener('keyup',visible)  

}
function etape8(){
  but.removeChild(document.getElementById("etape8"));
  toggle();
  etape +=1;
  map.getView().setCenter(ol.proj.fromLonLat([-1.662480814879475,48.108134626125945]));
  map.getView().setZoom(12);

  
  var r= $('<button id="etape9" onclick="etape9()">etape 9</button>');
  

  $("#but").append(r);
}
function etape7(){
  if(etat_carte == 0){
    document.getElementById("map").style.visibility == 'visible';
    but.removeChild(document.getElementById("etape7"));
    document.removeEventListener("keyup",visible)
    etat_carte = 0;
    if(etat_couche_g_osm[0] == true){
      raster_g.setVisible(true);
    }else{
      raster.setVisible(true);
    }
    toggle();

    etat_couche_g_osm = [raster_g.getVisible(),raster.getVisible()]

    etape +=1;
    div_image.removeChild(document.getElementById("image"));
    map.getView().setCenter(ol.proj.fromLonLat([1.2594813185945888,45.827554711096525]));
    map.getView().setZoom(11);
 
    var r= $('<button id="etape8" onclick="etape8()">Etape 8</button>');
    $("#but").append(r);
    // document.getElementById("map").style.visibility == 'visible';
  }
}
function etape6(){
  if(etat_carte == 0){
      //document.getElementsByClassName("ol-viewport").style.visibility == 'visible';
    but.removeChild(document.getElementById("etape6"));
    if(etat_couche_g_osm[0] == true){
      raster_g.setVisible(true);
    }else{
      raster.setVisible(true);
    }

    toggle();
    etat_couche_g_osm = [raster_g.getVisible(),raster.getVisible()]
  // console.log(etat_couche_g_osm);

    etat_carte = 1;
    etape +=1;
    div_image.removeChild(document.getElementById("image"));
    map.getView().setCenter(ol.proj.fromLonLat([5.0426,47.3221]));
    map.getView().setZoom(11);
    document.removeEventListener("keyup",visible)


    var im= $('<img src="image/dijon.PNG" id="image">');
    var r= $('<button id="etape7" onclick="etape7()">Etape 7</button>');
    $("#but").append(r);
    $("#div_image").append(im);
    //On ajoute un evenement afin de cacher la carte lorsqu'on regarde l'image
    document.getElementById("image").style.visibility == 'visible';

  // document.getElementById("map").style.visibility == 'hidden';
    if(raster_g.getVisible()== true){
      raster_g.setVisible(false);
    }else{
      raster.setVisible(false);
    }
    document.addEventListener('keyup',visible)

  }
}
function etape5(){ 
  map.removeLayer(l3bis);
  toggle();
  etape +=1;
  but.removeChild(document.getElementById("etape5"));
  map.getView().setCenter(ol.proj.fromLonLat([4.854357788402092,45.776679470458475]));
  map.getView().setZoom(10);

  etat_couche_g_osm = [raster_g.getVisible(),raster.getVisible()];
  etat_carte = 1;

  var im= $('<img src="image/lyon.PNG" id="image">');
  var r= $('<button id="etape6" onclick="etape6()">Etape 6</button>');
  $("#but").append(r);
  $("#div_image").append(im);

  //On ajoute un evenement afin de cacher la carte lorsqu'on regarde l'image
  document.getElementById("image").style.visibility == 'visible';

  // document.getElementById("map").style.visibility == 'hidden';

  if(raster_g.getVisible()== true){
    raster_g.setVisible(false);
  }else{
    raster.setVisible(false);
  }
  document.addEventListener('keyup',visible)
  document.getElementById("etape6").disabled = false; 

}
function etape4(){
  but.removeChild(document.getElementById("etape4"));
  toggle();
  etape +=1;
  map.removeLayer(l3);
  map.addLayer(l3bis);
  map.getView().setCenter(ol.proj.fromLonLat([2.3016,48.8878]));
  map.getView().setZoom(zoom_couche);

  var r= $('<button id="etape5" onclick="etape5()">Etape 5</button>');
  $("#but").append(r);
}
function etape3(){
  but.removeChild(document.getElementById("etape_3"));
  toggle();
  etape +=1;
  map.removeLayer(l2);
  map.addLayer(l3);
  map.getView().setCenter(ol.proj.fromLonLat([2.45797955479584,48.857993414174246]));
  map.getView().setZoom(zoom_couche);

  var r= $('<button id="etape4" onclick="etape4()">Etape 4</button>');
  $("#but").append(r);
}
function etape2(){
  but.removeChild(document.getElementById("etape_2"));
  toggle();
  etape +=1;
  map.removeLayer(l1);
  map.addLayer(l2);
  map.getView().setCenter(ol.proj.fromLonLat([2.3325,48.8339]));
  map.getView().setZoom(zoom_couche);

  var r= $('<button id="etape_3" onclick="etape3()">Etape 3</button>');
  $("#but").append(r);
}


function ajout(){
  let date = Date.now()
  let zoom = map.getView().getZoom();
  let coord = map.getView().calculateExtent(map.getSize()); 
  tab.push([date,zoom,coord,etape,etat_carte])
}



function debut1() {
  but.removeChild(document.getElementById("E1"));
  but.removeChild(document.getElementById("E2"));
  numero_enquete = 1;
  etape = 1;
  map = new ol.Map({
    /* Appel des couches de la carte */
    interactions: olgm.interaction.defaults(),
    layers: couches,
    /* Cible de la div map */
    target: 'map',
    /* Caractéristiques de la vue de la carte */
    view: new ol.View({
        center: ol.proj.fromLonLat([2.3383,48.8848]),
        zoom: zoom_couche
    })
  });
  olGM = new olgm.OLGoogleMaps({map: map});
  olGM.activate();
  var r='<button id="etape_2" onclick="etape2()">Etape 2</button>';
  interval = setInterval(ajout, 100) ;
  $("#but").append(r);
  map.addLayer(l1);
  
}
function debut2() {
  but.removeChild(document.getElementById("E1"));
  but.removeChild(document.getElementById("E2"));
  numero_enquete = 2;
  etape = 1;
  
  map = new ol.Map({
    /* Appel des couches de la carte */
    interactions: olgm.interaction.defaults(),
    layers: couches,
    /* Cible de la div map */
    target: 'map',
    /* Caractéristiques de la vue de la carte */
    view: new ol.View({
        center: ol.proj.fromLonLat([2.3383,48.8848]),
        zoom: zoom_couche
    })
  });
  olGM = new olgm.OLGoogleMaps({map: map});
  olGM.activate();
  raster.setVisible(!raster.getVisible());

  var r='<button id="etape_2" onclick="etape2()">Etape 2</button>';
  interval = setInterval(ajout, 100) ;
  $("#but").append(r);
  map.addLayer(l1);
  
}






 