$(document).ready(function(){


    // ----------------------------- highlight (style) chips on click ------------------------------------// 
    // define variables
    var colorStyle = {
        "border":"2px solid #17a2b8",
        "background-color":"#17a2b8",
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
            'id_programs_0': 'musicCourses',
            'id_programs_1': 'photographyCourses',
            'id_programs_2': 'ITCourses',
            'id_programs_3': 'testPrepCourses',
            'id_programs_4': 'earlyCourses', 
            'id_programs_5': 'coreCourses',
            'id_programs_6': 'artCourses',
            'id_programs_7': 'sciCourses',
            'id_programs_8': 'vsaCourses',
            'id_programs_9': 'busCourses',
            'id_programs_10': 'hmeCourses',
            'id_programs_11': 'tecCourses',
            'id_programs_12': 'languages',
        }[courseID];
    }

    function getCourses(programme){
        // takes program as parameter and returns set of courses
        return {
            testPrepCourses: $("#id_subjects_34, #id_subjects_35, #id_subjects_36, #id_subjects_37, #id_subjects_38, #id_subjects_39"),
            musicCourses: $("#id_subjects_40, #id_subjects_41, #id_subjects_42, #id_subjects_43, #id_subjects_44, #id_subjects_45"),
            photographyCourses: $("#id_subjects_46, #id_subjects_47, #id_subjects_48"),
            ITCourses: $("#id_subjects_49, #id_subjects_50, #id_subjects_51, #id_subjects_52, #id_subjects_53, #id_subjects_54, #id_subjects_55, #id_subjects_56"),

            earlyCourses: $("#id_subjects_0, #id_subjects_1, #id_subjects_2"),
            coreCourses: $("#id_subjects_3, #id_subjects_4, #id_subjects_5, #id_subjects_6, #id_subjects_7"),
            artCourses: $("#id_subjects_8, #id_subjects_9, #id_subjects_10, #id_subjects_11, #id_subjects_12, #id_subjects_13, #id_subjects_14"),
            sciCourses: $("#id_subjects_15, #id_subjects_16, #id_subjects_17"),
            vsaCourses: $("#id_subjects_18, #id_subjects_19, #id_subjects_20, #id_subjects_21, #id_subjects_22, #id_subjects_23, #id_subjects_24, #id_subjects_25"),
            busCourses: $("#id_subjects_26, #id_subjects_27, #id_subjects_28, #id_subjects_29, #id_subjects_30"),
            hmeCourses: $("#id_subjects_31, #id_subjects_32, #id_subjects_33"),
            tecCourses: $(""),
            languages: $("#id_subjects_3, #id_subjects_57, #id_subjects_58, #id_subjects_59, #id_subjects_60, #id_subjects_61, #id_subjects_62"),

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


    // format currency --> rate input
    $("#id_price").on({
        keyup: function() {
          formatCurrency($(this));
        },
        blur: function() { 
          formatCurrency($(this), "blur");
          
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
})

