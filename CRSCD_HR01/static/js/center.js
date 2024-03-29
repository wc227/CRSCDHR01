$(function(){
    // 日期函数
    $('body*').delegate('.datetime', 'mouseenter', function(){
        $('.datetime').datetimepicker({
            format: "yyyy-mm-dd",
            weekStart: '1',
            startView: 2,
            language:'zh-CN',
            minView: 2,
            autoclose: 1,
            pickerPosition:'bottom-center',
        });
    });

    // 样式调整函数(输入正确）
    function input_true(field){
        field.parent().parent().addClass('has-success').removeClass('has-error');
        field.next('p').addClass('hidden');
    }

    // 样式调整函数(输入错误）
    function input_false(field,text){
        field.parent().parent().addClass('has-error').removeClass('has-success');
        field.next('p').removeClass('hidden').html(text);
    }

// 基本信息校验
    var name = $('#name');
    var phone = $('#phone');
    var work_year = $('#work_year');
    var live_location = $('#live_location');
    var study_location = $('#study_location');
    var identity_id = $('#identity_id');
    var age = $('#age');
    var party = $('#party');

    var error_name = false;
    var error_phone = false;
    var error_age = false;
    var error_work_year = false;
    var error_live_location = false;
    var error_study_location = false;
    var error_identity_id = false;
    var error_party = false;

    // 姓名校验函数
    function check_name(){
        var len = name.val().length;
        if(len<=1||len>20){
            var text = '请输入正确的姓名';
            input_false(name,text);
            error_name = true;
        }
        else{
            input_true(name);
            error_name = false;
        }
    }

    // 手机号校验函数
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

    // 年龄校验函数
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

    // 工作年限校验函数
    function check_work_year(){
        var value = work_year.val();
        if(value==='请选择'){
            input_false(work_year, '请选择工作年限。');
            error_work_year = true;
        }
        if(value==='应届毕业生'){
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

    // 政治面貌校验函数
    function check_party(){
        if(party.val()!=='请选择'){
            input_true(party);
            error_party = false;
        }
        else{
            input_false(party, '请选择政治面貌。');
            error_party = true;
        }
    }

    // 居住地校验函数
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

    // 生源地校验函数
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

    // 身份证号校验函数
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

    name.blur(function(){check_name();});
    phone.blur(function(){check_phone();});
    work_year.blur(function(){check_work_year();});
    live_location.blur(function(){check_live_location();});
    study_location.blur(function(){check_study_location();});
    identity_id.blur(function(){check_identity_id();});
    age.blur(function(){check_age();});
    party.blur(function(){check_party();});

// 工作信息校验
    var error_company = false;
    var error_position = false;
    var error_work_time = false;
    var error_work_desc = false;

    // 新增与删除工作信息
    var work_list = $('#work_list');
    var work_add = $('#work_add');
    var work_li = $('#work_list li:first').html();
    var work_li_val = $('<li>' + work_li + '</li>');
    var work_clone = work_li_val.clone();
    var workLen = parseInt($('#workLen').html());
    work_add.click(function(){
        work_clone.clone().appendTo(work_list);
        if(workLen===0){workLen += 2;}
        else{workLen += 1;}
    });

    work_list.delegate('a', 'click', function(){
        if(workLen>1){
            var workId = $(this).parent().parent().children('div:first-child').html();
            $.get('/center/work_del/', {workID: workId});
            $(this).parent().parent().remove();
            workLen -= 1;
        }
        else if(workLen===1){
            $('#work_list li div:last').addClass('hidden');
        }
    });

    // 工作信息校验代理
    work_list.delegate('input, select, textarea', 'blur', function(){
        var id_val = $(this).attr('id');
        switch(id_val){
            case 'company':
                var company = $(this);
                check_company(company);
                break;
            case 'position':
                var position = $(this);
                check_position(position);
                break;
            case 'work_desc':
                var work_desc = $(this);
                check_work_desc(work_desc);
                break;
        }
    });
    work_list.delegate('.datetime', 'change', function(){
        var stime = $(this);
        var etime = $(this).siblings('input');
        if($(this).attr('id')==='work_stime'){
            check_work_time(stime, etime);
        }
    });
    work_list.delegate('.datetime', 'change', function(){
        var stime = $(this).siblings('input');
        var etime = $(this);
        if($(this).attr('id')==='work_etime'){
            check_work_time(stime, etime);
        }
    });

    // 工作单位校验函数
    function check_company(company){
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
    // 职位校验函数
    function check_position(position){
        var len = position.val().length;
        if(len>0 && len<50){
            input_true(position);
            error_position = false;
        }
        else{
            var text = '请输入职务名称。';
            input_false(position, text);
            error_position = true;
        }
    }
    // 职责描述校验函数
    function check_work_desc(work_desc){
        var len = work_desc.val().length;
        if(len>0 && len<200){
            input_true(work_desc);
            error_pos_desc = false;
        }
        else{
            var text = '请输入职责描述，最多200个字符。';
            input_false(work_desc, text);
            error_pos_desc = true;
        }
    }
    // 工作时间校验函数
    function check_work_time(stime, etime){
        var stime_val = stime.val();
        var stime_len = stime.val().length;
        var etime_val = etime.val();
        var etime_len = etime.val().length;
        if(stime_len>0 && etime_len>0 && etime_val>stime_val){
            input_true(etime);
            stime.css("border", "1px solid #3c763d").siblings('input').css("border", "1px solid #3c763d");
            error_work_time = false;
        }
        if(stime_len===0){
            var text = '请选择开始时间。';
            input_false(etime, text);
            stime.css("border", "1px solid #a94442").siblings('input').css("border", "1px solid #a94442");
            error_work_time = true;
        }
        if(etime_len===0){
            text = '请选择结束时间。';
            input_false(etime, text);
            stime.css("border", "1px solid #a94442").siblings('input').css("border", "1px solid #a94442");
            error_work_time = true;
        }
        if(stime_val>=etime_val && etime_len!==0 && stime_len!==0){
            text = '开始时间应早于结束时间。';
            stime.css("border", "1px solid #a94442").siblings('input').css("border", "1px solid #a94442");
            input_false(etime, text);
            error_work_time = true;
        }
    }

// 教育信息校验
    var error_edu = false;
    var error_school = false;
    var error_profession = false;
    var error_edu_time = false;
    var error_education = false;
    var error_degree = false;
    var error_profession_desc = false;

    // 新增教育信息
    var edu_list = $('#edu_list');
    var edu_add = $('#edu_add');
    var edu_li = $('#edu_list li:first').html();
    var edu_li_val = $('<li>' + edu_li + '</li>');
    var edu_clone = edu_li_val.clone();
    var eduLen = parseInt($('#eduLen').html());

    edu_add.click(function(){
        if(eduLen<4){
            edu_clone.clone().appendTo(edu_list);
            if(eduLen===0){eduLen += 2}
            else{eduLen += 1}
            if(eduLen===4){
                edu_add.addClass('hidden');
            }
        }
    });

    // 删除教育信息
    edu_list.delegate('a', 'click', function(){
        if(eduLen>1){
            var eduId = $(this).parent().parent().children('div:first-child').html();
            $.get('/center/edu_del/', {eduId: eduId});
            $(this).parent().parent().remove();
            eduLen --;
            edu_add.removeClass('hidden');
            if(eduLen===1){
                $('#edu_list li div:last').addClass('hidden');
            }
        }
    });

    // 学历校验代理函数
    edu_list.delegate('input, select, textarea', 'blur', function(){
        var id_val = $(this).attr('id');
        switch(id_val){
            case 'school':
                var school = $(this);
                check_school(school);
                break;
            case 'education':
                var education = $(this);
                check_education(education);
                break;
            case 'degree':
                var degree = $(this);
                check_degree(degree);
                break;
            case 'profession':
                var profession = $(this);
                check_profession(profession);
                break;
            case 'profession_desc':
                var profession_desc = $(this);
                check_profession_desc(profession_desc);
                break;
        }
    });
    edu_list.delegate('.datetime', 'change', function(){
        var stime = $(this);
        var etime = $(this).siblings('input');
        if($(this).attr('id')==='edu_stime'){
            check_edu_time(stime, etime);
        }
    });
    edu_list.delegate('.datetime', 'change', function(){
        var stime = $(this).siblings('input');
        var etime = $(this);
        if($(this).attr('id')==='edu_etime'){
            check_edu_time(stime, etime);
        }
    });

    // 学校校验函数
    function check_school(school){
        var len = school.val().length;
        if(len>0 && len<50){
            input_true(school);
            error_school = false;
        }
        else{
            var text = '请输入正确的学校名称。';
            input_false(school, text);
            error_school = true;
        }
    }
    // 学历校验函数
    function check_education(education){
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
    // 专业校验函数
    function check_profession(profession){
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
    // 学位校验函数
    function check_degree(degree){
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
    // 专业描述校验函数
    function check_profession_desc(profession_desc){
        var len = profession_desc.val().length;
        if(len>200){
            var text = '专业描述最多不能超过200字。';
            input_false(profession_desc, text);
            error_profession_desc = true;
        }
        else{
            input_true(profession_desc);
            error_profession_desc =false;
        }
    }
    // 学历日期校验函数
    function check_edu_time(stime, etime){
        var stime_val = stime.val();
        var stime_len = stime.val().length;
        var etime_val = etime.val();
        var etime_len = etime.val().length;
        if(stime_len>0 && etime_len>0 && etime_val>stime_val){
            input_true(etime);
            stime.css("border", "1px solid #3c763d").siblings('input').css("border", "1px solid #3c763d");
            error_edu_time = false;
        }
        if(stime_len===0){
            var text = '请选择入学时间。';
            input_false(etime, text);
            stime.css("border", "1px solid #a94442").siblings('input').css("border", "1px solid #a94442");
            error_edu_time = true;
        }
        if(etime_len===0){
            text = '请选择毕业时间。';
            input_false(etime, text);
            stime.css("border", "1px solid #a94442").siblings('input').css("border", "1px solid #a94442");
            error_edu_time = true;
        }
        if(stime_val>=etime_val && etime_len!==0 && stime_len!==0){
            text = '毕业时间应早于开学时间。';
            stime.css("border", "1px solid #a94442").siblings('input').css("border", "1px solid #a94442");
            input_false(etime, text);
            error_edu_time = true;
        }
    }

    // 简历上传函数
    $('#resume_file').fileinput({
        language: 'zh',
        uploadUrl: '/center/resume_up/',
        allowedFileExtensions: ['pdf', 'jpg', 'png', 'bpm', 'jpeg'],
        showPreview: false,
        overwriteInitial: true,
        maxFileCount: 1,
        maxFileSize: 1024*10,
        autoReplace: true,
        required: true,
    }).on("fileuploaded", function(event, data){
       if(data.response){
           var fileName = data.filenames;
           $('#fileUpBox').addClass('hidden');
           $('#fileViewBox').removeClass('hidden');
           $('#fileView').html(fileName);
           $('#fileFuncBox').removeClass('hidden');
       }
    });

    // 简历删除函数
    $('#resumeDel').click(function(){
        $.post('/center/resume_del/', function(data){
            if(data.delete===1){
                $('#fileUpBox').removeClass('hidden');
                $('#fileViewBox').addClass('hidden');
                $('#fileFuncBox').addClass('hidden');
            }
        });
    });

    // 表单提交函数
    $('#save').click(function(){
        $('#resume_form').submit();
    });

    // 个人中心查看申请职位详情
    $('#postDisplay').on('show.bs.modal', function(event){
        var button = $(event.relatedTarget);
        var recipient = button.data('post');
        var modal = $(this);
        $.get('/center/positionModal/?positionId='+recipient, function(data){
            //接收岗位数据
            var postName = data.position_name;
            var postType = data.position_type;
            var applyType = data.apply_type;
            var company = data.position_company;
            var location = data.position_location;
            var department = data.department;
            var publicDate = data.pub_date;
            var expireDate = data.exp_date;
            var exp = data.exp_req;
            var edu = data.edu_req;
            var num = data.num;
            var responbility = data.position_detail;
            var requirements = data.position_req;
            var responsibilities = responbility.replace(/\n/g,'<br>',);
            var requirement = requirements.replace(/\n/g,'<br>');
            modal.find('.modal-title').text(postName);
            modal.find('#modalPostType').text(postType);
            modal.find('#modalApplyType').text(applyType);
            modal.find('#modalCompany').text(company);
            modal.find('#modalLocation').text(location);
            modal.find('#modalDepartment').text(department);
            modal.find('#modalPublicDate').text(publicDate);
            modal.find('#modalExp').text(exp);
            modal.find('#modalEdu').text(edu);
            modal.find('#modalNum').text(num);
            modal.find('#modalExpireDate').text(expireDate);
            modal.find('#modalResponsibilities').html(responsibilities);
            modal.find('#modalRequirement').html(requirement);
        });

        // 取消申请与收藏
        var applyCancel =  $('#applyCancel');
        var favCancel = $('#favCancel');
        var confirmCancel = $('#confirmCancel');
        var successCancel = $('#successCancel');
        var successFavCancel = $('#successFavCancel');
        var postApply = $('#applyPost');
        var applySuccess = $('#applySuccess');
        var addFav = $('#addFav');
        var addFavSuccess = $('#addFavSuccess');

        applyCancel.removeClass('hidden');
        confirmCancel.addClass('hidden');
        successCancel.addClass('hidden');
        successFavCancel.addClass('hidden');
        applySuccess.addClass('hidden');
        postApply.removeClass('hidden');
        addFav.removeClass('hidden');
        addFavSuccess.addClass('hidden');
        favCancel.removeClass('hidden');


        // 取消申请
        applyCancel.click(function(){
           $(this).addClass('hidden');
           confirmCancel.removeClass('hidden');
        });

        // 确认取消申请
        confirmCancel.click(function(){
            $.get('/position/postHandle/?type=applyCancel&positionID='+recipient,function(){
                button.parent().parent().remove();
                confirmCancel.addClass('hidden');
                successCancel.removeClass('hidden');
            });
        });

        // 取消收藏
        favCancel.click(function(){
            $.get('/position/postHandle/?type=favCancel&positionID='+recipient,function(){
                button.parent().parent().remove();
                favCancel.addClass('hidden');
                successFavCancel.removeClass('hidden');
                postApply.addClass('hidden');
            });
        });

        // 申请职位
        postApply.click(function(){
            var next = window.location.pathname; //获取当前url，并传递给login视图，用于登录后跳转回当前页。
            $.get('/position/postHandle/?type=apply&positionID='+recipient, function(data){
                if(data.success===1){
                    postApply.addClass('hidden');
                    favCancel.addClass('hidden');
                    applySuccess.removeClass('hidden');
                }
                else if(data.success===2){
                    resumeAlert();
                }
                else{
                    loginAlert(next);
                }
            });
        });

        // 职位收藏
        addFav.click(function(){
            var next = window.location.pathname; //获取当前url，并传递给login视图，用于登录后跳转回当前页。
            $.get('/position/postHandle/?type=fav&positionID='+recipient,function(data){
                if(data.success===1){
                    addFav.addClass('hidden');
                    addFavSuccess.removeClass('hidden');
                }
                else if(data.success===2){
                    resumeAlert();
                }
                else{
                    loginAlert(next);
                }
            });
        });

        // 登录提示
        function loginAlert(next){
            alert('请登录');
            window.location.replace('/user/logIn/?next='+next);
        }

        // 维护简历提示
        function resumeAlert(){
            alert('请维护简历');
            window.location.replace('/center/resume/')
        }
    });

    // 显示和隐藏修改密码框
    $('#changePwdBtn').click(function(){
        if($('#changePwdCon').hasClass('hidden')){
            $('#changePwdCon').removeClass('hidden');
            $('#chgPwdBtnCon').addClass('dropup');
        }
        else{
            $('#changePwdCon').addClass('hidden');
            $('#chgPwdBtnCon').removeClass('dropup');
        }
    });

    // 显示和隐藏修改邮箱框
    $('#changeEmailBtn').click(function(){
        if($('#changeEmailCon').hasClass('hidden')){
            $('#changeEmailCon').removeClass('hidden');
            $('#chgEmailBtnCon').addClass('dropup');
        }
        else{
            $('#changeEmailCon').addClass('hidden');
            $('#chgEmailBtnCon').removeClass('dropup');
        }
    });

    // 更改密码
    $('#chgPwdSubmit').click(function(){
        var prePwd = $('#prePwd').val();
        var newPwd = $('#newPwd').val();
        var reNewPwd = $('#reNewPwd').val();
        var chgPwdWarn = $('#chgPwdWarn');

        // 校验密码
        checkPrePwd();

        // 校验原密码函数
        function checkPrePwd(){
            $.post('/user/checkPwd/', {"prePwd": prePwd}, function(data){
                if(data.success===1){
                    checkNewPwd();
                }
                else{
                    chgPwdWarn.html("您输入的原密码有误");
                }
            }, "json");
        }

        // 校验新密码函数
        function checkNewPwd(){
            if(newPwd.length<8){
                chgPwdWarn.html('密码长度最短为8位。');
                return false
            }
            if(newPwd.length>=8 && newPwd!==reNewPwd){
                chgPwdWarn.html('两次输入的密码不一致。');
                return false
            }
            if(newPwd.length>=8 && newPwd===reNewPwd){
                alert("修改成功，请重新登录");
                $('#chgPwdForm').submit();
            }
        }
    });

    // 更改邮箱
    $('#chgEmailSubmit').click(function(){
        var newEmail = $('#newEmail').val();
        var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
        var chgEmailWarn = $('#chgEmailWarn');
        if(re.test(newEmail)){
            // 验证邮箱是否已经注册
            $.get('/user/register_exist/?user_email='+newEmail,function(data){
                if(data.count===1){
                    chgEmailWarn.html("此邮箱已注册。")
                }
                else{
                    alert("修改成功，请使用新邮箱重新登录。");
                    $('#chgEmailForm').submit();
                }
            })
        }
        else{
            chgEmailWarn.html('请输入正确的邮箱。');
        }
    });
});
