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

    var name = $('#name');
    var phone = $('#phone');
    var work_year = $('#work_year');
    var live_location = $('#live_location');
    var study_location = $('#study_location');
    var identity_id = $('#identity_id');
    var age = $('#age');
    var party = $('#party');


    //定义失去焦点函数
    name.blur(function(){check_name();});
    phone.blur(function(){check_phone();});
    work_year.blur(function(){check_work_year();});
    live_location.blur(function(){check_live_location();});
    study_location.blur(function(){check_study_location();});
    identity_id.blur(function(){check_identity_id();});
    age.blur(function(){check_age();});
    party.blur(function(){check_party();});

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
        if(work_year.val()!=='请选择'){
            input_true(work_year);
            error_work_year = false;
        }
        else{
            input_false(work_year, '请选择工作年限。');
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

    //日期函数
    $(".form_datetime").datetimepicker({
        format: "yyyy-mm-dd",
        todayHighlight:1,
        minView: "day",
        startView: 2,
        forceParse: 0,
        showMeridian:1,
        autoclose:1
    });




});
