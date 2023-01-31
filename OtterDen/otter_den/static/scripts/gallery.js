document.addEventListener('DOMContentLoaded', function(){

  var modal = document.getElementById("modal-img");
  var img = document.getElementById("img-not-modal");
  var modalImg = document.getElementById("img-modal");

  img.addEventListener('click', function(){
    modal.style.display = "block";
    modalImg.src = this.src;
    var span = document.getElementsByClassName('close')[0];
    span.onclick = function() {
      modal.style.display = "none";
    }
  });
});
 