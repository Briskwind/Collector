/**
 * Created by xufengxu on 2018/10/31.
 */

function setCookie(name, value, expTime) {
    // 过期时间 要乘以 1000
    var exp = new Date();
    exp.setTime(exp.getTime() + expTime * 1000);
    document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString();
}


function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
        return unescape(arr[2]);
    else
        return null;
}


function delCookie(name) {
    var exp = new Date();
    exp.setTime(exp.getTime() - 1);
    var cval = getCookie(name);
    if (cval != null)
        document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
}


// 通用post
function AjaxPost(url, data, callBack, errorCallBack) {
    var cookies = document.cookie.match(/csrftoken=\w+/g);
    console.log('cookies', cookies)
    var csrftoken;
    if (cookies) {
        csrftoken = document.cookie.match(/csrftoken=\w+/g)[0].replace(/csrftoken=/, '');
    } else {
        csrftoken = ''
    }

    $.ajax({
        url: url,
        type: 'POST',
        data: JSON.stringify(data),
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFTOKEN", csrftoken);
            console.log('beforeSend')
        },
        contentType: 'application/json'

    }).done(function (resp) {
        if (callBack) {
            callBack(resp)

        }

    }).fail(function (err) {
        if (errorCallBack) {
            errorCallBack(err)
        }
    })
};


//
function AjaxGet(url, callBack) {
    $.ajax({
        url: url,
        type: 'GET',
        beforeSend: function (xhr) {
            console.log('beforeSend')
        }

    }).done(function (resp) {
        if (callBack) {
            callBack(resp)
        } else {
            console.log('no callback')
        }

    }).fail(function (err) {
        console.log('err', err.responseJSON)
    })
};


//  通用图片上传 ajax


function UploadFiles(url, data, callBack, errorCallBack) {

    var cookies = document.cookie.match(/csrftoken=\w+/g);
    var csrftoken;
    if (cookies) {
        csrftoken = document.cookie.match(/csrftoken=\w+/g)[0].replace(/csrftoken=/, '');
    } else {
        csrftoken = ''
    }

    $.ajax({
        url: url,
        type: 'POST',
        cache: false,
        data: data,
        processData: false,
        contentType: false,
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFTOKEN", csrftoken);
            console.log('beforeSend')
        },

    }).done(function (resp) {
        if (callBack) {
            callBack(resp)
        }

    }).fail(function (err) {
        if (errorCallBack) {
            errorCallBack(err)
        }
    })

}


// 删除列表中当指定元素
function findIndex(val, list) {
    for (var i = 0; i < list.length; i++) {
        if (list[i] == val) return i;
    }
    return -1;
};

function delValue(val, list) {
    var index = findIndex(val, list);
    if (index > -1) {
        list.splice(index, 1);
    }
};


// 数组去重
function unique(array){
    var n = [];//临时数组
    for(var i = 0;i < array.length; i++){
        if(n.indexOf(array[i]) == -1) n.push(array[i]);
    }
    return n;
}
