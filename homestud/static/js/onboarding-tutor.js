
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
        },
        individualChips = $('#id_2-class_type_0'),
        groupChips = $('#id_2-class_type_1'),
        onlineChips = $('#id_2-class_type_2');
        
    // chip id 0 for class-type
    individualChips.click(function() {
        
        if (individualChips.is(':checked')){
            // if checkbox checked, style with color
            individualChips.closest('label').css(colorStyle);
        } else {
            // else restore default style
            individualChips.closest('label').css(defaultStyle);
        }
    }); 

    // chip id 1 for class-type
    groupChips.click(function() {
       
        if (groupChips.is(':checked')){
            groupChips.closest('label').css(colorStyle);
        } else {
    
            groupChips.closest('label').css(defaultStyle);
    
        }
    }); 

    // chip id  for class-type
    onlineChips.click(function() {
        if (onlineChips.is(':checked')){
            
            onlineChips.closest('label').css(colorStyle);
        } else {
    
            onlineChips.closest('label').css(defaultStyle);
    
        }
    }); 

    // programme chips variables 
    const early = $('#id_3-tutoring_programs_0'), 
      prjhs = $('#id_3-tutoring_programs_1'),
      art = $('#id_3-tutoring_programs_2'),
      sci = $('#id_3-tutoring_programs_3'),
      vsa = $('#id_3-tutoring_programs_4'),
      bus = $('#id_3-tutoring_programs_5'),
      hme = $('#id_3-tutoring_programs_6'),
      tec = $('#id_3-tutoring_programs_7');
    
    // style early years chips on click
    early.click(function() {
        if (early.is(':checked')){
            
            early.closest('label').css(colorStyle);
        } else {
    
            early.closest('label').css(defaultStyle);
    
        }
    
    }); 

    // style prjhs chips on click
    prjhs.click(function() {
        if (prjhs.is(':checked')){
            
            prjhs.closest('label').css(colorStyle);
        } else {
    
            prjhs.closest('label').css(defaultStyle);
    
        }
    
    });
    
    // style art chips on click
    art.click(function() {
        if (art.is(':checked')){
            
            art.closest('label').css(colorStyle);
        } else {
    
            art.closest('label').css(defaultStyle);
    
        }
    
    });

    // style sci chips on click
    sci.click(function() {
        if (sci.is(':checked')){
            
            sci.closest('label').css(colorStyle);
        } else {
    
            sci.closest('label').css(defaultStyle);
    
        }
    
    });

     // style vsa chips on click
     vsa.click(function() {
        if (vsa.is(':checked')){
            
            vsa.closest('label').css(colorStyle);
        } else {
    
            vsa.closest('label').css(defaultStyle);
    
        }
    
    });
    // style bus chips on click
    bus.click(function() {
        if (bus.is(':checked')){
            
            bus.closest('label').css(colorStyle);
        } else {
    
            bus.closest('label').css(defaultStyle);
    
        }
    
    });
    // style hme chips on click
    hme.click(function() {
        if (hme.is(':checked')){
            
            hme.closest('label').css(colorStyle);
        } else {
    
            hme.closest('label').css(defaultStyle);
    
        }
    
    });

}); //end of document.ready function


/* -------------------------------- applies chips style on page reload. ----------------------- */
window.onload = function() { 
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
        },
        individualChips = $('#id_2-class_type_0'),
        groupChips = $('#id_2-class_type_1'),
        onlineChips = $('#id_2-class_type_2');

/* ------------------------------------ Class Type Chips ----------------------------- */
  
    // chip id 0 for class-type
    if (individualChips.is(':checked')){
        individualChips.closest('label').css(colorStyle);
    } else {
    
        individualChips.closest('label').css(defaultStyle);
    
    }
    // chip id 1 for class-type
    if (groupChips.is(':checked')){
        groupChips.closest('label').css(colorStyle);
    } else {
    
        groupChips.closest('label').css(defaultStyle);

    }
    // chip id 2 for class-type
    if (onlineChips.is(':checked')){
        onlineChips.closest('label').css(colorStyle);
    } else {
    
        onlineChips.closest('label').css(defaultStyle);

    }

    /* ------------------------------- Courses/subjects chips ------------------------------*/ 

