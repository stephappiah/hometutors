//let autocomplete;
function initAutocomplete(){
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById('id_0-address'),
        {
            types: [],
            componentRestrictions: {'country': ['GH']},
            fields: ['place_id', 'geometry', 'name']
        }
    );
    autocomplete.addListener('place_changed', onPlaceChanged);
} 
function onPlaceChanged(){
    var place = autocomplete.getPlace();

    if (!place.geometry){
        //User did not selet a prediction; reset the input field --> id_0_address is id for search box
        document.getElementById('id_0-address').placeholder = 'Enter a location';
        // disable next button
        $('.savebtn').prop( "disabled", true);
        console.log('value empty');
    
    } else {
        //Get lon and lat of entered location
        var latitude = place.geometry.location.lat()
        var longitude = place.geometry.location.lng()
        //Convert to point value and prefill into the field (hidden from user)
        var point = `SRID=4326;POINT(${longitude} ${latitude})`
        $('#id_0-location').val(point);
        console.log(point)

        // enable next button on place clicked
        $('.savebtn').prop( "disabled", false);
        console.log('value not empty');
    }
}