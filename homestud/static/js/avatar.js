
$(document).ready(function (){
    // insert input element right before form
    $( '<input type="file" accept="image/*" id="imageInput" onchange="handleImageUpload(event); loadFile();" />' ).insertBefore( "#tutorForm" );

    // insert img element right before input file
    $( "<img id='previewAvatar' alt='your image' width='100' height='100' />" ).insertBefore( "#id_4-avatar" );
    // insert upload button
    $("<p style='display:block;width:120px; ' class='btn upload-btn text-center mint-bg' onclick='uploadImage()'>Upload</p>").insertAfter('#previewAvatar');

    $('#id_4-avatar').remove();

    

    // get default avatar's link from static folder
    var defaultIMG = '/static/img/avatar/no-avatar.png';
    // update img element's src
    document.getElementById('previewAvatar').src = defaultIMG;
});

function loadFile(){
    // get uploaded file onchange
    var imgURL = URL.createObjectURL(event.target.files[0]);
    // update img element's
    document.getElementById('previewAvatar').src = imgURL;

}

function uploadImage(){
    // click on input file button when upload button is pressed
    $('#imageInput').trigger('click');
    
}