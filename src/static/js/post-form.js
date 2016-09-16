$(document).ready(function(){

  $(".content-markdown").each(function(){
    var content = $(this).text();
    var markedContent = marked(content);
    $(this).html(markedContent);
  });

  var titleInput = $("#id_title");
  var contentInput = $("#id_content");

  function setContent(value) {
    if (value !== undefined) {
      var markedContent = marked(value);
      $("#preview-content").html(markedContent);
      $("#preview-content img").each(function(){
        $(this).addClass("img-responsive");
      });
    }
  }

  // initializes the content preview
  setContent(contentInput.val());

  contentInput.keyup(function(){
    var newContent = $(this).val();
    setContent(newContent);
  });

  function setTitle(value){
    $("#preview-title").text(value);
  }

  setTitle(titleInput.val());

  titleInput.keyup(function(){
    var newTitle = $(this).val();
    setTitle(newTitle);
  });

});