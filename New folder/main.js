
const facebookbutton = document.querySelector(".facebookbtn");
const whatsappbutton = document.querySelector(".whatsappbtn");
const linkedinbutton = document.querySelector(".linkedinbtn");
const twitterbutton = document.querySelector(".twitterbtn");

function init(){
    let postUrl=encodeURI(document.location.href);
    let postTitle = encodeURI("Check out our new page!");


    facebookbutton.setAttribute("href",'https://www.facebook.com/sharer.php?u=${postUrl}');

    whatsappbutton.setAttribute("href",'https://api.whatsapp.com/send?text=${postTitle}${postUrl}');

    linkedinbutton.setAttribute("href",'https://www.linkedin.com/shareArticle?url=${postUrl}&title=${posttitle}');

    twitterbutton.setAttribute("href",'https://twitter.com/share?url=${postUrl}&text=${posttitle}&via=[via]&hashtags=[hashtags]');
}
init();/* to call the init function when the page loads*/