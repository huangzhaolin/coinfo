/**
 * Created with PyCharm.
 * User: zhaolin.huang
 * Date: 14-1-11
 * Time: 下午5:12
 * To change this template use File | Settings | File Templates.
 */
coinfo.template = {}
coinfo.template.pannel = function (head, body) {
    return "<section class=\"panel\"><header class=\"panel-heading\">" +
        head +
        "<span class=\"tools pull-right\">" +
        "<a class=\"icon-chevron-down\"></a>" +
        "<a class=\"icon-remove\"></a>" +
        "</span>" +
        "</header>" +
        "<div class=\"panel-body\">" +
        body +
        "</div>" +
        "</section>";
};

coinfo.template.weiboUser = function (weiboType, userInfo) {
    var description = "description" in userInfo ? userInfo["description"] : "";
    description = description.length > 15 ? description.slice(0, 15) + "..." : description;
    var subscribeButton = "<button type=\"button\" class=\"btn btn-success btn-xs\" onclick=\"subscribeWeiboUser('" + weiboType + "','" + userInfo['id'] + "',this)\"><i class=\"icon-eye-open\"></i> <span>关注</span> </button>";
    var subscribedButton="<button type=\"button\" class=\"btn btn-defualt btn-xs\" ><i class=\"icon-eye-open\"></i> <span>已关注</span> </button>";
    return "<article class=\"media\">" +
        "<a class=\"pull-left thumb p-thumb\">" +
        "<img src=\"" + userInfo["avatar_hd"] + "\">" +
        "</a><div class=\"media-body pull-left\">" +
        "<a class=\"cmt-head\" href=\"http://weibo.com/" + userInfo["profile_url"] + "\" target='_blank'>" + userInfo["name"] + "</a>" +
        "<p> <i>" + userInfo["location"] + "</i> " + description + "</p>" +
        "</div><div class=\"pull-right hidden-phone\">" +
        (userInfo["subscribed"]?subscribedButton:subscribeButton)+
        "</div></article>";
};