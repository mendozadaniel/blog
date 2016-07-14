$(document).ready(function(){

  $(".post-detail-item img").each(function(){
    $(this).addClass("img-responsive");
  });

  // Toggles comment window when reply button is clicked
  $(".comment-reply-btn").click(function(event){
    event.preventDefault();
    $(this).parent().next(".comment-reply").fadeToggle();
  });
});
