


function uploadToServer(compressedFile){
  var submit = $('#submitTutor');
  var formElem = document.getElementById('tutorForm');
  var filename = username + '-' + date + '.png';

  function get_tutor_slug(){
    // send an ajax call to a view that fetches the current user's slug
    $.ajax({
      url: "/ajax/get_tutor_slug/",
      type: "GET",

      success: function(data){
          window.location.replace(`/tutor/${data}/review`);
          console.log(data);
          
      },

      error: function(){
        console.log('error')
      }
    });
  }
  submit.on('click', function (event){
    // prevent default send behaviour
    event.preventDefault();

    // disable btns on click --> to do: show loading spinner instead
    $('.btn').prop('disabled', true);
    // loading spinner
    $('<div class="text-center mt-3"><div class="spinner-border text-info" role="status"><span class="sr-only">Loading...</span></div></div>').insertAfter('.avatar');
    

    // Get the form data from the event object
    var form_data = new FormData(formElem);
    console.log(form_data);
    form_data.append('compressedImage', compressedFile,`${filename}`);
    for (var value of form_data.values()) {
      console.log(value);
    }

    
    // post form via ajax
    $.ajax({
      url: "/onboarding-tutor/",
      type: "POST",
      data: form_data,

      success: function(){
        console.log('Submitted successfully');
        // redirect users to share profile page
        get_tutor_slug();
        //window.location.replace("/share-profile");
        
      },

      error: function(){
        console.log('Submission failed!!');
        // enable btns on click --> to do: hide loading spinner instead
        $('.btn').prop('disabled', false);
        // remove loading spinner
        $('.spinner-border').addClass('d-none');
        // loading spinner
        $('<div class="trans-alert mt-2 text-center"><div class="alert alert-danger" role="alert">Upload failed. Please try again!</div></div>').insertAfter('.avatar');
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