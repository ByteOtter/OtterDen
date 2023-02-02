document.addEventListener('DOMContentLoaded', function () {

    document.getElementById("pin").addEventListener('click', function () {
        let postId = window.location.pathname.split("/")[2]
        fetch('/post/' + postId + '/pin', {
            method: 'POST',
        })
    }, false);
}, false);