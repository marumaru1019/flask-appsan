$(".js-tag").on("click", function (e) {
    // trim() can remove empty elements
    // WARNING: textareaから中身を取得するときにはtext()でなく、val()を使う
    let $before_text = $("#js-tweet").val();
    let $tag = $(this).text();
    $(".js-form").val($before_text.trim()+" "+$tag.trim());
});
