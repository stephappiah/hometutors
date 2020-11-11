

function uploadToServer(compressedFile){

  const formElem = document.querySelector('form');
  formElem.addEventListener('formData', (e)=> {

    // on form submission, prevent default
    e.preventDefault();

    console.log(formElem);
 
   
    // construct a FormData object, which fires the formdata event
    let data = new FormData(formElem);

    // set value of profile picture to compressed file;
    data.append('4-avatar', compressedFile, 'compressedFileTesting');

    // Get the form data from the event object
    for (var value of data.values()) {
      console.log(value);
    }
    

    // submit the data via XHR
    let request = new XMLHttpRequest();
    request.open("POST", "/onboarding-tutor/");
    request.send(data);

  });

}

async function handleImageUpload(event) {
    
    const imageFile = event.target.files[0];
    console.log('originalFile instanceof Blob', imageFile instanceof Blob); // true
    console.log(`originalFile size ${imageFile.size / 1024 / 1024} MB`);
    
    const options = {
      maxSizeMB: 1,
      maxWidthOrHeight: 1920,
      useWebWorker: true
    };
    try {
      const compressedFile = await imageCompression(imageFile, options);
      console.log('compressedFile instanceof Blob', compressedFile instanceof Blob); // true
      console.log(`compressedFile size ${compressedFile.size / 1024 / 1024} MB`); // smaller than maxSizeMB
        
      uploadToServer(compressedFile); // write your own logic

      

      
    } catch (error) {
      console.log(error);
    }
   
  }