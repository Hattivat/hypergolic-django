$(function(){
    $('form').find('[type=radio], [type=checkbox]').removeClass('form-control').addClass('form-check-input');
    $('form').find('[type=radio], [type=checkbox]').parent('div, p').addClass('form-check');
    $('form').find('[type=radio], [type=checkbox]').sibling('label').addClass('form-check-label');
});