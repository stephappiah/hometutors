


function uploadToServer(compressedFile){
  var submit = $('#submitTutor');
  var formElem = document.querySelector('form');
  var filename = username + '-' + date + '.png';

  submit.on('click', function (event){
    // prevent default send behaviour
    event.preventDefault();

    // disable btns on click --> to do: show loading spinner instead
    $('.btn').prop('disabled', true);
    

    // Get the form data from the event object
    var data = new FormData(formElem);
    data.append('compressedImage', compressedFile,`${filename}`);
    for (var value of data.values()) {
      console.log(value);
    }

    
    // post form via ajax
    $.ajax({
      url: "/onboarding-tutor/",
      type: "POST",
      data: data,

      success: function(){
        console.log('Submitted successfully');
        // redirect to dashboard
        window.location.replace("/dashboard/profile");
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
  document.getElementById('previewAvatar').src = imgURL;

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
        document.getElementById('previewAvatar').src = '/static/img/spinner.gif';
        
        // disable submit button
        $('#submitTutor').attr("disabled", true);
      } else{
        // enable submit button after img compression is done.
        $('#submitTutor').removeAttr("disabled");
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