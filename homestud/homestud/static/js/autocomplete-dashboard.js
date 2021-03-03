//let autocomplete;
function initAutocomplete(){
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById('id_personal_info-address'),
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
        document.getElementById('id_personal_info-address').placeholder = 'Enter a location';
        // disable next button
        $(':submit').prop( "disabled", true);
        console.log('value empty');
    
    } else {
        //Get lon and lat of entered location
        var latitude = place.geometry.location.lat()
        var longitude = place.geometry.location.lng()
        //Convert to point value and prefill into the field (hidden from user)
        var point = `SRID=4326;POINT(${longitude} ${latitude})`
        $('#id_personal_info-location').val(point);
        console.log(point)

        // enable next button on place clicked
        $(':submit').prop( "disabled", false);
        // style helptext with green
        $('.helptext').css({'color': '#6c757d'});
        console.log('value not empty');
    }
}

