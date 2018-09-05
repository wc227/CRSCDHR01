$(function(){

    //定义变量
    var error_name = false;
    var error_phone = false;
    var error_age = false;
    var error_work_year = false;
    var error_live_location = false;
    var error_study_location = false;
    var error_identity_id = false;
    var error_party = false;
    var error_company = false;
    var error_post = false;
    var error_workTime = false;
    var error_pos_desc = false;
    var error_school = false;
    var error_profession = false;
    var error_school_time = false;
    var error_education = false;
    var error_degree = false;
    var error_profession_desc = false;

    var name = $('#name');
    var phone = $('#phone');
    var work_year = $('#work_year');
    var live_location = $('#live_location');
    var study_location = $('#study_location');
    var identity_id = $('#identity_id');
    var age = $('#age');
    var party = $('#party');
    var company = $('#company');
    var post = $('#post');
    var work_start_time = $('#work_start_time');
    var work_end_time = $('#work_end_time');
    var post_desc = $('#post_desc');
    var school = $('#school');
    var profession = $('#profession');
    var school_start_time = $('#school_start_timel');
    var school_end_time = $('#school_end_time');
    var education = $('#education');
    var degree = $('#degree');
    var profession_desc = $('#profession_desc');

    //定义失去焦点函数
    name.blur(function(){check_name();});
    phone.blur(function(){check_phone();});
    work_year.blur(function(){check_work_year();});
    live_location.blur(function(){check_live_location();});
    study_location.blur(function(){check_study_location();});
    identity_id.blur(function(){check_identity_id();});
    age.blur(function(){check_age();});
    party.blur(function(){check_party();});
    company.blur(function(){check_company();});
    post.blur(function(){check_post();});
    post_desc.blur(function(){check_post_desc();});
    school.blur(function (){check_school();});
    profession.blur(function(){check_profession();});
    education.blur(function(){check_education();});
    degree.blur(function(){check_degree();});


    //字段校验函数

    //样式调整函数(输入正确）
    function input_true(field){
        field.parent().parent().addClass('has-success').removeClass('has-error');
        field.next('p').addClass('hidden');
    }

    //样式调整函数(输入错误）
    function input_false(field,text){
        field.parent().parent().addClass('has-error').removeClass('has-success');
        field.next('p').removeClass('hidden').html(text);
        error_name = true;
    }

    //姓名校验函数
    function check_name(){
        var len = name.val().length;
        if(len<=1||len>5){
            var text = '请输入正确的姓名';
            input_false(name,text);
            error_name = true;
        }
        else{
            input_true(name);
            error_name = false;
        }
    }

    //手机号校验函数
    function check_phone(){
        var re = /^1[34578]\d{9}$/;
        if(re.test(phone.val())){
            input_true(phone);
            error_phone = false;
        }
        else{
            var text = '请输入正确的手机号';
            input_false(phone, text);
            error_phone = true;
        }
    }

    //年龄校验函数
    function check_age(){
        var re = /^\d{2}$/;
        if(re.test(age.val()) && age.val()>=18 && age.val()<60){
            input_true(age);
            error_age = false;
        }
        else{
            var text = '请填写两位纯数字';
            if(age.val()<18 && age.val()>0){text = '雇用未成年人是非法用工！';}
            if(age.val()>60){text = '除了工作，人生还可以更精彩！';}
            input_false(age, text);
            error_age = false;
        }
    }

    //工作年限校验函数
    function check_work_year(){
        var value = work_year.val();
        if(value=='请选择'){
            input_false(work_year, '请选择工作年限。');
            error_work_year = true;
        }
        if(value=='应届毕业生'){
            $('#info_work').addClass('hidden');
            $('#info_work_box').addClass('hidden');
            input_true(work_year);
            error_work_year = true;
        }
        if(value!=='应届毕业生' && value!=='请选择'){
            $('#info_work').removeClass('hidden');
            $('#info_work_box').removeClass('hidden');
            input_true(work_year);
            error_work_year = true;
        }
    }

    //政治面貌校验函数
    function check_party(){
        if(party.val()!=='请选择'){
            input_true(party);
            error_party = false;
        }
        else{
            input_false(party, '请选择政治面貌。');
            error_work_year = true;

        }
    }

    //居住地校验函数
    function check_live_location(){
        var len = live_location.val().length;
        if(len<=2||len>12){
            var text = '请输入现居住地，精确到省市区即可。';
            input_false(live_location, text);
            error_live_location = true;
        }
        else{
            input_true(live_location);
            error_live_location = false;
        }
    }

    //生源地校验函数
    function check_study_location(){
        var len = study_location.val().length;
        if(len<=2||len>8){
            var text = '请输入生源地，精确到省市即可，例如“黑龙江哈尔滨”。';
            input_false(study_location, text);
            error_study_location = true;
        }
        else{
            input_true(study_location);
            error_study_location = false;
        }
    }

    //身份证号校验函数
    function check_identity_id(){
        var re = /^(^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$)|(^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])((\d{4})|\d{3}[Xx])$)$/
        if(re.test(identity_id.val())){
            input_true(identity_id);
            error_identity_id = false;
        }
        else{
            var text = '请输入正确的身份证号';
            input_false(identity_id, text);
            error_identity_id = true;
        }
    }

    //工作单位校验函数
    function check_company(){
        var len = company.val().length;
        if(len>0 && len<50){
            input_true(company);
            error_company = false;
        }
        else{
            var text = '请输入正确的公司名称。';
            input_false(company, text);
            error_company = true;
        }
    }

    //职位校验函数
    function check_post(){
        var len = post.val().length;
        if(len>0 && len<50){
            input_true(post);
            error_post = false;
        }
        else{
            var text = '请输入正确的职务。';
            input_false(post, text);
            error_post = true;
        }
    }

    //工作时间校验函数
    function check_workTime(){
        var value1 = work_start_time.val();
        var value2 = work_end_time.val();
        if(value1!=='' && value2!=='' && value2>value1){
            input_true(work_start_time);
            input_true(work_end_time);
            error_workTime = false;
        }
        if(value1==''||value2==''){
            var text = '请选择开始时间和结束时间。';
            input_false(work_start_time,text);
            input_false(work_end_time,text);
            error_workTime = true;
        }
        if(value2<=value1){
            text  = '开始时间应早于结束时间。';
            input_false(work_start_time,text);
            input_false(work_end_time, text);
            error_workTime = true;
        }
    }

    //职责描述校验函数
    function check_post_desc(){
        var len = post_desc.val().length;
        if(len>0){
            input_true(post_desc);
            error_pos_desc = false;
        }
        else{
            var text = '请输入职责描述。';
            input_false(post_desc, text);
            error_pos_desc = true;
        }
    }

    //学校校验函数
    function check_school(){
        var len = school.val().length;
        if(len>0 && len<50){
            input_true(school);
            error_school = false;
        }
        else{
            var text = '请输入正确的学校名称。';
            input_false(school,text);
            error_school = true;
        }
    }

    //专业校验函数
    function check_profession(){
        var len = profession.val().length;
        if(len>0 && len<50){
            input_true(profession);
            error_profession = false;
        }
        else{
            var text = '请输入正确的专业名称。';
            input_false(profession,text);
            error_profession = true;
        }
    }

    //学历校验函数
    function check_education(){
        var value = education.val();
        if(value==='请选择'){
            var text = '请选择学历。';
            input_false(education, text);
            error_education = true;
        }
        else{
            input_true(education);
            error_education = false;
        }
    }

    //学位校验函数
    function check_degree(){
        var value = degree.val();
        if(value==='请选择'){
            var text = '请选择学位。';
            input_false(degree, text);
            error_degree = true;
        }
        else{
            input_true(degree);
            error_degree = false;
        }
    }

    //学历时间校验函数
    function check_school_time(){
        var startTime = school_start_time.val();
        var endTime = school_end_time.val();
        if(startTime==''||endTime==''){
            var text = '请选择入学时间和毕业时间。';
            input_false(school_end_time, text);
            error_school_time = true;
        }
        if(startTime<=endTime){
            text = '入学时间应早于毕业时间。';
            input_false(school_end_time, text);
            error_school_time = true;
        }
        else{
            input_true(school_end_time);
            error_school_time = false;
        }
    }



    //日期函数
    $('.datetime').datetimepicker({
        format: "yyyy-mm-dd",
        weekStart: '1',
        start:'1990-01-01',
        language:'zh-CN',
        todayHighlight:1,
        minView: 2,
        forceParse: 0,
        showMeridian:1,
        autoclose:1,
        pickerPosition:'bottom-left',
    });




});