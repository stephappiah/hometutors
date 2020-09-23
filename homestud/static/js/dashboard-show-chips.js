


$(document).ready(function(){

    const early = $('#id_interest-tutoring_programs_0'), 
      prjhs = $('#id_interest-tutoring_programs_1'),
      art = $('#id_interest-tutoring_programs_2'),
      sci = $('#id_interest-tutoring_programs_3'),
      vsa = $('#id_interest-tutoring_programs_4'),
      bus = $('#id_interest-tutoring_programs_5'),
      hme = $('#id_interest-tutoring_programs_6'),
      tec = $('#id_interest-tutoring_programs_7');
    
    // list of courses under programme
    const earlyCourses = $("#id_interest-courses_subjects_0, #id_interest-courses_subjects_1, #id_interest-courses_subjects_2"),
        primjhsCourses = $("#id_interest-courses_subjects_3, #id_interest-courses_subjects_4, #id_interest-courses_subjects_5"),
        artCourses = $("#id_interest-courses_subjects_3, #id_interest-courses_subjects_4, #id_interest-courses_subjects_5, #id_interest-courses_subjects_6, #id_interest-courses_subjects_7, #id_interest-courses_subjects_8, #id_interest-courses_subjects_9, #id_interest-courses_subjects_10, #id_interest-courses_subjects_11, #id_interest-courses_subjects_12"),
        sciCourses = $("#id_interest-courses_subjects_3, #id_interest-courses_subjects_4, #id_interest-courses_subjects_5, #id_interest-courses_subjects_13, #id_interest-courses_subjects_14, #id_interest-courses_subjects_15, #id_interest-courses_subjects_28"),
        vsaCourses = $("#id_interest-courses_subjects_3, #id_interest-courses_subjects_4, #id_interest-courses_subjects_5, #id_interest-courses_subjects_16, #id_interest-courses_subjects_17, #id_interest-courses_subjects_18, #id_interest-courses_subjects_19, #id_interest-courses_subjects_20, #id_interest-courses_subjects_21, #id_interest-courses_subjects_22, #id_interest-courses_subjects_23"),
        busCourses = $("#id_interest-courses_subjects_3, #id_interest-courses_subjects_4, #id_interest-courses_subjects_5, #id_interest-courses_subjects_24, #id_interest-courses_subjects_25, #id_interest-courses_subjects_26, #id_interest-courses_subjects_27, #id_interest-courses_subjects_28"),
        hmeCourses = $("#id_interest-courses_subjects_3, #id_interest-courses_subjects_4, #id_interest-courses_subjects_5, #id_interest-courses_subjects_29, #id_interest-courses_subjects_30, #id_3-courses_subjects_32");
    
    // if Early program is clicked show/hide related courses
    early.click(function() {
        // if chips is checked -- show courses
        if (early.is(':checked')){
            // show courses
            earlyCourses.closest('label').css({
                "display":"inline-block",   
            });
        } else {
            // hide courses
            earlyCourses.closest('label').css({
                "display":"none"
            });
    
        }
    }); 

    // if primary/jhs is clicked show/hide related courses
    prjhs.click(function() {
        // if chips is checked -- show courses
        if (prjhs.is(':checked')){
            // show courses
            primjhsCourses.closest('label').css({
                "display":"inline-block",
                    
            });
        } else {
            // Hide courses
            primjhsCourses.closest('label').css({
                "display":"none",
            });
    
        }
    }); 

    // if art is clicked show/hide related courses
    art.click(function() {
        // if chips is checked -- show courses
        if (art.is(':checked')){
            // show courses
            artCourses.closest('label').css({
                "display":"inline-block",
                    
            });
        } else {
            // Hide courses
            artCourses.closest('label').css({
                "display":"none",
            });
    
        }
    }); 

    // if sci is clicked show/hide related courses
    sci.click(function() {
        // if chips is checked -- show courses
        if (sci.is(':checked')){
            // show courses
            sciCourses.closest('label').css({
                "display":"inline-block",
                    
            });
        } else {
            // Hide courses
            sciCourses.closest('label').css({
                "display":"none",
            });
    
        }
    }); 

    // if vsa is clicked show/hide related courses
    vsa.click(function() {
        // if chips is checked -- show courses
        if (vsa.is(':checked')){
            // show courses
            vsaCourses.closest('label').css({
                "display":"inline-block",
                    
            });
        } else {
            // Hide courses
            vsaCourses.closest('label').css({
                "display":"none",
            });
    
        }
    }); 

    // if vsa is clicked show/hide related courses
    bus.click(function() {
        // if chips is checked -- show courses
        if (bus.is(':checked')){
            // show courses
            busCourses.closest('label').css({
                "display":"inline-block",
                    
            });
        } else {
            // Hide courses
            busCourses.closest('label').css({
                "display":"none",
            });
    
        }
    }); 

    // if vsa is clicked show/hide related courses
    hme.click(function() {
        // if chips is checked -- show courses
        if (hme.is(':checked')){
            // show courses
            hmeCourses.closest('label').css({
                "display":"inline-block",
                    
            });
        } else {
            // Hide courses
            hmeCourses.closest('label').css({
                "display":"none",
            });
    
        }
    }); 

}); //end of document.ready function