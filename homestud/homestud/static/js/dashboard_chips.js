
// first to initiate styling of chips
$(document).ready(function(){
    console.log('document ready function working!');

    // format currency --> rate input
    $("#id_tutor_profile-rate_per_hour").on({
        keyup: function() {
          formatCurrency($(this));
        },
        blur: function() { 
          formatCurrency($(this), "blur");
        }
    });

    // remove normal negotiable checkbox from dom; initiated before insert switch bcos it takes the id
    $( "#id_tutor_profile-negotiable" ).remove();

    // create switch button for negotiation btn
    $('<div class="switch"><label>Not negotiable<input type="checkbox" id="id_tutor_profile-negotiable" checked name="tutor_profile-negotiable"><span class="lever"></span>Negotiable</label></div>').insertAfter('#id_tutor_profile-rate_per_hour');

    // define variables
    const colorStyle = {
        "border":"2px solid #26a69a",
        "background-color":"#26a69a",
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

    // format input:rate with currency
    function formatNumber(n) {
        // format number 1000000 to 1,234,567
        return n.replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",")
      }
      
      
    function formatCurrency(input, blur) {
        // appends $ to value, validates decimal side
        // and puts cursor back in right position.
        
        // get input value
        var input_val = input.val();
        
        // don't validate empty input
        if (input_val === "") { return; }
        
        // original length
        var original_len = input_val.length;
        
        // initial caret position 
        var caret_pos = input.prop("selectionStart");
            
        // check for decimal
        if (input_val.indexOf(".") >= 0) {
        
            // get position of first decimal
            // this prevents multiple decimals from
            // being entered
            var decimal_pos = input_val.indexOf(".");
        
            // split number by decimal point
            var left_side = input_val.substring(0, decimal_pos);
            var right_side = input_val.substring(decimal_pos);
        
            // add commas to left side of number
            left_side = formatNumber(left_side);
        
            // validate right side
            right_side = formatNumber(right_side);
            
            // On blur make sure 2 numbers after decimal
            if (blur === "blur") {
            right_side += "00";
            }
            
            // Limit decimal to only 2 digits
            right_side = right_side.substring(0, 2);
        
            // join number by .
            input_val = "GHS" + " " + left_side + "." + right_side;
        
        } else {
            // no decimal entered
            // add commas to number
            // remove all non-digits
            input_val = formatNumber(input_val);
            input_val = "GHS" + " " + input_val;
            
            // final formatting
            if (blur === "blur") {
            input_val += ".00";
            }
        }
        
        // send updated string to input
        input.val(input_val);
        
        // put caret back in the right position
        var updated_len = input_val.length;
        caret_pos = updated_len - original_len + caret_pos;
        input[0].setSelectionRange(caret_pos, caret_pos);
    }

    // remove desktop form on mobile devices
    if (screen.width<=767) {
        //remove desktop form
        $('.lg-row-forms').remove();
        console.log('smaller screen');
       }
       else {
       //remove mobile form
       $('.mobile-forms').remove();
       console.log('larger screens');
    }
    // disable searchbar autocomplete
    // $('#search-bar-autocomplete').remove();
    // $('#search-bar-init').remove();
    // $(`<script src="${autocompleteSRC}"></script>`).insertAfter('#search-boxy');  

    // disable submit/update button when address box is clicked
    $('#id_personal_info-address').keyup(function(){
        // disable next button
        console.log('keyup');
        $(':submit').prop( "disabled", true);
        $('.helptext').css({'color': '#dc3545'});
    });

}); //end of document.ready function

// ------------------------------------------------------- On widow reload -----------------------------------------------------------------------------------------

window.onload = function () { 
    //---------------------------------   Style chips    ------------------------------------------------
    console.log('onload working!');
    // insert new google api 
    //$('<script id="newAutocomplete" src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCS3XC77YuRTTdhNn9AvdLWjJshRmsnoHk&libraries=places&callback=initAutocomplete" async defer></script>').insertAfter('#variableScripts');
    

            // define variables
    const colorStyle = {
        "border":"2px solid #26a69a",
        "background-color":"#26a69a",
        "color": "#fff",
        "transition": "all .2s"
        },
        defaultStyle = {
            "border":"2px solid rgba(139, 139, 139, .3)",
            "background-color":"rgba(255, 255, 255, .9)",
            "color": "#adadad",
            "transition": "all .2s"
        };
    
    
    // run a function to get all the ids of the class 
    // grab the id
    // check if it's checked or not, 
    // then style appropriately
    
    $('.chips_class_type').each(function (){

        var id = $(this).attr('id');
        var elemID = `#${id}`;
        var grabID = $(`${elemID}`);


        if (grabID.is(':checked')){
            grabID.closest('label').css(colorStyle);
        } else {
            grabID.closest('label').css(defaultStyle);
        }
    });


            // --------------------- Show or hide courses on reload ---------------------------

        function getProgName(courseID){
            // takes courseID and returns name of course
            return {
                'id_3-tutoring_programs_0': 'earlyCourses', 
                'id_3-tutoring_programs_1': 'primjhsCourses',
                'id_3-tutoring_programs_2': 'artCourses',
                'id_3-tutoring_programs_3': 'sciCourses',
                'id_3-tutoring_programs_4': 'vsaCourses',
                'id_3-tutoring_programs_5': 'busCourses',
                'id_3-tutoring_programs_6': 'hmeCourses',
                'id_3-tutoring_programs_7': 'tecCourses'
            }[courseID];
        }
    
        function getCourses(programme){
            // takes program as parameter and returns set of courses
            return {
                earlyCourses: $("#id_3-courses_subjects_0, #id_3-courses_subjects_1, #id_3-courses_subjects_2"),
                primjhsCourses: $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5"),
                artCourses: $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5, #id_3-courses_subjects_6, #id_3-courses_subjects_7, #id_3-courses_subjects_8, #id_3-courses_subjects_9, #id_3-courses_subjects_10, #id_3-courses_subjects_11, #id_3-courses_subjects_12"),
                sciCourses: $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5, #id_3-courses_subjects_13, #id_3-courses_subjects_14, #id_3-courses_subjects_15, #id_3-courses_subjects_28"),
                vsaCourses: $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5, #id_3-courses_subjects_16, #id_3-courses_subjects_17, #id_3-courses_subjects_18, #id_3-courses_subjects_19, #id_3-courses_subjects_20, #id_3-courses_subjects_21, #id_3-courses_subjects_22, #id_3-courses_subjects_23"),
                busCourses: $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5, #id_3-courses_subjects_24, #id_3-courses_subjects_25, #id_3-courses_subjects_26, #id_3-courses_subjects_27, #id_3-courses_subjects_28"),
                hmeCourses: $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5, #id_3-courses_subjects_29, #id_3-courses_subjects_30, #id_3-courses_subjects_31"),
                tecCourses: $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5")
            }[programme];
        }
    
    
        $('.chips_class_type').each(function(){
    
            var id = $(this).attr('id');
            var elemID = `#${id}`;
            var grabID = $(`${elemID}`);
    
            let prog = getProgName(id);
                // get set of courses from programme
            let courses = getCourses(prog);
            
            
            if (grabID.is(':checked')){ 
                // show courses
                courses.closest('label').css({
                    "display":"inline-block",   
                });
            } else {
                // Hide courses
                courses.closest('label').css({
                    "display":"none"
                });
            }
        });

           
        
        /* -------------------Courses Chips color styling -> onclick -------------------------------*/ 
    
};

