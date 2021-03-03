$(document).ready(function(){

    // insert input element right before form
    $( '<input type="file" accept="image/*" name="compressedImage" id="imageInput" onchange="handleImageUpload(event); loadFile();" />' ).insertBefore( ".avatarForm" );

    // insert img element right before input file
    $( "<img class='previewAvatar' alt='your image' onclick='uploadImage()' width='100' height='100' />" ).insertBefore( ".avatar" );
    // insert upload button
    $("<p style='display:block;width:120px; ' class='btn upload-btn text-center mint-bg' onclick='uploadImage()'>Browse Files</p>").insertAfter('.previewAvatar');
  
    var link = $('#avatarForm a').text();
    console.log(`/static/img/${link}`);

    var trialLink = $('a').attr('href');
    
    // get default avatar's link from static folder
    // var defaultIMG = avatarLink; //avatarLink is passed in profile-dashboard.html template
    // update img element's src
    $('.previewAvatar').attr('src', avatarLink); //hardcoded url of current user avatar
    console.log(avatarLink);
    

});

function uploadImage(){
    // click on input file button when upload button is pressed
    $('#imageInput').trigger('click');
    
}


// ------------------------------------------------      image compression goes here            ------------------------------------------------------




function uploadToServer(compressedFile){
    var submit = $('.avt-btn');
    // todo: upload only works on mobile version since form is different from desktop's
    var formElem = document.getElementById('avatarForm');
    var filename = username + '-' + date + '.png';
  
    submit.on('click', function (event){
      // prevent default send behaviour
      event.preventDefault();
  
      // disable btns on click --> to do: show loading spinner instead
      $('.btn').prop('disabled', true);
      // loading spinner
      $('<div class="text-center mt-3"><div class="spinner-border text-info" role="status"><span class="sr-only">Loading...</span></div></div>').insertAfter('.avatar')
      
  
      // Get the form data from the event object
      var data = new FormData(formElem);
      data.append('compressedImage', compressedFile,`${filename}`);
      for (var value of data.values()) {
        console.log(value);
      }
  
      
      // post form via ajax
      $.ajax({
        url: "/dashboard/profile",
        type: "POST",
        data: data,
  
        success: function(){
          console.log('Submitted successfully');
          // redirect users to share profile page
          window.location.reload();
        },
  
        error: function(){
          console.log('Submission failed!!');
        },
  
        cache: false,
        contentType: false,
        processData: false
    })
      // end of ajax
    }); //end of onsubmit
    
  } //end of upload-to-server func
  
  
  // function previews compressed image to user
  function loadFile(compressedFile){
    // get uploaded file onchange
    var imgURL = URL.createObjectURL(compressedFile);
    // update img element's
    $('.previewAvatar').attr('src', imgURL);
  
  }
  
  async function handleImageUpload(event) {
      
      const imageFile = event.target.files[0];
      console.log('originalFile instanceof Blob', imageFile instanceof Blob); // true
      console.log(`originalFile size ${imageFile.size / 1024 / 1024} MB`);
      
      const options = {
        maxSizeMB: 0.2,
        maxWidthOrHeight: 1920,
        onProgress: onProgress,
        useWebWorker: true
      };
  
      function onProgress(p){
        // if p is not 100, load spinner
        if (p != 100){
          // load spinner...spinner variable is set in a script at oboard-tutor.html
          $('.previewAvatar').attr('src', '/static/img/spinner.gif');
          
          // disable submit button
          $('#avt-btn').attr("disabled", true);
        } else{
          // enable submit button after img compression is done.
          $('#avt-btn').removeAttr("disabled");
        }
  
      }
  
      try {
        const compressedFile = await imageCompression(imageFile, options);
        console.log('compressedFile instanceof Blob', compressedFile instanceof Blob); // true
        console.log(`compressedFile size ${compressedFile.size / 1024 / 1024} MB`); // smaller than maxSizeMB
          
        await loadFile(compressedFile);
        await uploadToServer(compressedFile); // write your own logic
  
        
      } catch (error) {
        console.log(error);
  
      }
     
    }