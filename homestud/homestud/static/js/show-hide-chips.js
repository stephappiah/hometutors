


$(document).ready(function(){
    

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


    $('.chips_class_type').click(function(){

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

}); //end of document.ready function