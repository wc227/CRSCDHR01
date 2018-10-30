$(function(){

    // 职位类别选择器
    var typeList = [];

    var locationList = [];


    $('#typeFilter').delegate('a', 'click', function(){
        var obj = $(this);
        filterFunc(obj, typeList);
        displayControl();
    });

    $('#locationFilter').delegate('a', 'click', function(){
        var obj = $(this);
        filterFunc(obj, locationList);
        displayControl();
    });

    function filterFunc(obj, list){
        var filter = obj.html();
        var index = list.indexOf(filter);
        if(obj.data('status') === 0){
            obj.addClass('colorChange1').removeClass('colorChange2');
            list.push(filter);
            obj.data('status', 1);
        }
        else{
            obj.removeClass('colorChange1').addClass('colorChange2');
            list.splice(index,1);
            obj.data('status', 0);
        }
    }

    function displayControl() {
        $('.positions').each(function(){
            var obj = $(this);
            var type = obj.children('#postType').html();
            var location = obj.children('#postLocation').html();
            var typeExist = $.inArray(type, typeList);
            var locationExist = $.inArray(location, locationList);
            var lenType = typeList.length;
            var lenLocation = locationList.length;

            if(lenLocation===0 && lenType!==0 && typeExist===-1){
                obj.hide();
            }
            else if(lenLocation!==0 && lenType===0 && locationExist===-1){
                obj.hide();
            }
            else if(lenLocation!==0 && lenType!==0 && locationExist===-1){
                obj.hide();
            }
            else if(lenLocation!==0 && lenType!==0 && typeExist===-1){
                obj.hide();
            }
            else{
                obj.show();
            }


        }) // each
    } // function displayControl


    // 分页



});