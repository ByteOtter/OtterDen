document.addEventListener('DOMContentLoaded', function(){
  var img = document.getElementById("img-not-modal");
  
  var modal = document.getElementById("modal-img");
  var modalImg = document.getElementById("img-modal");

  if (img != null) {
    img.addEventListener('click', function(){
      modal.style.display = "block";
      modalImg.src = this.src;
      var span = document.getElementsByClassName('close')[0];
      span.onclick = function() {
        modal.style.display = "none";
      }
    });
  }
});
 