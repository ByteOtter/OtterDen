document.addEventListener('DOMContentLoaded', function () {
    var postContent = document.getElementById("article-content");
    let link = postContent.textContent;

    // find and replace urls within the content of a post and create a hyperlink to that website
    function replaceURLs(postContent) {
        if (!postContent) return;

        var urlRegex = /(((https?:\/\/)|(www\.))[^\s]+)/g;
        return postContent.replace(urlRegex, function (url) {
            var hyperlink = url;
            if (!hyperlink.match('^https?:\/\/')) {
                hyperlink = 'http://' + hyperlink;
            }
            return '<a class="article-content-link" href="' + hyperlink + '" target="_blank" rel="noopener noreferrer">' + url + '</a>'
        });
    }

    // escape meta characters to avoid XSS
    function escapeHtml(link) {
        return link
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
    }

    document.getElementById("article-content").innerHTML = replaceURLs(escapeHtml(link))
}, false);
