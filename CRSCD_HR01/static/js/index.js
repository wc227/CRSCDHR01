$(function(){

    var postCon = $('#postCon');

    // 查看详情
    postCon.delegate('#showDetail', 'click', function(){
        $(this).addClass('hidden').siblings("#postDes, #hideDetail").removeClass('hidden');
    });

    // 隐藏详情
    postCon.delegate('#hideDetail', 'click', function(){
        $(this).addClass('hidden').siblings('#postDes').addClass('hidden').siblings('#showDetail').removeClass('hidden');
    });

    // 职位申请
    postCon.delegate('#postApply', 'click', function(){
        var obj = $(this);
        $.get('/position/postHandle/?type=apply&positionID='+$(this).siblings("#positionID").html(),function(data){
            if(data.success===1){
                obj.addClass('hidden').siblings('#applySuccess').removeClass('hidden').siblings('#postStore, #favSuccess').addClass('hidden');
            }
            else{
                alert('请登录');
                window.location.replace('/user/logIn/')
            }
        });
    });

    // 职位收藏
    postCon.delegate('#postStore', 'click', function(){
        var obj = $(this);
        $.get('/position/postHandle/?type=fav&positionID='+$(this).siblings("#positionID").html(), function(data){
            if(data.success===1){
                obj.addClass('hidden').next().removeClass('hidden');
            }
            else{
                alert('请登录');
                window.location.replace('/user/logIn/')
            }
        });
    });


});

