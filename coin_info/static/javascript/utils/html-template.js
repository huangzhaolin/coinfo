/**
 * Created with PyCharm.
 * User: zhaolin.huang
 * Date: 14-1-11
 * Time: 下午5:12
 * To change this template use File | Settings | File Templates.
 */
coinfo.template={}
coinfo.template.pannel=function(head,body){
    return "<section class=\"panel\"><header class=\"panel-heading\">" +
        head +
        "<span class=\"tools pull-right\">" +
        "<a class=\"icon-chevron-down\"></a>" +
        "<a class=\"icon-remove\"></a>" +
        "</span>" +
        "</header>" +
        "<div class=\"panel-body\">" +
        body+
        "</div>"+
        "</section>";
};

