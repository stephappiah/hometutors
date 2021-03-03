

// this is for when document is fully loaded
// on reload function is found in onboard-tutor.html
$(document).ready(function(){
    
    // disable searchbar autocomplete
    $('#search-bar-autocomplete').remove();
    $('#search-bar-init').remove();
    $(`<script src="${autocompleteSRC}"></script>`).insertAfter('#search-boxy'); 
    
    // create a wordcount box after bio field
    $("<p class='wordCount'></p>").insertAfter('#id_2-bio');

    // format currency --> rate input
    $("#id_2-rate_per_hour").on({
        keyup: function() {
          formatCurrency($(this));
        },
        blur: function() { 
          formatCurrency($(this), "blur");
        }
    });

    // remove normal negotiable checkbox from dom; initiated before insert switch bcos it takes the id
    $( "#id_2-negotiable" ).remove();

    // create switch button for negotiation btn
    $('<div class="switch"><label>Not negotiable<input type="checkbox" id="id_2-negotiable" checked name="2-negotiable"><span class="lever"></span>Negotiable</label></div>').insertAfter('#id_2-rate_per_hour');
    
    //-------disable cut,copy,paste on bio field
    $('#id_2-bio').bind('copy paste cut',function(e) { 
        e.preventDefault();
    })
    
    //-------------------- start counting on key pressed ------------------------//
    var wordLen = 40,
        len; // Maximum word length
    $('#id_2-bio').keydown(function(event) {	
        len = $('#id_2-bio').val().split(/[\s]+/);
    
        wordsLeft = (wordLen) - len.length;

        // display words left in wordcount box
        if (wordsLeft === 1){
            $('.wordCount').text(wordsLeft + ' word left');
        }else{
            $('.wordCount').text(wordsLeft + ' words left');
        }
        

        // change box color when word count <= 0
        if (wordsLeft <= 0){
            $('.wordCount').css({
                'background-color': '#2c9176',
                'color': 'white'
            });
            $('.wordCount').text("You're good to go!");
            $('.savebtn').prop( "disabled", false );
        } else {
            $('.wordCount').css({
                'background-color': '#343a40',
                'color': 'white'
            });
            $('.savebtn').prop( "disabled", true );
        }
        
    });

    // ------ Bio description helper --------------//
    $("<p class='bioHelper'>You'll need to provide a brief description of yourself: your interest, education, and experience with teaching your subjects.</p>").insertAfter('.wordCount');

    // ----------------------------- highlight (style) chips on click ------------------------------------// 
    // define variables
    const colorStyle = {
        "border":"2px solid #1ba883",
        "background-color":"#1ba883",
        "color": "#fff",
        "transition": "all .2s"
        },
        defaultStyle = {
            "border":"2px solid rgba(139, 139, 139, .3)",
            "background-color":"rgba(255, 255, 255, .9)",
            "color": "#555555",
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


    // ----------------------------- show or hide courses chips based on program clicked ------------------------------------// 

    function getProgName(courseID){
        // takes courseID and returns name of course
        return {
            'id_3-tutoring_programs_0': 'musicCourses',
            'id_3-tutoring_programs_1': 'photographyCourses',
            'id_3-tutoring_programs_2': 'ITCourses',
            'id_3-tutoring_programs_3': 'testPrepCourses',
            'id_3-tutoring_programs_4': 'earlyCourses', 
            'id_3-tutoring_programs_5': 'coreCourses',
            'id_3-tutoring_programs_6': 'artCourses',
            'id_3-tutoring_programs_7': 'sciCourses',
            'id_3-tutoring_programs_8': 'vsaCourses',
            'id_3-tutoring_programs_9': 'busCourses',
            'id_3-tutoring_programs_10': 'hmeCourses',
            'id_3-tutoring_programs_11': 'tecCourses',
            'id_3-tutoring_programs_12': 'languages',
        }[courseID];
    }

    function getCourses(programme){
        // takes program as parameter and returns set of courses
        return {
            testPrepCourses: $("#id_3-courses_subjects_34, #id_3-courses_subjects_35, #id_3-courses_subjects_36, #id_3-courses_subjects_37, #id_3-courses_subjects_38, #id_3-courses_subjects_39"),
            musicCourses: $("#id_3-courses_subjects_40, #id_3-courses_subjects_41, #id_3-courses_subjects_42, #id_3-courses_subjects_43, #id_3-courses_subjects_44, #id_3-courses_subjects_45"),
            photographyCourses: $("#id_3-courses_subjects_46, #id_3-courses_subjects_47, #id_3-courses_subjects_48"),
            ITCourses: $("#id_3-courses_subjects_49, #id_3-courses_subjects_50, #id_3-courses_subjects_51, #id_3-courses_subjects_52, #id_3-courses_subjects_53, #id_3-courses_subjects_54, #id_3-courses_subjects_55, #id_3-courses_subjects_56"),

            earlyCourses: $("#id_3-courses_subjects_0, #id_3-courses_subjects_1, #id_3-courses_subjects_2"),
            coreCourses: $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5, #id_3-courses_subjects_6, #id_3-courses_subjects_7"),
            artCourses: $("#id_3-courses_subjects_8, #id_3-courses_subjects_9, #id_3-courses_subjects_10, #id_3-courses_subjects_11, #id_3-courses_subjects_12, #id_3-courses_subjects_13, #id_3-courses_subjects_14"),
            sciCourses: $("#id_3-courses_subjects_15, #id_3-courses_subjects_16, #id_3-courses_subjects_17"),
            vsaCourses: $("#id_3-courses_subjects_18, #id_3-courses_subjects_19, #id_3-courses_subjects_20, #id_3-courses_subjects_21, #id_3-courses_subjects_22, #id_3-courses_subjects_23, #id_3-courses_subjects_24, #id_3-courses_subjects_25"),
            busCourses: $("#id_3-courses_subjects_26, #id_3-courses_subjects_27, #id_3-courses_subjects_28, #id_3-courses_subjects_29, #id_3-courses_subjects_30"),
            hmeCourses: $("#id_3-courses_subjects_31, #id_3-courses_subjects_32, #id_3-courses_subjects_33"),
            tecCourses: $(""),
            languages: $("#id_3-courses_subjects_3, #id_3-courses_subjects_57, #id_3-courses_subjects_58, #id_3-courses_subjects_59, #id_3-courses_subjects_60, #id_3-courses_subjects_61, #id_3-courses_subjects_62"),

        }[programme];
    }


    $('.chips_class_type').click(function(){

        var id = $(this).attr('id');
        var elemID = `#${id}`;
        var grabID = $(`${elemID}`);
            
        
        if (grabID.is(':checked')){ 

            let prog = getProgName(id);
            // get set of courses from programme
            let courses = getCourses(prog);
            // show courses
            courses.closest('label').css({
                "display":"inline-block",   
            });
        } else {

            let prog = getProgName(id);
            // get set of courses from programme
            let courses = getCourses(prog);
            // Hide courses
            courses.closest('label').css({
                "display":"none"
            });
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
 
}); //end of document.ready function

