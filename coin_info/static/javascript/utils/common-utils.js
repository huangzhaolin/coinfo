coinfo.utils = {};
/**
 * bind enter
 * @param e
 * @param fn
 */
coinfo.utils.bindEnterKey = function (e, fn) {
    $(e).bind("keydown", function (event) {
        if (event.keyCode == 13) {
            fn();
        }
    });
};
coinfo.utils.addLoader=function(e){
  $(e).html("<div align='center'><img src='static/img/loader.gif'/></div>");
};