$(function(){

    //定义变量
    var error_password = false;
    var error_check_password = false;
    var error_email = false;
    var error_check = true;
    var error_name = false;
    var error_login = true;
    var user_email = $('#user_email');
    var user_pwd = $('#user_pwd');
    var user_cpwd = $('#user_cpwd');
    var name = $('#name');
    var login_email = $('#login_email');
    var login_pwd = $('#login_pwd');

    //定义失去焦点函数
    name.blur(function(){check_name();});
    user_email.blur(function(){check_email();});
    user_pwd.blur(function(){check_pwd();});
    user_cpwd.blur(function(){check_cpwd();});
    //login_email.blur(function(){login_email_check();});

    //校验是否同意声明
    $('#agree').click(function(){
        if($(this).is(':checked')){
            error_check = false;
            $('#agree_warn').addClass('hidden');
        }
        else{
            error_check = true;
            $('#agree_warn').removeClass('hidden');
        }
    });

    //姓名校验函数
    function check_name(){
        var len = name.val().length;
        var name_box = $('#nameBox');
        var name_false = $('#name_false');
        var name_true = $('#name_true');
        var name_warn = $('#name_warn');

        if(len<=1||len>10){
            name_box.addClass('has-error').removeClass('has-success');
            name_false.removeClass('hidden');
            name_true.addClass('hidden');
            name_warn.removeClass('hidden').html('此输入正确的姓名。');
            error_name = true;
        }
        else{
            name_box.removeClass('has-error').addClass('has-success');
            name_false.addClass('hidden');
            name_true.removeClass('hidden');
            name_warn.addClass('hidden');
            error_name = false;
        }
    }

    //邮箱校验函数
    function check_email(){
        var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/
        var email_box = $('#emailBox');
        var email_false = $('#email_false');
        var email_true = $('#email_true');
        var email_warn = $('#email_warn');

        //验证邮箱格式是否正确
        if(re.test(user_email.val())){

            // 验证邮箱是否已经注册
            $.get('/user/register_exist/?user_email='+user_email.val(),function(data){
                if(data.count==1){
                    email_box.addClass('has-error').removeClass('has-success');
                    email_false.removeClass('hidden');
                    email_true.addClass('hidden');
                    email_warn.removeClass('hidden').html('此邮箱已注册。');
                    error_email = true;
                }
                else{
                    email_box.addClass('has-success').removeClass('has-error');
                    email_false.addClass('hidden');
                    email_true.removeClass('hidden');
                    email_warn.addClass('hidden');
                    error_email = false;
                }
            })
        }
        else{
            email_box.addClass('has-error').removeClass('has-success');
            email_false.removeClass('hidden');
            email_true.addClass('hidden');
            email_warn.removeClass('hidden').html('请输入正确的邮箱。');
            error_email = false;
        }
    }

    //校验密码长度函数
    function check_pwd(){
        var pwd_box = $('#pwdBox');
        var pwd_warn = $('#pwd_warn');
        var pwd_true = $('#pwd_true');
        var pwd_false = $('#pwd_false');
        var len = $('#user_pwd').val().length;

        if(len<8||len>20){
            pwd_box.addClass('has-error').removeClass('has-success');
            pwd_warn.removeClass('hidden').html('密码长度应为8-20位。');
            pwd_false.removeClass('hidden');
            pwd_true.addClass('hidden');
            error_password = true;
        }
        else{
            pwd_box.addClass('has-success').removeClass('has-error');
            pwd_warn.addClass('hidden');
            pwd_false.addClass('hidden');
            pwd_true.removeClass('hidden');
            error_password = false;
        }
    }

    //校验密码一致性函数
    function check_cpwd(){
        var cpwd = user_cpwd.val();
        var pwd =  user_pwd.val();
        var cpwd_box = $('#cpwdBox');
        var cpwd_true = $('#cpwd_true');
        var cpwd_false = $('#cpwd_false');
        var cpwd_warn = $('#cpwd_warn');


        if(cpwd==pwd && error_password==false){
            cpwd_box.addClass('has-success').removeClass('has-error');
            cpwd_true.removeClass('hidden');
            cpwd_false.addClass('hidden');
            cpwd_warn.addClass('hidden');
            error_check_password = false;
        }
        else{
            cpwd_box.addClass('has-error').removeClass('has-success');
            cpwd_true.addClass('hidden');
            cpwd_false.removeClass('hidden');
            cpwd_warn.removeClass('hidden').html('两次输入的密码不一致。');
            error_check_password = true;
        }
    }

    //提交注册综合校验
    $('#reg_form').submit(function(){
        check_name();
        check_email();
        check_pwd();
        check_cpwd();
        if(error_name==false && error_email==false && error_password==false && error_check_password==false && error_check==false){
            alert('注册成功')
            return true;
        }
        else {
            return false;
        }
    });

    //修改密码

});

