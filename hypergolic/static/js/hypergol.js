$(function(){
    $('form').children('select, :text, :password, :email, :url, :search, \
                       :datetime-local, :date, :month, :time, :week, :number,\
                       :tel, :color').addClass('form-control');
    $('form').children('div, p').addClass('form-group');
    $('form').children(':file').addClass('form-control-file');
    $('form').children(':radio, :checkbox').addClass('form-check-input');
    $('form').children(':radio, :checkbox').parent('div, p').addClass('form-check');
    $('form').children(':radio, :checkbox').sibling('label').addClass('form-check-label');
});