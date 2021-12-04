var lc = map;
var boxes = {
{
    boxes | safe
}
}
;
var olis = {
{
    olis | safe
}
}

var oilStyle = {
    "color": "#000",
    "weight": 5,
    "opacity": 0.65
};
var activeStyle = {
    "color": "#FFF",
    "weight": 5,
    "opacity": 0.65
};

$.each(boxes, function (index, value) {
    L.imageOverlay(value.imageUrl, value.imageBounds, {'interactive': true}).addTo(map);
})
$.each(olis, function (index, value) {

    L.geoJSON(value, {
            coordsToLatLng: function (coords) {
                return new L.LatLng(coords[0], coords[1]);
            },
            style: function (feature) {
                switch (feature.properties.party) {
                    case 'Republican':
                        return {color: "#ff0000"};
                    case 'Democrat':
                        return {color: "#0000ff"};
                }
            }
        }
    ).bindPopup(function (value) {
        return value.feature.properties['name'];
    }).addTo(map);
})