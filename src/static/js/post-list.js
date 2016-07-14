$(document).ready(function(){

  $(".post-detail-item img").each(function(){
    $(this).addClass("img-responsive");
  });

  // Makes posts area clickable in post_list view
  $(".thumbnail-post").click(function(){
    window.location=$(this).find("a").attr("href");
    return false;
  });
});