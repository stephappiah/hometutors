

// this is for when document is fully loaded
// on reload function is found in onboard-tutor.html
$(document).ready(function(){
    
    // create a wordcount box after bio field
    $("<p class='wordCount'></p>").insertAfter('#id_2-bio');

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
            $('.wordCount').text('Done!');
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
    $("<p class='bioHelper'>You'll need to provide a brief description of yourself: your interest, education, and experience with your subjects.</p>").insertAfter('.wordCount');

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
            'id_3-tutoring_programs_5': 'primjhsCourses',
            'id_3-tutoring_programs_6': 'artCourses',
            'id_3-tutoring_programs_7': 'sciCourses',
            'id_3-tutoring_programs_8': 'vsaCourses',
            'id_3-tutoring_programs_9': 'busCourses',
            'id_3-tutoring_programs_10': 'hmeCourses',
            'id_3-tutoring_programs_11': 'tecCourses'
        }[courseID];
    }

    function getCourses(programme){
        // takes program as parameter and returns set of courses
        return {
            testPrepCourses: $("#id_3-courses_subjects_32, #id_3-courses_subjects_33, #id_3-courses_subjects_34"),
            musicCourses: $("#id_3-courses_subjects_35, #id_3-courses_subjects_36, #id_3-courses_subjects_37, #id_3-courses_subjects_38"),
            photographyCourses: $("#id_3-courses_subjects_39, #id_3-courses_subjects_40, #id_3-courses_subjects_41"),
            ITCourses: $("#id_3-courses_subjects_42, #id_3-courses_subjects_43, #id_3-courses_subjects_44 , #id_3-courses_subjects_45"),

            earlyCourses: $("#id_3-courses_subjects_0, #id_3-courses_subjects_1, #id_3-courses_subjects_2"),
            primjhsCourses: $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5"),
            artCourses: $("#id_3-courses_subjects_6, #id_3-courses_subjects_7, #id_3-courses_subjects_8, #id_3-courses_subjects_9, #id_3-courses_subjects_10, #id_3-courses_subjects_11, #id_3-courses_subjects_12"),
            sciCourses: $("#id_3-courses_subjects_13, #id_3-courses_subjects_14, #id_3-courses_subjects_15, #id_3-courses_subjects_28"),
            vsaCourses: $("#id_3-courses_subjects_16, #id_3-courses_subjects_17, #id_3-courses_subjects_18, #id_3-courses_subjects_19, #id_3-courses_subjects_20, #id_3-courses_subjects_21, #id_3-courses_subjects_22, #id_3-courses_subjects_23"),
            busCourses: $("#id_3-courses_subjects_24, #id_3-courses_subjects_25, #id_3-courses_subjects_26, #id_3-courses_subjects_27, #id_3-courses_subjects_28"),
            hmeCourses: $("#id_3-courses_subjects_29, #id_3-courses_subjects_30, #id_3-courses_subjects_31"),
            tecCourses: $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5")
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
 
}); //end of document.ready function