// *** Currently not working because it is last step of the form and doesnt save on reload 
    // define variables 
    const early = $('#id_3-tutoring_programs_0'), 
      prjhs = $('#id_3-tutoring_programs_1'),
      art = $('#id_3-tutoring_programs_2'),
      sci = $('#id_3-tutoring_programs_3'),
      vsa = $('#id_3-tutoring_programs_4'),
      bus = $('#id_3-tutoring_programs_5'),
      hme = $('#id_3-tutoring_programs_6'),
      tec = $('#id_3-tutoring_programs_7');
    
    // list of courses under programme
    const earlyCourses = $("#id_3-courses_subjects_0, #id_3-courses_subjects_1, #id_3-courses_subjects_2"),
        primjhsCourses = $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5"),
        artCourses = $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5, #id_3-courses_subjects_6, #id_3-courses_subjects_7, #id_3-courses_subjects_8, #id_3-courses_subjects_9, #id_3-courses_subjects_10, #id_3-courses_subjects_11, #id_3-courses_subjects_12"),
        sciCourses = $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5, #id_3-courses_subjects_13, #id_3-courses_subjects_14, #id_3-courses_subjects_15, #id_3-courses_subjects_28"),
        vsaCourses = $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5, #id_3-courses_subjects_16, #id_3-courses_subjects_17, #id_3-courses_subjects_18, #id_3-courses_subjects_19, #id_3-courses_subjects_20, #id_3-courses_subjects_21, #id_3-courses_subjects_22, #id_3-courses_subjects_23"),
        busCourses = $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5, #id_3-courses_subjects_24, #id_3-courses_subjects_25, #id_3-courses_subjects_26, #id_3-courses_subjects_27, #id_3-courses_subjects_28"),
        hmeCourses = $("#id_3-courses_subjects_3, #id_3-courses_subjects_4, #id_3-courses_subjects_5, #id_3-courses_subjects_29, #id_3-courses_subjects_30, #id_3-courses_subjects_32");

    if (early.is(':checked')){
        
        early.closest('label').css(colorStyle);
    } else {
        console.log('reload working');
        early.closest('label').css(defaultStyle);

    }
    // if early years chips is checked -- show courses
    if (early.is(':checked')){
        console.log('reload working');
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

    // if  primary/jhs chips is checked -- show courses
    if (prjhs.is(':checked')){
        // show courses
        primjhsCourses.closest('label').css({
            "display":"inline-block",   
        });
    } else {
        // hide courses
        primjhsCourses.closest('label').css({
            "display":"none"
        });

    }
    
     // if  art chips is checked -- show courses
     if (art.is(':checked')){
        // show courses
        artCourses.closest('label').css({
            "display":"inline-block",   
        });
    } else {
        // hide courses
        artCourses.closest('label').css({
            "display":"none"
        });

    }

     // if  sci chips is checked -- show courses
     if (sci.is(':checked')){
        // show courses
        sciCourses.closest('label').css({
            "display":"inline-block",   
        });
    } else {
        // hide courses
        sciCourses.closest('label').css({
            "display":"none"
        });

    }

    // if  vsa chips is checked -- show courses
    if (vsa.is(':checked')){
        // show courses
        vsaCourses.closest('label').css({
            "display":"inline-block",   
        });
    } else {
        // hide courses
        vsaCourses.closest('label').css({
            "display":"none"
        });

    }

    // if  bus chips is checked -- show courses
    if (bus.is(':checked')){
        // show courses
        busCourses.closest('label').css({
            "display":"inline-block",   
        });
    } else {
        // hide courses
        busCourses.closest('label').css({
            "display":"none"
        });

    }
    // if  hme chips is checked -- show courses
    if (hme.is(':checked')){
        // show courses
        hmeCourses.closest('label').css({
            "display":"inline-block",   
        });
    } else {
        // hide courses
        hmeCourses.closest('label').css({
            "display":"none"
        });

    }
};