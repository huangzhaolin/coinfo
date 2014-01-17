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
