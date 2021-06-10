$("#js-tweet-btn").on("click", function (e) {
    let $tweetLink = "https://twitter.com/intent/tweet?text="+encodeURIComponent($('.js-form').val())
    window.open($tweetLink, '_blank'); // 新しいタブを開き、ページを表示
});
