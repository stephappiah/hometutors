

function uploadToServer(compressedFile){

  var formElem = document.querySelector('form');
  var submit = document.querySelector('#submitTutor');
  
  submit.addEventListener('click', function (e){

    // Get the form data from the event object
    var data = new FormData(formElem);
    data.append('compressedImage', compressedFile, 'compressedFile.png');
    for (var value of data.values()) {
      console.log(value);
    }
    
    // submit the data via XHR
    var request = new XMLHttpRequest();
    request.open("POST", "/onboarding-tutor/", true);

    request.send(data);

    e.preventDefault();

  });

}

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
      maxSizeMB: 1,
      maxWidthOrHeight: 1920,
      onProgress: onProgress,
      useWebWorker: true
    };

    function onProgress(p){
      // if p is not 100, load spinner
      if (p != 100){

        document.getElementById('previewAvatar').src = spinner;
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