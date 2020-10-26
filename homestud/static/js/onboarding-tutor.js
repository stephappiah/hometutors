// Rewriting this script


// first to initiate styling of chips
$(document).ready(function(){
    // define variables
    const colorStyle = {
        "border":"2px solid #1bdbf8",
        "background-color":"#12bbd4",
        "color": "#fff",
        "transition": "all .2s"
        },
        defaultStyle = {
            "border":"2px solid rgba(139, 139, 139, .3)",
            "background-color":"rgba(255, 255, 255, .9)",
            "color": "#adadad",
            "transition": "all .2s"
        };
    
    
    // when class-->'chips_class_type' is clicked
    // grab the id
    // check if it's checked or not, 
    // then style appropriately

    $('.chips_class_type').click(function(){

        var id = $(this).attr('id');
        var elemID = `#${id}`;
        var grabID = $(`${elemID}`);

        if (grabID.is(':checked')){
            grabID.closest('label').css(colorStyle);
        } else {
            grabID.closest('label').css(defaultStyle);
        }
    });
 
}); //end of document.ready function

