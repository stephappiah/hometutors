
$(document).ready(function (){
    // insert input element right before form
    $( '<input type="file" accept="image/*" name="compressedImage" id="imageInput" onchange="handleImageUpload(event); loadFile();" />' ).insertBefore( "#tutorForm" );

    // insert img element right before input file
    $( "<img id='previewAvatar' alt='your image' onclick='uploadImage()' width='100' height='100' />" ).insertBefore( "#id_4-avatar" );
    // insert upload button
    $("<p style='display:block;width:120px; ' class='btn upload-btn text-center mint-bg' onclick='uploadImage()'>Upload</p>").insertAfter('#previewAvatar');

    // get default avatar's link from static folder
    var defaultIMG = '/static/img/avatar/no-avatar.png';
    // update img element's src
    document.getElementById('previewAvatar').src = defaultIMG;

    // checks if input file field is empty;
    // then disables the submit button.
    if ($('#imageInput').get(0).files.length === 0) {
        console.log("No files selected.");

        // disable submit button
        $('#submitTutor').attr("disabled", true);
    }

});


function uploadImage(){
    // click on input file button when upload button is pressed
    $('#imageInput').trigger('click');
    
}